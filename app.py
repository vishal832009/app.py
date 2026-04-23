import streamlit as st
import google.generativeai as genai

# Page Title
st.set_page_config(page_title="My AI App")
st.title("Gemini 1.5 Flash AI")

# Secret key access
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    user_input = st.text_input("Mujhse kuch puchiye:")
    
    if st.button("Submit"):
        if user_input:
            response = model.generate_content(user_input)
            st.write(response.text)
        else:
            st.warning("Pehle kuch likhiye!")

except Exception as e:
    st.error(f"Error: {e}")
    st.info("Check karein ki aapne Streamlit Secrets mein GOOGLE_API_KEY daali hai ya nahi.")
            
