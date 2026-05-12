from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Launch Chrome browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open website
driver.get("https://www.google.com")

# Maximize window
driver.maximize_window()

# Print title
print("Website Title:", driver.title)

# Wait for 5 seconds
time.sleep(5)

# Close browser
driver.quit()

print("Test completed successfully!")