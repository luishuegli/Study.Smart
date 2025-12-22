"""
Test script to verify Firestore connectivity and progress tracking.

Run this script to test if:
1. Firebase Admin SDK is properly initialized
2. Firestore connection works
3. Progress tracking functions work correctly
"""

import firebase_admin
from firebase_admin import credentials, firestore
import os
from datetime import datetime

def test_firestore_connection():
    """Test basic Firestore connectivity"""
    print("=" * 60)
    print("FIRESTORE CONNECTION TEST")
    print("=" * 60)
    
    # Check if Firebase is already initialized
    if not firebase_admin._apps:
        cred_path = "serviceAccountKey.json"
        
        if not os.path.exists(cred_path):
            print(f"❌ ERROR: {cred_path} not found!")
            print(f"   Please download your service account key from Firebase Console")
            print(f"   and save it as 'serviceAccountKey.json' in the project root.")
            return False
        
        try:
            cred = credentials.Certificate(cred_path)
            firebase_admin.initialize_app(cred)
            print("✅ Firebase Admin SDK initialized successfully")
        except Exception as e:
            print(f"❌ Error initializing Firebase: {e}")
            return False
    else:
        print("✅ Firebase Admin SDK already initialized")
    
    # Test Firestore connection
    try:
        db = firestore.client()
        print("✅ Firestore client created successfully")
        
        # Try to write a test document
        test_ref = db.collection("_test").document("connection_test")
        test_data = {
            "test": True,
            "timestamp": datetime.utcnow().isoformat(),
            "message": "Connection test successful"
        }
        
        test_ref.set(test_data)
        print("✅ Successfully wrote test document to Firestore")
        
        # Read it back
        doc = test_ref.get()
        if doc.exists:
            print("✅ Successfully read test document from Firestore")
            print(f"   Data: {doc.to_dict()}")
        
        # Clean up
        test_ref.delete()
        print("✅ Test document deleted")
        
        return True
        
    except Exception as e:
        print(f"❌ Firestore error: {e}")
        return False


def test_progress_tracking():
    """Test progress tracking functions"""
    print("\n" + "=" * 60)
    print("PROGRESS TRACKING TEST")
    print("=" * 60)
    
    try:
        from utils.progress_tracker import track_question_answer, get_user_progress
        
        # Test with a fake user ID
        test_user_id = "test_user_123"
        test_course_id = "vwl"
        
        print(f"\n📝 Testing progress tracking for user: {test_user_id}")
        
        # Track a question answer
        print("\n1. Tracking question answer...")
        success = track_question_answer(
            user_id=test_user_id,
            course_id=test_course_id,
            topic_id="1",
            subtopic_id="1.1",
            question_id="q_1_1_stetig",
            is_correct=True
        )
        
        if success:
            print("   ✅ Question answer tracked successfully")
        else:
            print("   ❌ Failed to track question answer")
            return False
        
        # Retrieve progress
        print("\n2. Retrieving progress...")
        progress = get_user_progress(test_user_id, test_course_id)
        
        if progress:
            print("   ✅ Progress retrieved successfully")
            print(f"   Progress data: {progress}")
            
            # Verify the data structure
            if "topics" in progress:
                if "1" in progress["topics"]:
                    if "1.1" in progress["topics"]["1"]["subtopics"]:
                        subtopic = progress["topics"]["1"]["subtopics"]["1.1"]
                        if "q_1_1_stetig" in subtopic["completed_questions"]:
                            print("   ✅ Question found in completed_questions")
                        if "q_1_1_stetig" in subtopic["correct_questions"]:
                            print("   ✅ Question found in correct_questions")
        else:
            print("   ❌ No progress data retrieved")
            return False
        
        # Clean up test data
        print("\n3. Cleaning up test data...")
        db = firestore.client()
        db.collection("users").document(test_user_id).collection("progress").document(test_course_id).delete()
        print("   ✅ Test data cleaned up")
        
        return True
        
    except Exception as e:
        print(f"❌ Progress tracking error: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    print("\n🔥 FIREBASE & FIRESTORE TEST SUITE\n")
    
    # Test 1: Firestore Connection
    firestore_ok = test_firestore_connection()
    
    # Test 2: Progress Tracking (only if Firestore works)
    if firestore_ok:
        progress_ok = test_progress_tracking()
    else:
        progress_ok = False
        print("\n⚠️  Skipping progress tracking test (Firestore connection failed)")
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    print(f"Firestore Connection: {'✅ PASS' if firestore_ok else '❌ FAIL'}")
    print(f"Progress Tracking:    {'✅ PASS' if progress_ok else '❌ FAIL'}")
    print("=" * 60)
    
    if firestore_ok and progress_ok:
        print("\n🎉 All tests passed! Your progress tracking system is ready to use.")
        print("\nNext steps:")
        print("1. Log in to your app")
        print("2. Answer a question")
        print("3. Check Firebase Console to see the data")
    else:
        print("\n⚠️  Some tests failed. Please fix the issues above.")


if __name__ == "__main__":
    main()
