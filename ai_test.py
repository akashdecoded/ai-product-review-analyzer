'''
from google import genai

# Yahan apni asali API key daalo
API_KEY = "ENTER_YOUR_KEY"

client = genai.Client(api_key=API_KEY)

print("Aapki API key ke liye yeh models available hain:\n")

try:
    # API se saare available models ki list nikal rahe hain
    for model in client.models.list():
        print(model.name)
except Exception as e:
    print("Error:", e)
'''
from google import genai

# Yahan apni asli API key daalo
API_KEY = "YOUR_GOOGLE_API_KEY"

client = genai.Client(api_key=API_KEY)
question = "Python me web scraping kya hoti hai? Sirf ek line me batao."

print("Jawab dhoondh rahe hain...\n")

try:
    # Humne apna best model select kar liya hai: gemini-2.5-flash
    response = client.models.generate_content(
        model='gemini-3-flash-preview',
        contents=question,
    )
    print("✅ AI ka Jawab:")
    print(response.text)

except Exception as e:
    print("❌ Error:", e)