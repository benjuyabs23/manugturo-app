import streamlit as st
import google.generativeai as genai

# Page Configuration to Wide Layout to mimic your Canvas design
st.set_page_config(page_title="MANUGTURO AI", page_icon="📝", layout="wide")

# Custom CSS injected to replicate the chalkboard & paper layout perfectly
st.markdown("""
    <style>
    .stApp { background-color: #1a261f; }
    [data-testid="stColumn"]:nth-of-type(1) {
        background-color: #e8e4db;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 3px 3px 10px rgba(0,0,0,0.3);
    }
    [data-testid="stColumn"]:nth-of-type(2) {
        background-color: #fdfbf7;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.4);
        min-height: 500px;
        border: 1px solid #e0dad0;
    }
    h1, h5 { color: #ffffff !important; font-family: 'Helvetica Neue', sans-serif; }
    h3 { color: #1a261f !important; font-family: 'Helvetica Neue', sans-serif; }
    div[data-testid="stMarkdownContainer"] p { color: #2b2b2b; font-weight: 500; }
    </style>
""", unsafe_allow_html=True)

# App Headers
st.title("MANUGTURO Lesson Planner")
st.markdown("##### *Click. Generate. Teach. Custom lessons made easy for FREE...! Developed for DepEd Teachers*")
st.markdown("---")

# Configure the Free Gemini API
# --- REMEMBER TO CHANGE THIS KEY ---
GEMINI_API_KEY = "AIzaSyCf9waQjr7PlIB5XgNrfBVbxskEIxE8s1I"
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# SIDE-BY-SIDE LAYOUT (1/3 Width Inputs, 2/3 Width Document View)
col_input, col_output = st.columns([1, 2])

# LEFT PANEL: INPUT DETAILS
with col_input:
    st.markdown("### **INPUT DETAILS**")
    
    grade = st.selectbox("1. Select Grade Level: *", ["Grade 1", "Grade 2", "Grade 3", "Grade 4", "Grade 5", "Grade 6", "Grade 7", "Grade 8", "Grade 9", "Grade 10", "Grade 11", "Grade 12"])
    subject = st.text_input("2. Enter Subject Area: *", placeholder="e.g., Mathematics or Science")
    topic = st.text_input("3. Topic: *", placeholder="Specify your Topic and Objectives here")
    criteria = st.text_area("4. Additional Criteria / Instructions:", placeholder="You can specify additional criteria or specific instructions here (e.g., Student & Teacher Activity setup)...")
    
    # Matching your exact 4 Dropdown items from colTemplates
    template_choice = st.selectbox(
        "5. Lesson Plan Template: *", 
        [
            "1-Session ILAW Framework (D.O. 9 s. 2026)", 
            "4-Sessions ILAW Framework (D.O. 9 s. 2026)", 
            "4A's Format", 
            "5E's Format"
        ]
    )
    
    generate_clicked = st.button("Generate Lesson Plan", type="primary", use_container_width=True)

# RIGHT PANEL: GENERATOR ENGINE
with col_output:
    if generate_clicked:
        if subject and topic:
            if GEMINI_API_KEY == "AIzaSyCf9waQjr7PlIB5XgNrfBVbxskEIxE8s1I":
                st.error("⚠️ Please replace 'AIzaSyCf9waQjr7PlIB5XgNrfBVbxskEIxE8s1I' in the code with your actual Google AI Studio API Key!")
            else:
                with st.spinner("Manugturo is processing your selected template guidelines..."):
                    
                    # --- DYNAMIC RULES CONTEXT INJECTION ---
                    if template_choice == "1-Session ILAW Framework (D.O. 9 s. 2026)":
                        template_rules = """
                        
                        Your task is to generate a highly professional and effective Lesson Plan using the ILAW Framework, following the DepEd Order 9, series of 2026 trimester guidelines and adhere to the Intentions, Learning Experience, Assessment and Ways Forward (ILAW) Framework and its Learning Design Principles (Clear Goals and Teaching, Active Retrieval and Spacing, Self-awareness and Metacognition, Scaffolding, Purpose & Values Integration, Inclusion, Checks for Understanding, and Social Learning).  
                        
                        Structure the output according to these four pillars (display these four pillars on the output):
                        - 1. INTENTIONS: Learning Competency and Curriculum Standards, Learning Objectives (Cognitive, Psychomotor, Affective), Learner Context (strengths, interests, barriers like visual impairments, fine motor difficulties, reading levels).
                        - 2. LEARNING EXPERIENCE: Pre-lesson well-being activity, Flow (applying Clear goals, Scaffolding, Mastery tracking, Connection to past competencies, Collaboration/Reflection), Learning Resources (with explicit Emergency Alternatives), Opportunities for Integration.
                        - 3. ASSESSMENT: Formative Assessment (2-3 tasks), Accommodations (visual, auditory, or group-based variations for equity).
                        - 4. WAYS FORWARD: Extended Learning (home activity), Reflections (2 questions for the teacher).
                        - 5. DECLARATION OF AI USE: Include a statement citing how AI was used in the formulation of this plan.
                        
                        CRITICAL: Use an HTML <table> with borders for all grids and matrixes where data is structured.
                        """
                        
                    elif template_choice == "4-Sessions ILAW Framework (D.O. 9 s. 2026)":
                        template_rules = """
                        Your task is to generate a highly professional and effective 4-session Lesson Plan using the ILAW Framework, following the DepEd Order 9, series of 2026 trimester guidelines and adhere to the Intentions, Learning Experience, Assessment and Ways Forward (ILAW) Framework and its Learning Design Principles.  
                        
                        Structure the output according to these four pillars across a 4-Session Matrix:
                        - 1. INTENTIONS: Competency/Curriculum Standards. Learning Objectives (Create a 4-Session HTML Grid Table: Rows = Cognitive, Psychomotor, Affective; Columns = Session 1-4). Learner Context (Create a 4-Session Grid Table: Columns = Session 1-4 describing classroom barriers).
                        - 2. LEARNING EXPERIENCE: Create a 4-Session HTML Grid Table with Columns = Session 1-4 containing Pre-Lesson tasks, Scaffolded Flow, Inclusive Resources (with Emergency Alternatives), and Integrations.
                        - 3. ASSESSMENT: Create a 4-Session HTML Grid Table with Columns = Session 1-4 containing Formative Assessment tasks and Accommodations.
                        - 4. WAYS FORWARD: Create a 4-Session HTML Grid Table with Columns = Session 1-4 containing Extended Learning and 2 Teacher Reflections.
                        - 5. DECLARATION OF AI USE: Include a statement citing how AI was used in the formulation of this plan.
                        
                        CRITICAL: Use beautifully styled, bordered HTML <table> grids to separate Session 1, Session 2, Session 3, and Session 4 contents for every section as requested.
                        """
                        
                    elif template_choice == "4A's Format":
                        template_rules = """
                        Create a detailed, learner-centered, and classroom-ready 4A's lesson plan following the 4A's instructional model: Activity, Analysis, Abstraction, Application.
                        Include:
                        1. Objectives (Cognitive, Affective, Psychomotor)
                        2. Subject Matter (Topic, References, Materials/Visual Aids, Subject Integrations)
                        3. Procedure Proper (Teacher Script and Expected Learner Responses for each):
                           - A. Activity: Motivational/interactive task
                           - B. Analysis: Processing/Critical-thinking questions
                           - C. Abstraction: Generalization and key concepts summarized
                           - D. Application: Real-life application activity or situational group work
                        4. Differentiated Instructions and Activities: Explicitly separate strategies for Advanced/Fast Learners (Enrichment), Average Learners (Guided practice), Struggling Learners (Scaffolded support), and Learners with Special Educational Needs (Modified activities, visual supports, peer buddy). Differentiate based on content, process, product, pacing, and grouping.
                        5. Assessment: Formative task, performance task, or exit ticket with a rubric/scoring guide.
                        6. Assignment/Homework connected to the lesson.
                        Ensure suggested teacher scripts and potential student responses are embedded throughout.
                        """
                        
                    elif template_choice == "5E's Format":
                        template_rules = """
                        Create a detailed, learner-centered, and classroom-ready 5E's lesson plan following the 5E Instructional Model: Engage, Explore, Explain, Elaborate, Evaluate.
                        Include: Learning Competencies/Objectives, Content Standards, Performance Standards, MELCs (if applicable), Subject/Values Integration, Materials, ICT Integration, and Classroom Management Strategies.
                        
                        For each phase (Engage, Explore, Explain, Elaborate, Evaluate), provide an structured breakdown displaying:
                        - Teacher's Activities
                        - Learners' Activities
                        - Guide Questions & Expected Responses
                        - Time Allotment
                        
                        Add differentiated instruction targets for Fast, Average, Struggling, and Special Educational Needs learners. Include formative assessments, performance tasks, and reflection rubrics in the Evaluate phase.
                        """
                    
                    # Consolidating user runtime metadata and targeted prompt rules
                    master_prompt = f"""
                    SYSTEM INSTRUCTION: You are a Master Teacher and Senior Curriculum Designer for the Department of Education (DepEd) in the Philippines. 
                    Generate an exceptional, ready-to-print lesson plan file matching the exact template layout rules provided.
                    
                    USER INPUT METADATA:
                    - Targeted Grade Level: {grade}
                    - Subject / Learning Area: {subject}
                    - Core Topic / Lesson Title: {topic}
                    - User Custom Instructions: {criteria}
                    
                    TEMPLATE RUNTIME RULES:
                    {template_rules}
                    
                    Ensure high pedagogical standards, age-appropriate language, and clear structural separation.
                    """
                    
                    try:
                        response = model.generate_content(master_prompt)
                        st.success(f"✨ Finalized {template_choice} Draft Rendered Successfully!")
                        st.markdown("---")
                        
                        # Displays the output inside the paper container
                        st.markdown(response.text, unsafe_allow_html=True)
                        
                        st.markdown("---")
                        st.download_button(
                            label="📥 Download Structured Lesson Plan (.txt)",
                            data=response.text,
                            file_name=f"{template_choice.replace(' ', '_')}_{topic.replace(' ', '_')}.txt",
                            mime="text/plain",
                            use_container_width=True
                        )
                    except Exception as e:
                        st.error(f"AI Generation Fault: {e}")
        else:
            st.error("⚠️ Validation Error: Please input both a Subject Area and Lesson Topic on the left configuration panel.")
    else:
        # Initial paper preview screen matching your design layout state
        st.info("💡 Input configuration details into the left panel container, select your structural framework blueprint, and click 'Generate Lesson Plan' to output the complete pedagogical matrix here.")
