"""
Progress Tracking Utility Module

Handles all progress tracking logic for the Study.Smart application:
- Tracks user answers to MCQ questions
- Calculates progress percentages (completed and understood)
- Syncs progress data to/from Firestore
"""

import streamlit as st
from datetime import datetime
from typing import Dict, List, Optional, Set
import firebase_admin.firestore


def track_question_answer(
    user_id: str,
    course_id: str,
    topic_id: str,
    subtopic_id: str,
    question_id: str,
    is_correct: bool,
    selected_index: Optional[int] = None
) -> bool:
    """
    Records a question answer and updates progress in Firestore.
    
    Args:
        user_id: Firebase user ID
        course_id: Course identifier (e.g., "vwl")
        topic_id: Topic identifier (e.g., "1")
        subtopic_id: Subtopic identifier (e.g., "1.1")
        question_id: Unique question identifier
        is_correct: Whether the answer was correct
    
    Returns:
        True if successfully saved, False otherwise
    """
    try:
        db = firebase_admin.firestore.client()
        progress_ref = db.collection("users").document(user_id).collection("progress").document(course_id)
        
        # Get current progress data
        doc = progress_ref.get()
        if doc.exists:
            progress_data = doc.to_dict()
        else:
            progress_data = {
                "course_id": course_id,
                "last_updated": datetime.utcnow().isoformat(),
                "topics": {}
            }
        
        # Ensure topic structure exists
        if topic_id not in progress_data["topics"]:
            progress_data["topics"][topic_id] = {
                "topic_id": topic_id,
                "subtopics": {}
            }
        
        if subtopic_id not in progress_data["topics"][topic_id]["subtopics"]:
            progress_data["topics"][topic_id]["subtopics"][subtopic_id] = {
                "completed_questions": [],
                "correct_questions": [],
                "answers": {} # Map question_id -> index
            }
        
        sub_data = progress_data["topics"][topic_id]["subtopics"][subtopic_id]
        
        # Ensure answers dict exists (for backward compatibility if data exists)
        if "answers" not in sub_data:
            sub_data["answers"] = {}
        
        # Store index if provided
        if selected_index is not None:
            sub_data["answers"][question_id] = selected_index
        
        # Add question to completed list if not already there
        if question_id not in sub_data["completed_questions"]:
            sub_data["completed_questions"].append(question_id)
        
        # Add to correct list if correct and not already there
        if is_correct and question_id not in sub_data["correct_questions"]:
            sub_data["correct_questions"].append(question_id)
        # Remove from correct list if now incorrect (user changed answer)
        elif not is_correct and question_id in sub_data["correct_questions"]:
            sub_data["correct_questions"].remove(question_id)
        
        # Update timestamp
        progress_data["last_updated"] = datetime.utcnow().isoformat()
        
        # Save detailed progress to sub-collection
        progress_ref.set(progress_data)
        
        # --- DASHBOARD COMPATIBILITY ---
        # Sync overall completion percentage to the main user document
        try:
            from views.course_overview import calculate_topic_progress, SUBTOPIC_QUESTION_COUNTS
            from data import COURSES
            
            course = COURSES.get(course_id)
            if course:
                overall_completed = 0.0
                topic_count = 0
                
                for topic in course["topics"]:
                    t_id = topic["id"].replace("topic_", "")
                    sub_ids = [st["id"] for st in topic.get("subtopics", [])]
                    t_data = progress_data.get("topics", {}).get(t_id, {})
                    
                    completed_pct = calculate_topic_progress(t_data, sub_ids)
                    overall_completed += completed_pct
                    topic_count += 1
                
                if topic_count > 0:
                    summary_pct = overall_completed / topic_count
                    
                    # Update main user doc for dashboard (matches firebase_config.save_progress logic)
                    user_ref = db.collection("users").document(user_id)
                    user_ref.set({
                        "progress": {
                            course_id: summary_pct
                        }
                    }, merge=True)
        except Exception as sync_err:
            print(f"Warning: Failed to sync dashboard progress: {sync_err}")
        
        return True
        
    except Exception as e:
        print(f"Error tracking question answer: {e}")
        return False


def get_user_progress(user_id: str, course_id: str) -> Dict:
    """
    Retrieves user progress from Firestore.
    
    Args:
        user_id: Firebase user ID
        course_id: Course identifier
    
    Returns:
        Progress data dictionary or empty dict if not found
    """
    try:
        db = firebase_admin.firestore.client()
        progress_ref = db.collection("users").document(user_id).collection("progress").document(course_id)
        doc = progress_ref.get()
        
        if doc.exists:
            return doc.to_dict()
        return {}
        
    except Exception as e:
        print(f"Error loading progress: {e}")
        return {}


def get_subtopic_progress(user_id: str, course_id: str, topic_id: str, subtopic_id: str) -> Dict:
    """
    Gets progress for a specific subtopic.
    
    Returns:
        Dict with 'completed_questions' and 'correct_questions' lists
    """
    progress = get_user_progress(user_id, course_id)
    
    if not progress:
        return {"completed_questions": [], "correct_questions": []}
    
    topics = progress.get("topics", {})
    topic_data = topics.get(topic_id, {})
    subtopics = topic_data.get("subtopics", {})
    
    return subtopics.get(subtopic_id, {"completed_questions": [], "correct_questions": []})


def calculate_topic_progress(topic_data: Dict, total_questions_per_subtopic: Dict[str, int]) -> Dict:
    """
    Calculates completed and understood percentages for a topic.
    
    Args:
        topic_data: Topic data from Firestore
        total_questions_per_subtopic: Dict mapping subtopic_id to total question count
    
    Returns:
        Dict with 'completed_pct' and 'understood_pct'
    """
    subtopics = topic_data.get("subtopics", {})
    
    total_completed = 0
    total_correct = 0
    total_questions = 0
    
    for subtopic_id, count in total_questions_per_subtopic.items():
        total_questions += count
        
        if subtopic_id in subtopics:
            subtopic = subtopics[subtopic_id]
            total_completed += len(subtopic.get("completed_questions", []))
            total_correct += len(subtopic.get("correct_questions", []))
    
    if total_questions == 0:
        return {"completed_pct": 0.0, "understood_pct": 0.0}
    
    return {
        "completed_pct": total_completed / total_questions,
        "understood_pct": total_correct / total_questions
    }


    # This is a placeholder for future complex recalculations
    return progress_data


def is_question_answered(user_id: str, course_id: str, topic_id: str, subtopic_id: str, question_id: str) -> bool:
    """
    Checks if a specific question has been answered.
    
    Returns:
        True if answered, False otherwise
    """
    subtopic_progress = get_subtopic_progress(user_id, course_id, topic_id, subtopic_id)
    return question_id in subtopic_progress.get("completed_questions", [])


def is_question_correct(user_id: str, course_id: str, topic_id: str, subtopic_id: str, question_id: str) -> bool:
    """
    Checks if a specific question was answered correctly.
    
    Returns:
        True if answered correctly, False otherwise
    """
    subtopic_progress = get_subtopic_progress(user_id, course_id, topic_id, subtopic_id)
    return question_id in subtopic_progress.get("correct_questions", [])
def get_saved_answer_index(user_id: str, course_id: str, topic_id: str, subtopic_id: str, question_id: str) -> Optional[int]:
    """
    Retrieves the saved answer index for a specific question.
    
    Returns:
        Index (int) or None if not found
    """
    subtopic_progress = get_subtopic_progress(user_id, course_id, topic_id, subtopic_id)
    answers = subtopic_progress.get("answers", {})
    return answers.get(question_id)
