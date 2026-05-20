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

# Secure API Configuration using Streamlit Secrets
try:
    GEMINI_API_KEY = st.secrets["GEMINI_KEY"]
    genai.configure(api_key=GEMINI_API_KEY)
    # Using the updated, working free-tier flash model
    model = genai.GenerativeModel('gemini-1.5-flash')
    secrets_configured = True
except Exception as e:
    secrets_configured = False

# SIDE-BY-SIDE LAYOUT (1/3 Width Inputs, 2/3 Width Document View)
col_input, col_output = st.columns([1, 2])

# LEFT PANEL: INPUT DETAILS
with col_input:
    st.markdown("### **INPUT DETAILS**")
    
    grade = st.selectbox("1. Select Grade Level: *", ["Grade 1", "Grade 2", "Grade 3", "Grade 4", "Grade 5", "Grade 6", "Grade 7", "Grade 8", "Grade 9", "Grade 10", "Grade 11", "Grade 12"])
    subject = st.text_input("2. Enter Subject Area: *", placeholder="e.g., Mathematics or Science")
    topic = st.text_input("3. Topic: *", placeholder="Specify your Topic and Objectives here")
    criteria = st.text_area("4. Additional Criteria / Instructions:", placeholder="You can specify additional criteria or specific instructions here (e.g., Student & Teacher Activity setup)...")
    
    # Your exact 4 Dropdown items from your colTemplates collection
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
        if not secrets_configured:
            st.error("⚠️ Setup Error: 'GEMINI_KEY' is missing from your Streamlit App Advanced Settings Dashboard Secrets box!")
        elif subject and topic:
            with st.spinner("Manugturo is processing your selected template guidelines..."):
                
                # --- DYNAMIC RULES CONTEXT INJECTION FROM YOUR COLTEMPLATES ---
                if template_choice == "1-Session ILAW Framework (D.O. 9 s. 2026)":
                    template_rules = """
                    Your task is to generate a highly professional and effective Lesson Plan using the ILAW Framework, following the DepEd Order 9, series of 2026 trimester guidelines and adhere to the Intentions, Learning Experience, Assessment and Ways Forward (ILAW) Framework and its Learning Design Principles (Clear Goals and Teaching, Active Retrieval and Spacing, Self-awareness and Metacognition, Scaffolding, Purpose & Values Integration, Inclusion, Checks for Understanding, and Social Learning).  
                    
                    Structure the output according to these four pillars (display this four pillars on the output):
                    
                    ### 1. INTENTIONS
                    * Learning Competency and Curriculum Standards: Write the competency/ies from the curriculum guide that we are targeting, and the content or performance standards applicable to the sessions.
                    * Learning Objectives: Provide specific objectives for Cognitive, Psychomotor, and Affective domains.
                    * Learner Context: Describe a realistic classroom context including common learner strengths, interests, and potential barriers to learning (e.g., visual impairments, fine motor difficulties, or varying reading levels).
                    
                    ### 2. LEARNING EXPERIENCE
                    * Pre-Lesson: Describe a (get ready) activity that checks well-being and hooks interest.
                    * Flow: Design a (journey) of activities that purposefully apply the Learning Design Principles: Make objectives clear to learners, provide scaffolding (guide them before letting them try alone), check mastery/understanding/well-being, connect concepts to past competencies, and encourage collaboration/reflection.
                    * Learning Resources: List inclusive resources and provide (Emergency Alternatives) (e.g., If no internet, use printed diagrams).
                    * Opportunities for Integration: Suggest a meaningful connection to another subject or technology.
                    
                    ### 3. ASSESSMENT
                    * Formative Assessment: Design 2-3 tasks or questions to gather feedback during the lesson.
                    * Accommodations: Provide specific ways (visual, auditory, or group-based) for learners with different abilities to demonstrate their understanding.
                    
                    ### 4. WAYS FORWARD
                    * Extended Learning: Suggest an activity learners can do at home to spark curiosity or reinforce mastery.
                    * Reflections: Provide 2 reflective questions for the teacher to ponder after the session.
                    
                    ### 5. DECLARATION OF AI USE
                    * Include a statement citing how AI was used in the formulation of this plan.
                    
                    Use an HTML <table> with borders for all grids and matrixes where numerical or structured tracking content applies.
                    """
                    
                elif template_choice == "4-Sessions ILAW Framework (D.O. 9 s. 2026)":
                    template_rules = """
                    Your task is to generate a highly professional and effective 4-session Lesson Plan using the ILAW Framework, following the DepEd Order 9, series of 2026 trimester guidelines and adhere to the Intentions, Learning Experience, Assessment and Ways Forward (ILAW) Framework and its Learning Design Principles.  
                    
                    Structure the output according to these four pillars (display this four pillars on the output):
                    
                    ### 1. INTENTIONS
                    * Learning Competency and Curriculum Standards: Write the competency/ies from the curriculum guide targeting the session block.
                    * Learning Objectives: (START 4-Session Grid, ROWS = Cognitive, Psychomotor, and Affective, COLUMNS = Session Number): Provide specific objectives across 4-sessions using an HTML table.
                    * Learner Context: (START 4-Session Grid, COLUMNS = Session Number): Describe realistic classroom contexts and barriers across 4-sessions using an HTML table.
                    
                    ### 2. LEARNING EXPERIENCE
                    (START 4-Session Grid, COLUMNS = Session Number inside an HTML table layout for all below fields):
                    * Pre-Lesson: Describe a (get ready) activity that checks well-being and hooks interest across 4-sessions.
                    * Flow: Design a (journey) of activities that purposefully apply the Learning Design Principles across 4-sessions.
                    * Learning Resources: List inclusive resources and provide (Emergency Alternatives) across 4-sessions.
                    * Opportunities for Integration: Suggest meaningful connections across 4-sessions.
                    
                    ### 3. ASSESSMENT
                    (START 4-Session Grid, COLUMNS = Session Number inside an HTML table):
                    * Formative Assessment: Design 2-3 tasks or questions to gather feedback across 4-sessions.
                    * Accommodations: Provide specific ways for unique abilities across 4-sessions.
                    
                    ### 4. WAYS FORWARD
                    (START 4-Session Grid, COLUMNS = Session Number inside an HTML table):
                    * Extended Learning: Suggest an activity learners can do at home across 4-sessions.
                    * Reflections: Provide 2 reflective questions across 4-sessions.
                    
                    ### 5. DECLARATION OF AI USE
                    * Include a statement citing how AI was used in the formulation of this plan.
                    
                    Use an HTML <table> with borders for all grids to organize Session 1, Session 2, Session 3, and Session 4.
                    """
                    
                elif template_choice == "4A's Format":
                    template_rules = """
                    Create a detailed, learner-centered, and classroom-ready 4A's lesson plan following the 4A's instructional model: Activity, Analysis, Abstraction, Application.
                    
                    Include the following components:
                    1. Objectives: Cognitive, Affective, and Psychomotor objectives.
                    2. Subject Matter: Topic, References, Materials/Visual Aids, Subject Integrations.
                    3. Procedure Proper (4A's) - Write full suggested teacher scripts and expected student responses:
                       - A. Activity: Motivational/review activity and collaborative student task.
                       - B. Analysis: Processing questions, guided discussion, critical-thinking inquiries.
                       - C. Abstraction: Generalization of the lesson, key concepts, simplified definitions.
                       - D. Application: Real-life application activity, group work, or situational tasks.
                    4. Differentiated Instructions and Activities: Provide separate clear blocks for: Advanced/Fast Learners (Enrichment), Average Learners (Guided practice), Struggling Learners (Scaffolded tasks), and Special Educational Needs (Modified activities, peer supports). Differentiate based on content, process, product, pacing, and grouping.
                    5. Assessment: Formative test, performance evaluation, or exit ticket with rubrics.
                    6. Assignment/Homework.
                    """
                    
                elif template_choice == "5E's Format":
                    template_rules = """
                    Create a detailed, learner-centered, and classroom-ready 5E's lesson plan following the 5E Instructional Model: Engage, Explore, Explain, Elaborate, Evaluate.
                    
                    Include: Learning Competencies/Objectives, Content Standards, Performance Standards, MELCs, Subject/Values Integration, Materials, ICT Integration, and Classroom Management Strategies.
                    
                    For each phase of the 5E model, explicitly map out details for:
                    - Teacher's Activities & Scripts
                    - Learners' Activities & Expected Responses
                    - Guide Questions & Time Allotments
                    
                    Add differentiated instruction strategies for Fast, Average, Struggling, and LSEN learners. In the Evaluate section, display formal formative tasks, rubrics, performance tasks, and reflection elements.
                    """
                
                # Consolidation prompt mapping engine
                master_prompt = f"""
                SYSTEM SETTING: You are an expert Master Teacher and Curriculum Evaluator for the Department of Education (DepEd) in the Philippines.
                Generate a ready-to-use, print-compliant lesson plan matching the following metadata inputs.
                
                METADATA DETAILS:
                - Target Grade: {grade}
                - Content Domain / Subject Area: {subject}
                - Lesson Focus Title: {topic}
                - Extra Teacher Request criteria: {criteria}
                
                SPECIFIC TEMPLATE CONFIGURATION PROMPT TO FOLLOW:
                {template_rules}
                
                Generate high-quality output. If HTML tables are requested, output clear raw tables that parse smoothly into markup views.
                """
                
                try:
                    response = model.generate_content(master_prompt)
                    st.success(f"✨ Finalized {template_choice} Draft Generated!")
                    st.markdown("---")
                    
                    # Renders output onto paper canvas container safely
                    st.markdown(response.text, unsafe_allow_html=True)
                    
                    st.markdown("---")
                    st.download_button(
                        label="📥 Download Clean Lesson Plan Document (.txt)",
                        data=response.text,
                        file_name=f"{template_choice.replace(' ', '_')}_{topic.replace(' ', '_')}.txt",
                        mime="text/plain",
                        use_container_width=True
                    )
                except Exception as e:
                    st.error(f"AI System Processing Exception Error: {e}")
        else:
            st.error("⚠️ Form Validation: Please fill out both the Subject Area and Topic fields to activate.")
else:
    st.info("💡 Complete input setup details inside the left configuration card container and click 'Generate Lesson Plan' to render your master curriculum draft sheet layout here.")
