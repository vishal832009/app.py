import streamlit as st
import google.generativeai as genai

st.title("Gemini 1.5 Flash AI App")

# 1. API Key Setup
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    
    # 2. Model Initialization
    try:
        # 'models/' lagane se 404 error nahi aayega
        model = genai.GenerativeModel('models/gemini-1.5-flash')
        
        user_input = st.text_input("Mujhse kuch puchiye:", placeholder="Type here...")
        
        if st.button("Puchiye"):
            if user_input:
                response = model.generate_content(user_input)
                st.success(response.text)
            else:
                st.warning("Pehle kuch sawaal toh likhiye!")
                
    except Exception as error_message:
        # Yahan humne 'e' ki jagah 'error_message' use kiya hai taaki confusion na ho
        st.error(f"Google API Error: {error_message}")
else:
    st.error("Secrets mein GOOGLE_API_KEY nahi mili. Please Streamlit Dashboard check karein.")
            
