from pprint import pprint
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

from lib import joinTwoArrays

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=c:\\Users\\Ticua\\AppData\\Local\\Google\\Chrome\\User Data\\")
driver = webdriver.Chrome(options=options)

# driver.get("https://docs.google.com/forms/d/1aHBvqirBuINCZLI-rEE-Spu4SOxTDVPkJ4OxP-6_v5c/edit#response=ACYDBNgvxEqvzydtC_N0wJWNO1lY1GV8EK7doRNQAOrgr31_jtEnWCQwPktN0XPuANSIK38")
driver.get("https://docs.google.com/forms/d/1HP9dVlB2IF_87c66isam1gRm8q6AgP4ltpcMdqwCHGQ/edit#response=ACYDBNi-wpSV23He9GdXOm7QQdGMG8HC1tkuu3I1Ab6CQc9NhC0OWgCBQlFTR1WR01xApF4")
time.sleep(5)

# Reset count to first answer
answers_count_field = driver.find_element(
  by=By.XPATH,
  value="/html/body/div[2]/div[2]/div[1]/div[2]/div/div[4]/div/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div/div[1]/input"
)
answers_count_field.clear()
answers_count_field.send_keys("1")

# fields = [i.text for i in driver.find_elements(by=By.CLASS_NAME, value="M7eMe")]
fields = []

for field in driver.find_elements(by=By.CLASS_NAME, value="M7eMe"):
  if field.get_attribute("class") == "M7eMe":
    # print(field.get_attribute("class"))
    fields.append(field.text)

# print(f"Fields are {fields}")


answers = []
# Amount of answers
count = int(driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div[1]/div[2]/div/div[4]/div/div[1]/div[1]/div[2]/div[2]/div/div[3]").text)
while count != 0:
  time.sleep(2)
  answers.append(
    joinTwoArrays(
      key_array=fields,
      value_array=[i.text for i in driver.find_elements(By.CLASS_NAME, "Mh5jwe.JqSWld.yqQS1")]
    )
  )

  # Might throw warning, because the element we click is a span (dumbass google not using buttons)
  driver.find_element(
    by=By.XPATH,
    value="/html/body/div[2]/div[2]/div[1]/div[2]/div/div[4]/div/div[1]/div[1]/div[2]/div[3]/div/span"
  ).click()
  count -= 1

pprint(answers)

time.sleep(5)
driver.quit()