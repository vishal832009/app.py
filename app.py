# Model ko sahi version ke saath call karne ka tarika
try:
    # 'models/' prefix lagane se 404 error aksar theek ho jata hai
    model = genai.GenerativeModel(model_name='models/gemini-1.5-flash')
    
    # Test request
    response = model.generate_content("Hello")
    st.write(response.text)
except Exception as e:
    st.error(f"Error: {e}")
            
