import streamlit as st
import google.generativeai as genai
from google.generativeai.types import RequestOptions

st.title("Gemini 1.5 Flash (Fixed Version)")

if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    
    try:
        # v1 version ko force karna taaki 404 na aaye
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        user_input = st.text_input("Sawaal puchiye:")
        
        if st.button("Submit"):
            if user_input:
                # Yahan hum 'v1' api version specify kar rahe hain
                response = model.generate_content(
                    user_input,
                    request_options=RequestOptions(api_version='v1')
                )
                st.success(response.text)
            else:
                st.warning("Kuch toh likhiye!")
                
    except Exception as e:
        st.error(f"Abhi bhi issue hai: {e}")
else:
    st.error("API Key missing in Secrets!")
