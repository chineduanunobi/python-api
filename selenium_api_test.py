from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# Configure the Chrome WebDriver with options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # Run Chrome in headless mode
chrome_options.add_argument('--no-sandbox')  # Disable sandbox for headless mode
chrome_options.add_argument('--disable-dev-shm-usage')  # Disable /dev/shm usage for headless mode
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Load your ECS-hosted application's URL
ecs_app_url = "http://api-lb-819883266.us-east-1.elb.amazonaws.com"
driver.get(ecs_app_url)


# Add your assertion based on your application's behavior
# For example, checking for specific content in the page
assert "Wednesday" in driver.page_source

# Close the driver
driver.quit()
