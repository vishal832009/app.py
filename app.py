import streamlit as st
import google.generativeai as genai
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="AI Resume Coach", page_icon="📝")

# --- API SETUP ---
# Streamlit Secrets se API key lega (Deployment ke waqt kaam aayega)
api_key = st.sidebar.text_input("Apni Gemini API Key yahan dalein:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    st.title("🤖 AI Resume Coach")
    st.write("Main aapke raw experience ko professional bullet points mein badal dunga.")

    # --- INPUTS ---
    job_desc = st.text_area("Job Description (Jiske liye apply kar rahe hain):", placeholder="Copy-paste J.D. here...")
    user_exp = st.text_area("Apna Experience ya Skills likhein:", placeholder="e.g., Maine 2 saal sales mein kaam kiya aur target meet kiye...")

    if st.button("Resume Points Chamkayein! ✨"):
        if not job_desc or not user_exp:
            st.warning("Pehle dono fields fill kijiye!")
        else:
            with st.spinner("AI Coaching in progress..."):
                prompt = f"""
                You are a professional Career Coach and Resume Expert. 
                Based on the following Job Description: {job_desc}
                And the user's raw experience: {user_exp}
                
                Please provide:
                1. 5 High-impact, ATS-friendly bullet points using the 'Action Verb + Task + Result' formula.
                2. Suggestions for keywords to add.
                3. A brief 'Professional Summary' for the top of the resume.
                """
                response = model.generate_content(prompt)
                st.success("Tayyar hai! Neeche se copy karein:")
                st.markdown("---")
                st.write(response.text)
else:
    st.info("Sidebar mein apni Gemini API Key dalein shuru karne ke liye.")
