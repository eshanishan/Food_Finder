import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import json


# Correctly specify the path to your ChromeDriver
chromedriver_path = "C:\\Users\\idhan\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
service = Service(chromedriver_path)

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=service)

# Get the current date in the format "YYYY-MM-DD"
# current_date = datetime.now().strftime("%Y-%m-%d")

# URL you want to scrape
for i in range(10, 32):
  url = f"https://dininguiowa.nutrislice.com/menu/catlett-market-place/lunch-2/2024-11-{i}/"
  driver.get(url)

  # Find the "View Menus" button and click it
  # Wait until the "View Menus" button is clickable and then click it
  try:
    view_menus_button = WebDriverWait(driver, 5).until(
      EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='018026bcdb3445168421175d9ae4dd06' and contains(text(), 'View Menus')]"))
    )
    view_menus_button.click()
  except Exception as e:
  # Wait for the page to load (n seconds)
    time.sleep(3)


  # Find all buttons with the specified HTML tag and click them
  buttons = driver.find_elements(By.XPATH, "//a[@id='section-toggle' and @role='button']")
  for button in buttons:
    try:
      button.click()
      time.sleep(.1)  # Wait a bit for the content to load
    except Exception as e:
      print(f"Could not click button: {e}")
  # List of button texts to click
  # buttons_to_click = [
  #   "Beverages", "Breads & Spreads", "Burger Bar", "Cereal", "Condiments", 
  #   "Deli Bar", "Delights", "Family Table", "Fire Up", "Flavors Abroad", 
  #   "Fruit & Yogurt", "Frozen Yogurt Bar", "Gluten Free", "Salad Bar", 
  #   "Sprouts", "Za!"
  # ]

  # # Click each button
  # for button_text in buttons_to_click:
  #   try:
  #     button = WebDriverWait(driver, 5).until(
  #       EC.element_to_be_clickable((By.XPATH, f"//a[@id='section-toggle' and contains(text(), '{button_text}')]"))
  #     )
  #     button.click()
  #     time.sleep(.1)  # Wait a bit for the content to load
  #   except Exception as e:
  #     print(f"Could not click button with text '{button_text}': {e}")

  # Get the page source
  page_source = driver.page_source


  # Save the HTML content to a file

  with open('Iowa.html', 'w', encoding='utf-8') as file:
    file.write(page_source)

  with open('Iowa.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

  def extract_food_names(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    food_names = [food.get_text(strip=True) for food in soup.find_all(class_='food-name')]
    return food_names

  food_names = extract_food_names(html_content)

  # Print the food names
  print(food_names)

  # Save the food names to a new file as an array

  # Load existing food names from the file if it exists
  try:
    with open('static/food_cattlet.json', 'r', encoding='utf-8') as file:
      existing_food_names = json.load(file)
  except FileNotFoundError:
    existing_food_names = []

  # Add new food names if they are not already in the list
  new_food_names = [food for food in food_names if food not in existing_food_names]
  all_food_names = existing_food_names + new_food_names

  # Save the updated food names to the file
  with open('static/food_cattlet.json', 'w', encoding='utf-8') as file:
    json.dump(all_food_names, file, ensure_ascii=False, indent=4)
