import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Chatbot")
st.title("Gemini 1.5 Flash")

# API Key check
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)

    try:
        # Solution: Sirf 'gemini-1.5-flash' use karein, 'models/' prefix ke bina 
        # Ya phir 'gemini-pro' try karein agar ye fail ho
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        user_input = st.text_input("Sawaal puchiye:")

        if st.button("Submit"):
            if user_input:
                # generate_content default v1 version use karta hai
                response = model.generate_content(user_input)
                st.write(response.text)
            else:
                st.warning("Kuch likhiye...")

    except Exception as e:
        # Agar abhi bhi error aaye, toh ye dusra model try karega
        st.error(f"Pehla error: {e}")
        st.info("Alternative model 'gemini-pro' try kar raha hoon...")
        
        try:
            model_alt = genai.GenerativeModel('gemini-pro')
            res = model_alt.generate_content("Hello")
            st.success("Gemini-Pro kaam kar raha hai!")
        except Exception as e2:
            st.error(f"Dono models fail ho gaye: {e2}")
else:
    st.error("Secrets mein GOOGLE_API_KEY nahi mili!")
