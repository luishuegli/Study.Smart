# VWL-Brilliant Statistics Learning Platform

> **Interactive, Brilliant.org-style learning platform for Statistics (VWL)**

A web-based learning application built with **Streamlit** that teaches statistics through interactive visualizations, hands-on experiments, and AI-powered tutoring. Designed specifically for students in the VWL (Volkswirtschaftslehre) program.

---

## 📚 Table of Contents

- [Project Overview](#project-overview)
- [Current Status](#current-status)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Design Philosophy](#design-philosophy)
- [Module 1: Grundlagen der Wahrscheinlichkeit](#module-1-grundlagen-der-wahrscheinlichkeit)
- [Development Workflow](#development-workflow)
- [Firebase Integration Plan](#firebase-integration-plan)
- [Next Steps](#next-steps)
- [Setup & Installation](#setup--installation)

---

## 🎯 Project Overview

This platform transforms traditional statistics education by:

1. **Interactive Learning**: Every concept is immediately followed by hands-on experiments
2. **Visual Excellence**: Clean, modern UI inspired by Brilliant.org
3. **AI Tutoring**: Gemini 2.0 Flash provides contextual help for both theory and practice problems
4. **Exam Preparation**: Curated exam questions with step-by-step solutions
5. **Progress Tracking**: (Coming soon with Firebase) Track student progress across modules

### Learning Philosophy

**Theory → Experiment → Practice**

Each subsection follows this pattern:
- **Theory Card**: Concise explanation with examples
- **Interactive Experiment**: Immediate hands-on application
- **Practice Questions**: Test understanding with AI help available

---

## ✅ Current Status

### Completed ✓

**Infrastructure & Core Features:**
- ✅ Streamlit application with responsive layout
- ✅ Hierarchical navigation (Topics → Subtopics)
- ✅ AI integration with Gemini 2.0 Flash
- ✅ Exam question rendering with LaTeX support
- ✅ Answer validation and solution unveiling
- ✅ AI Q&A within solution expanders
- ✅ Custom CSS styling system

**Module 1.1 - Ereignisse, Ereignisraum und Ereignismenge:**
- ✅ **Complete** with three interactive experiments:
  1. **Elementarereignis**: Interactive dice roller
  2. **Ereignisraum**: Build the complete event space
  3. **Ereignis**: Select subsets (e.g., even numbers)
- ✅ White box design with gray borders
- ✅ Large icons (48px) with teal accents
- ✅ Theory-Experiment interleaved structure
- ✅ Consistent button styling (white with gray borders, purple when selected)

### In Progress 🚧

**Module 1.2-1.9**: Ready to implement
- Content generation workflow established
- Design system finalized
- Template ready for replication

### Planned 📋

- Firebase authentication & user management
- Progress tracking across modules
- Personalized learning paths
- Analytics dashboard
- Additional modules (1.2-1.9 and beyond)

---

## 🛠 Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Frontend** | Streamlit | Web application framework |
| **AI Model** | Google Gemini 2.0 Flash | Contextual tutoring & explanations |
| **Visualization** | Plotly | Interactive charts & graphs |
| **LaTeX** | st.latex() | Mathematical notation rendering |
| **Styling** | Custom CSS | Brilliant.org-inspired design |
| **Backend (Planned)** | Firebase | Authentication, database, hosting |
| **Environment** | Python 3.9+ | Runtime |

### Key Dependencies

```
streamlit
plotly
numpy
google-generativeai
python-dotenv
```

---

## 📁 Project Structure

```
statistics-learning-website/
├── app.py                          # Main Streamlit application
├── data.py                         # Course structure & metadata
├── exam_data.py                    # Exam questions database
├── course_config.py                # LaTeX notation config
├── .env                            # Environment variables (GEMINI_API_KEY)
│
├── views/
│   ├── dashboard.py                # Course overview page
│   ├── lesson.py                   # Individual lesson view
│   └── help.py                     # Help/tutorial page
│
├── topics/
│   └── topic_1_content.py          # Module 1 interactive content
│
├── Slides/                         # Original lecture slides (PDF → PNG)
│
└── README.md                       # This file
```

### Key Files Explained

**`app.py`**
- Entry point
- Configures Gemini AI model
- Handles page routing
- Initializes session state

**`data.py`**
- Defines course hierarchy (topics → subtopics)
- Maps subtopics to slide ranges
- Controls topic unlock status

**`exam_data.py`**
- Stores all exam questions
- Organized by topic and subtopic
- Includes questions, options, answers, and solutions

**`topics/topic_1_content.py`**
- Interactive content for Module 1 (Grundlagen der Wahrscheinlichkeit)
- Currently: Subtopic 1.1 implemented
- Template for 1.2-1.9

**`views/lesson.py`**
- Renders individual lessons
- Handles Q&A display
- Manages solution unveiling
- Integrates AI tutoring

---

## 🎨 Design Philosophy

### Visual Design Principles

1. **Clean & Minimal**: White backgrounds, gray borders, generous spacing
2. **Consistent**: All elements follow the same design language
3. **Interactive**: Buttons provide clear visual feedback
4. **Professional**: Inter font, Lucide icons, subtle shadows

### UI Components

**Theory Boxes** (`.theory-box`)
- White background
- 2px gray border (#e5e7eb)
- 56px icon in teal circle
- Clear header with bottom border

**Buttons**
- Default: White background, gray border
- Selected: Purple/indigo (#6366f1)
- Hover: Light gray background
- 20px border radius (rounded)

**Experiment Badges**
- Teal background (#ecfeff)
- Uppercase text
- Emoji + descriptive text

### Color Palette

| Color | Hex Code | Usage |
|-------|----------|-------|
| Teal (Primary) | `#14b8a6` | Icons, accents |
| Indigo (Selected) | `#6366f1` | Selected buttons |
| Gray Border | `#e5e7eb` | Borders, dividers |
| Dark Text | `#0f172a` | Headings |
| Body Text | `#475569` | Explanations |

---

## 📖 Module 1: Grundlagen der Wahrscheinlichkeit

**Current Status**: 1.1 Complete, 1.2-1.9 To Do

### Module Structure (9 Subsections)

| Subsection | Title | Status | Interactive Elements |
|------------|-------|--------|---------------------|
| **1.1** | Ereignisse, Ereignisraum und Ereignismenge | ✅ Complete | Dice roller, Event space builder, Subset selector |
| **1.2** | Wahrscheinlichkeit - Definition | 📋 To Do | TBD |
| **1.3** | Rechenregeln für Wahrscheinlichkeiten | 📋 To Do | TBD |
| **1.4** | Bedingte Wahrscheinlichkeit | 📋 To Do | TBD |
| **1.5** | Unabhängigkeit von Ereignissen | 📋 To Do | TBD |
| **1.6** | Totale Wahrscheinlichkeit | 📋 To Do | TBD |
| **1.7** | Satz von Bayes | 📋 To Do | TBD |
| **1.8** | Kombinatorik | 📋 To Do | TBD |
| **1.9** | Zufallsvariablen | 📋 To Do | TBD |

### 1.1 Details (Completed)

**Concepts Covered:**
1. **Elementarereignis (ω)**: The smallest, indivisible outcome
2. **Ereignisraum (S or Ω)**: The set of all possible outcomes
3. **Ereignis (A)**: A subset of the event space

**Interactive Experiments:**
1. **Dice Roller**: Experience a single elementary event
2. **Event Space Builder**: Click all dice faces to build S = {1,2,3,4,5,6}
3. **Subset Selector**: Select even numbers to define event A = {2,4,6}

**Design Pattern (Template for 1.2-1.9):**
```
Theory Box 1 → Experiment 1
Theory Box 2 → Experiment 2
Theory Box 3 → Experiment 3
Summary (optional)
Practice Questions + Solutions + AI Help
```

---

## 🔄 Development Workflow

### For Each New Subtopic (1.2, 1.3, etc.)

#### Phase 1: Content Planning
1. Review lecture slides for the subsection
2. Identify 2-3 core concepts
3. Design interactive experiments for each concept
4. Draft theory explanations (concise, example-driven)

#### Phase 2: Implementation
1. Add function to `topics/topic_1_content.py` (e.g., `render_subtopic_1_2()`)
2. Copy HTML/CSS structure from 1.1 (ensures consistency)
3. Implement theory boxes with:
   - Appropriate icon (from Lucide icons set)
   - Concise explanation
   - Clear example
   - Experiment badge
4. Build interactive experiments using Streamlit widgets
5. Add practice questions to `exam_data.py`

#### Phase 3: Integration
1. Update `views/lesson.py` to call new render function
2. Test interactive elements
3. Verify AI Q&A context is appropriate
4. Check visual consistency with 1.1

#### Phase 4: Verification
1. Load subtopic in browser
2. Test all interactive elements
3. Verify button styling (white → purple on selection)
4. Check mobile responsiveness
5. Test AI tutoring with sample questions

### AI Content Generation (Optional Accelerator)

Use the **Master Prompt** (stored in artifacts):
- Located at: `.gemini/antigravity/brain/.../gemini_content_gen_prompt.md`
- Generates Python code for new subtopics
- Includes theory, experiments, and exam questions
- **Human review required** before integration

---

## 🔥 Firebase Integration Plan

### Why Firebase?

- **Authentication**: User login/signup
- **Firestore Database**: Store user progress, scores, study time
- **Cloud Functions**: Backend logic (e.g., analytics)
- **Hosting**: Deploy the application
- **Analytics**: Track engagement metrics

### Data Model (Proposed)

```
users/
  {userId}/
    - email: string
    - displayName: string
    - createdAt: timestamp
    - progress/
        topic_1/
          - 1.1: {completed: bool, score: number, lastAttempt: timestamp}
          - 1.2: {completed: bool, score: number, lastAttempt: timestamp}
          ...
    - studyTime: {total: number, byTopic: {}}
    - preferences: {theme: string, notifications: bool}

questions/
  {questionId}/
    - topicId: string
    - subtopicId: string
    - question: string
    - options: array
    - correctAnswer: string
    - attempts: number
    - correctRate: number
```

### Integration Steps

#### Step 1: Firebase Setup
```bash
pip install firebase-admin
```

1. Create Firebase project at [console.firebase.google.com](https://console.firebase.google.com)
2. Enable Authentication (Email/Password)
3. Create Firestore database
4. Download service account key
5. Add to `.env`:
   ```
   FIREBASE_KEY_PATH=path/to/serviceAccountKey.json
   ```

#### Step 2: Authentication Flow
- Login/Signup page (new view)
- Session management with Streamlit session state
- Protected routes (redirect unauthenticated users)

#### Step 3: Progress Tracking
- Save question attempts (correct/incorrect)
- Update completion status per subtopic
- Calculate overall course progress

#### Step 4: Analytics Dashboard
- Study time by topic
- Accuracy rates
- Struggling areas (recommendations)
- Learning streak

### File Changes Required

1. **New file**: `firebase_config.py` - Initialize Firebase SDK
2. **New view**: `views/auth.py` - Login/signup UI
3. **Update**: `app.py` - Add authentication check
4. **Update**: `views/lesson.py` - Save progress on question submit
5. **New file**: `utils/db.py` - Database helper functions

---

## 🚀 Next Steps

### Immediate (This Sprint)

1. **Verify 1.1 is finalized**
   - [ ] Test all three experiments
   - [ ] Check on mobile viewport
   - [ ] Verify AI responses are contextual

2. **Implement 1.2: Wahrscheinlichkeit - Definition**
   - [ ] Review slides for 1.2
   - [ ] Design 2-3 interactive experiments
   - [ ] Write theory content
   - [ ] Add to `topic_1_content.py`

3. **Continue through 1.3-1.9**
   - Use 1.1 as the template
   - Maintain consistent design
   - Ensure each has unique, engaging experiments

### Short-term (Next 2 Weeks)

1. **Complete Module 1** (Subtopics 1.2-1.9)
2. **Firebase Setup**
   - Create Firebase project
   - Implement authentication
   - Design data schema
3. **Progress Tracking MVP**
   - Save completed subtopics
   - Display progress percentage

### Mid-term (1 Month)

1. **Module 2-5 Implementation**
2. **Analytics Dashboard**
3. **Mobile optimization**
4. **Performance improvements** (lazy loading, caching)

### Long-term (3 Months)

1. **Full course completion** (all VWL statistics topics)
2. **Gamification** (badges, streaks, leaderboards)
3. **Social features** (study groups, peer help)
4. **Deployment** to production (Firebase Hosting)

---

## 💻 Setup & Installation

### Prerequisites

- Python 3.9 or higher
- Google Gemini API key
- Terminal/Command Line access

### Installation

1. **Clone/Download the project**
   ```bash
   cd /path/to/statistics-learning-website
   ```

2. **Install dependencies**
   ```bash
   pip install streamlit plotly numpy google-generativeai python-dotenv
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run app.py --server.port 8501
   ```

5. **Access in browser**
   ```
   http://localhost:8501
   ```

### Firebase Setup (Future)

When ready to integrate Firebase:

1. Install Firebase Admin SDK:
   ```bash
   pip install firebase-admin
   ```

2. Get your service account key from Firebase Console

3. Add to `.env`:
   ```
   FIREBASE_KEY_PATH=./serviceAccountKey.json
   ```

---

## 📝 Contributing Guidelines

### Code Style

- Use **descriptive variable names** (e.g., `dice_result`, not `dr`)
- Add **comments** for complex logic
- Follow the established **design patterns** from 1.1
- Keep **functions focused** (single responsibility)

### Design Consistency

When adding new interactive elements:

1. Use `.theory-box` structure for theory content
2. Use `.experiment-badge` for experiment labels
3. Ensure buttons follow white/gray → purple pattern
4. Icons should be 48px, from Lucide icon set
5. Test on both desktop and mobile

### Testing Checklist

Before considering a subtopic "complete":

- [ ] All interactive elements work correctly
- [ ] Buttons are styled consistently (white default, purple selected)
- [ ] Theory boxes have proper borders and spacing
- [ ] Icons are visible and sized correctly (48px)
- [ ] Experiments provide clear feedback
- [ ] Practice questions load and validate correctly
- [ ] AI help is contextually relevant
- [ ] No console errors in browser DevTools

---

## 🤝 Support & Contact

For questions or issues:
- Review this README
- Check existing code in `topics/topic_1_content.py` for examples
- Refer to the artifact files for detailed prompts and workflows

---

## 📄 License

This project is for educational purposes.

---

## 🎯 Success Metrics

### For Each Subtopic

- ✅ 2-3 interactive experiments per subsection
- ✅ <500 words of theory text (stay concise)
- ✅ 3-5 practice questions with solutions
- ✅ AI-powered help available
- ✅ Visual consistency with 1.1

### For Module 1 Completion

- ✅ All 9 subtopics implemented
- ✅ Consistent design throughout
- ✅ All interactions tested
- ✅ Ready for Firebase integration

---

**Last Updated**: December 20, 2024  
**Version**: 1.1 (Module 1.1 Complete)  
**Next Milestone**: Module 1.2 Implementation
