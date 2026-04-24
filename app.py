import streamlit as st
import google.generativeai as genai

st.title("Gemini 1.5 Flash AI")

# Access the key from secrets
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    
    try:
        # Simple model name without 'models/' prefix
        model = genai.GenerativeModel('gemini-1.5-flash')
        user_input = st.text_input("Sawaal likhein:")
        
        if st.button("Generate"):
            if user_input:
                response = model.generate_content(user_input)
                st.write(response.text)
            else:
                st.info("Pehle kuch sawaal likhein.")
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.error("API Key nahi mili! Settings > Secrets check karein.")
