import requests
from bs4 import BeautifulSoup
from google import genai

# 1. APNA AI SETUP KARO (Apni API key dalo)
API_KEY = "ENTER_API_KEY"
client = genai.Client(api_key=API_KEY)

# 2. WEBSITE KA DATA NIKALNA
url = "ENTER_PRODUCT_LINK"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

print("🕵️‍♂️ Flipkart par jaa rahe hain aur data copy kar rahe hain...")

try:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Page ka saara text ek sath nikal rahe hain (HTML tags hata kar)
    # Shuru ke 6000 words le rahe hain jisme details aur reviews hote hain
    page_text = soup.get_text(separator=' ', strip=True)[:6000]
    
    print("✅ Data copy ho gaya! Ab AI se summary banwa rahe hain...\n")
    
    # 3. AI KO COMMAND DENA (PROMPT)
    ai_command = f"""
    Yeh ek Flipkart product page ka raw data hai: {page_text}
    
    Tumhara task yeh hai ki is kachre (raw text) mein se kaam ki baatein nikalo aur 
    mujhe Hinglish mein ek mast summary do. 
    
    Format aisa hona chahiye:
    - 📱 Product Ka Naam:
    - 💰 Price:
    - ⭐ Main Features (2-3 line mein):
    - 🗣️ Janta Kya Bol Rahi Hai (Reviews ka nichod):
    """
    
    # AI se jawab maangna
    ai_response = client.models.generate_content(
        model='gemini-3-flash-preview', # Hum stable aur fast model use kar rahe hain
        contents=ai_command,
    )
    
    print("✨ AI REVIEW SUMMARY ✨")
    print("-" * 30)
    print(ai_response.text)
    print("-" * 30)

except Exception as e:
    print("\n❌ Error aa gaya:", e)