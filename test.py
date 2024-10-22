# First check version of your chrome browser in settings> about chrome
# Download chrome web driver from https://developer.chrome.com/docs/chromedriver/downloads
# extract zip and store it in C:>program files 
# Create a test.py file and in terminal write  'pip install selenium'
# Copy the following code and run



from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Specify the path to the chromedriver.exe
chrome_driver_path = "C:/Program Files/chromedriver-win64/chromedriver.exe"  # Replace with your actual path

# Create a service object using the ChromeDriver path
service = Service(chrome_driver_path)

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=service)

# Navigate to the website
driver.get('https://google.com')

# Validate the title
expected_title = 'Google'  # Change this to the expected title
actual_title = driver.title

if expected_title == actual_title:
    print('Title validation successful!')
else:
    print('Title validation failed. Expected:', expected_title, 'Actual:', actual_title)

try:
    while True:
        pass  # This will keep the program running
except KeyboardInterrupt:
    print('Closing the browser...')

# Close the browser
driver.quit()
