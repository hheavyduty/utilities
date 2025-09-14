from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

def open_website_incognito(url):
    """
    Open a website in incognito mode using Chrome
    """
    # Set up Chrome options for incognito mode
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--start-fullscreen")
    
    # Create the driver with incognito options
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        # Navigate to the website
        driver.get(url)
        print(f"Opened {url} in incognito mode")
        
        # Press 'M' key
        driver.find_element("tag name", "body").send_keys("M")
        print("Pressed 'M' key")
        
        # Keep the browser open for a few seconds to see the result
        time.sleep(300)
        
    except Exception as e:
        print(f"Error opening website: {e}")
    
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    # Example usage
    website_url = "https://www.sonyliv.com/live-sport/title-1790006570/cricket-asia-cup-2025-1090489077?watch=true"  # Change this to your desired website
    try:
        while True:
            open_website_incognito(website_url)
            if time.strftime("%H:%M:%S") == "23:00:00":
                break
    except KeyboardInterrupt:
        print("\nProgram stopped by user (Ctrl+C)")