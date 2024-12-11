from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Setting up Selenium WebDriver
driver = webdriver.Chrome()

# Function to extract product details
def extract_product_details():
    products = []
    items = driver.find_elements(By.CLASS_NAME, '_75nlfW')
    for item in items:
        try:
            product_name = item.find_element(By.CLASS_NAME, 'KzDlHZ').text
            price_current = item.find_element(By.CSS_SELECTOR, 'div.Nx9bqj._4b5DiR').text.strip().replace('₹', '').replace(',', '')
            price_original = item.find_element(By.CSS_SELECTOR, 'div.yRaY8j.ZYYwLA').text.strip().replace('₹', '').replace(',', '')
            rating = item.find_element(By.CLASS_NAME, 'XQDdHH').text
            products.append({
                'product_name': product_name,
                'price_current': price_current,
                'price_original': price_original,
                'rating': rating,
            })
        except Exception as e:
            print(f"Error extracting product details: {e}")
            continue
    return products

# Function to navigate to the next page
def go_to_next_page(page_number):
    url = f'https://www.flipkart.com/search?q=mobile+phones&page={page_number}'
    driver.get(url)
    time.sleep(4)  # Wait for the next page to load

# Main scraping logic
all_products = []  # This will store all products from all pages

# Loop through multiple pages
for page_number in range(1, 5):  # Change the range as needed
    go_to_next_page(page_number)
    products = extract_product_details()
    all_products.extend(products)  # Append the products from this page to the master list
    print(f"Scraped page {page_number}")

# Closing the driver
driver.quit()

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(all_products)

# Define the file name
file_name = 'flipkart_product_details.csv'

# Save the DataFrame to a CSV file
df.to_csv(file_name, index=False)

print(f"Product details saved to {file_name}")
