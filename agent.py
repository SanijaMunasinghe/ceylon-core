import streamlit as st  
import os  
import google.generativeai as genai  
from duckduckgo_search import DDGS  
api_key = st.secrets.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")  
if api_key: genai.configure(api_key=api_key)  
model = genai.GenerativeModel("gemini-3.5-flash")  
st.set_page_config(page_title="Ceylon-Core AI", page_icon="????")  
st.title("???? Ceylon-Core Web Agent")  
if "messages" not in st.session_state: st.session_state.messages = []  
for msg in st.session_state.messages:  
    with st.chat_message(msg["role"]): st.markdown(msg["content"])  
if prompt := st.chat_input("Ask your agent..."):  
    st.session_state.messages.append({"role": "user", "content": prompt})  
    with st.chat_message("user"): st.markdown(prompt)  
    if any(w in prompt.lower() for w in ["search", "live", "news", "weather", "today"]):  
        try:  
            with DDGS() as ddgs:  
                results = [r['body'] for r in ddgs.text(prompt, max_results=3)]  
                prompt = f"Context:\n{chr(10).join(results)}\n\nQuestion: {prompt}"  
        except: pass  
    try:  
        res = model.generate_content(prompt).text  
        st.session_state.messages.append({"role": "assistant", "content": res})  
        with st.chat_message("assistant"): st.markdown(res)  
    except Exception as e: st.error(f"Error: {e}") 
