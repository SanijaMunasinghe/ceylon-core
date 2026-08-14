import os  
import google.generativeai as genai  
api_key = os.environ.get("GEMINI_API_KEY") or input("Enter Gemini API Key: ")  
genai.configure(api_key=api_key)  
model = genai.GenerativeModel("gemini-3.5-flash")  
print("Agent Ready! Type 'exit' to quit.")  
while True:  
    q = input("\nYou: ")  
    if q.lower() == 'exit': break  
    print(f"\nAgent: {model.generate_content(q).text}") 
