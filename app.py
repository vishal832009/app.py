import streamlit as st
import google.generativeai as genai
import os

st.title("Gemini 1.5 Flash AI (Stable)")

# API Key check
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
    
    # Forceful Configuration
    genai.configure(api_key=api_key)
    
    try:
        # Model initialization - yahan 'models/' prefix hata kar simple rakha hai
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        user_input = st.text_input("Sawaal puchiye:", key="input")
        
        if st.button("Generate Response"):
            if user_input:
                # Direct call without extra options to avoid NameErrors
                response = model.generate_content(user_input)
                
                if response.text:
                    st.success("AI ka Jawab:")
                    st.write(response.text)
                else:
                    st.warning("AI ne koi jawab nahi diya. Dubara try karein.")
            else:
                st.warning("Kuch likhiye!")
                
    except Exception as e:
        # Pura error dikhane ke liye
        st.error(f"Error Detail: {e}")
        st.info("Tip: Agar 404 aa raha hai, toh requirements.txt ko update karke Reboot karein.")
else:
    st.error("Secrets mein API Key nahi mili!")
