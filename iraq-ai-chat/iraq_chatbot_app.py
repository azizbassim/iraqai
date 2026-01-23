import json
import random

# Load model
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

def chat(user_input):
    words = user_input.split()
    matches = {}
    
    for word in words:
        if word in knowledge_base:
            category = knowledge_base[word]
            matches[category] = matches.get(category, 0) + 1
    
    category = max(matches, key=matches.get) if matches else 'unknown'
    response = random.choice(responses.get(category, responses['unknown']))
    
    return response, category

print("=" * 70)
print("🇮🇶 IRAQ AI CHATBOT - نموذج الذكاء الاصطناعي العراقي")
print("=" * 70)
print("\nاكتب رسالتك (Type in Arabic) | اكتب 'خروج' للخروج\n")

while True:
    try:
        user_input = input("👤 You: ").strip()
        
        if not user_input:
            continue
        
        if user_input.lower() in ['exit', 'quit', 'خروج']:
            print("\n🤖 شكراً لك! وداعاً!")
            break
        
        response, category = chat(user_input)
        print(f"🤖 Bot: {response}")
        print(f"   [Category: {category}]\n")
        
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        break
    except Exception as e:
        print(f"Error: {e}")
