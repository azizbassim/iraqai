import json
import random
import os
import requests
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")  # ✅ Token hidden here

app = Flask(__name__, template_folder='.')

# ========== Your existing local model ==========
try:
    with open('iraq_ai_model_v2.json', 'r', encoding='utf-8') as f:
        model_data = json.load(f)
    knowledge_base = model_data['knowledge_base']
except:
    knowledge_base = {
        'مرحبا': 'greeting',
        'عراق': 'location',
        'نموذج': 'ai',
        'شكراً': 'thanks'
    }

responses = {
    'greeting': ['مرحبا! كيف حالك؟', 'أهلا وسهلا!', 'سعيد بلقائك!'],
    'location': ['العراق بلد جميل', 'بغداد عاصمة العراق', 'الجغرافيا العراقية غنية'],
    'question': ['هذا سؤال ذكي!', 'أستطيع مساعدتك', 'دعني أفكر'],
    'thanks': ['من دواعي سروري!', 'شكراً لك!', 'يسعدني خدمتك'],
    'ai': ['نعم، أنا نموذج ذكاء اصطناعي', 'تم تطويري للعراق', 'أنا هنا لمساعدتك'],
    'unknown': ['أعتذر، لم أفهم جيداً', 'هل يمكنك إعادة الصياغة؟', 'لا أملك معلومات عن هذا']
}

def local_chat(user_input):
    words = user_input.split()
    matches = {}
    
    for word in words:
        if word in knowledge_base:
            category = knowledge_base[word]
            matches[category] = matches.get(category, 0) + 1
    
    category = max(matches, key=matches.get) if matches else 'unknown'
    response = random.choice(responses.get(category, responses['unknown']))
    
    return response, category

# ========== Web Routes ==========

@app.route('/')
def home():
    return render_template('index.html')  # Serves your HTML

# ========== API Route (Token stays hidden!) ==========

@app.route('/api/chat', methods=['POST'])
def api_chat():
    user_message = request.json.get('message')
    
    # Call external LLM API with hidden token
    # Change this URL based on your LLM provider
    response = requests.post(
        'https://api.openai.com/v1/chat/completions',  # or your LLM URL
        headers={
            'Authorization': f'Bearer {API_TOKEN}',  # ✅ Secure!
            'Content-Type': 'application/json'
        },
        json={
            'model': 'gpt-4',
            'messages': [{'role': 'user', 'content': user_message}]
        }
    )
    
    return jsonify(response.json())

# ========== Run Server ==========

if __name__ == '__main__':
    print("=" * 70)
    print("🇮🇶 IRAQ AI CHATBOT - Server Running")
    print("=" * 70)
    print("\nOpen http://localhost:5000 in your browser\n")
    app.run(debug=True, port=5000)
