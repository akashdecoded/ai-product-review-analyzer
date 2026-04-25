import requests
from bs4 import BeautifulSoup

# Step 1: Hum Flipkart ka ek link le rahe hain (Example ke liye iPhone)
url = "ENTER_ANY_PRODUCT_LINK_FROM_FLIPKART"

# Step 2: Bouncer se bachna! 
# Websites bots ko block kar deti hain. Yeh 'User-Agent' website ko 
# bewakoof banata hai ki hum script nahi, ek normal Google Chrome browser hain.
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

print("Flipkart par jaa rahe hain...")

try:
    # Step 3: Website ka pura HTML page download karna
    response = requests.get(url, headers=headers)
    
    # Step 4: HTML ko saaf karke padhne layak banana (Soup banana)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Step 5: Page ke andar se 'title' tag dhoondhna
    page_title = soup.find("title").text
    
    print("\n✅ Success! Page ka Title yeh mila:")
    print(page_title)

except Exception as e:
    print("\n❌ Scraping Error:", e)