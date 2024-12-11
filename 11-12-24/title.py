from selenium import webdriver

# Initialize WebDriver
driver = webdriver.Chrome()

# Open a website
driver.get("https://www.google.com")

# Print the page title
print("Page Title:", driver.title)

# Close the browser
driver.quit()


