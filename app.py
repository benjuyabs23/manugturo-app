import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(page_title="MANUGTURO AI", page_icon="📝", layout="centered")

# Configure the Free Gemini API
# --- IMPORTANT: Paste your copied Gemini API key between the quotes below ---
GEMINI_API_KEY = "PASTE_YOUR_GEMINI_API_KEY_HERE"
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

st.title("📝 MANUGTURO: ILAW Lesson Plan Generator")
st.subheader("Master Teacher's AI Assistant (100% Free Edition)")
st.write("Aligned with DepEd Order No. 9, s. 2026 & DepEd Order No. 3, s. 2026")

# Input Section
st.markdown("### 🔍 Curriculum & Learner Context Input")
subject = st.text_input("Subject / Learning Area", placeholder="e.g., Science 10, Mathematics 7")
topic = st.text_input("Topic / Lesson Title", placeholder="e.g., Atomic Structure, Linear Equations")

col1, col2 = st.columns(2)
with col1:
    grade = st.selectbox("Grade Level", ["Grade 1", "Grade 2", "Grade 3", "Grade 4", "Grade 5", "Grade 6", "Grade 7", "Grade 8", "Grade 9", "Grade 10", "Grade 11", "Grade 12"])
with col2:
    term = st.selectbox("Academic Term Alignment", ["Term 1 (Opening Block)", "Term 2 (Mid-Year Block)", "Term 3 (Closing Block)"])

competency = st.text_area("Learning Competency", placeholder="Paste the specific DepEd curriculum competency here...")

# Generate Button
if st.button("Generate ILAW Lesson Plan", type="primary"):
    if subject and topic and competency:
        if GEMINI_API_KEY == "PASTE_YOUR_GEMINI_API_KEY_HERE":
            st.error("⚠️ Please replace 'PASTE_YOUR_GEMINI_API_KEY_HERE' in the code with your actual Google AI Studio API Key!")
        else:
            with st.spinner("Manugturo is designing your ILAW lesson plan journey..."):
                
                # Full Master-Teacher ILAW Prompt Structure
                ilaw_prompt = f"""
                You are an expert Instructional Coach and Master Teacher for the Philippine Department of Education. 
                Generate a highly detailed and pedagogically sound Lesson Plan using the ILAW Framework, adhering strictly to DO 9, s. 2026 (Three-Term Pacing) and DO 3, s. 2026 (Ethical AI Use).
                
                Metadata Context:
                - Subject: {subject}
                - Topic: {topic}
                - Grade Level: {grade}
                - Target Academic Term: {term}
                - Learning Competency: {competency}
                
                Structure the output strictly into these four pillars with clean Markdown headers:
                
                ### I. INTENTIONS (I)
                - **Learning Objectives:** Break down the competency into 2-3 specific targets (Knowledge, Skills, and Attitudes).
                - **Learner Context:** Formulate a realistic learner profile detailing visual-spatial or auditory preferences, and identify explicit barriers to learning (e.g., technical connectivity, learning disabilities, motor difficulties) that require FLP (Flexible Learning Program) tagging.
                
                ### II. LEARNING EXPERIENCE (L)
                - **Pre-Lesson Well-being Check:** Detail a trauma-informed socio-emotional check-in activity using the Hinga (Check-in) and Hinto (Emergency Stop) protocol standards.
                - **The Flow (Scaffolded Journey):** Provide a chronological, actionable sequence of classroom interactions. Ensure it follows learning design principles: explicitly making goals clear, heavy scaffolding (modeling before solo execution), mastery tracking, and cross-subject integration.
                - **Resources & Inclusive Alternatives:** Provide resource lists alongside an Emergency Alternative option (e.g., if internet/power fails, use specific localized materials).
                
                ### III. ASSESSMENT (A)
                - **Formative Assessment Strategies:** Design 2 distinct formative evaluation tasks checking understanding during delivery.
                - **Accommodations for Equity:** List variations of the assessment task to cater to learners with unique sensory or cognitive contexts.
                - **Learner AI Use Category:** For each assessment task, explicitly assign and label one mandatory classification per DO 3, s. 2026: [Prohibited], [Limited], or [Extensive] along with a brief academic integrity rule.
                
                ### IV. WAYS FORWARD (W)
                - **Extended Learning & Curiosity:** Propose a low-resource homework or exploration task to reinforce mastery at home.
                - **Instructional Coaching & Reflection Questions:** Formulate 2 reflective metrics for the teacher to gauge execution success and notes for their next school LAC session.
                
                ### DECLARATION OF AI USE
                End the document with this exact declaration statement: "This instruction-ready design was structured and pedagogically enhanced using MANUGTURO AI to guarantee standard alignment under DO 3 s. 2026 guidelines."
                """
                
                try:
                    response = model.generate_content(ilaw_prompt)
                    st.success("✨ Lesson Plan Ready!")
                    st.markdown("---")
                    st.markdown(response.text)
                    
                    # Make it downloadable as a text file
                    st.download_button("📥 Download Lesson Plan (.txt)", data=response.text, file_name=f"ILAW_{topic.replace(' ', '_')}.txt", mime="text/plain")
                except Exception as e:
                    st.error(f"AI Connection Error: {e}")
    else:
        st.warning("Please fill out all the input fields before asking Manugturo to compile.")
