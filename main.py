from pprint import pprint
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

from lib import getQuestionType, joinTwoArrays
from scrape_functions import getDate, getRadioOption, getTextField

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=c:\\Users\\Ticua\\AppData\\Local\\Google\\Chrome\\User Data\\")
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)


driver.get("https://docs.google.com/forms/d/1HP9dVlB2IF_87c66isam1gRm8q6AgP4ltpcMdqwCHGQ/edit#response=ACYDBNhR5XHblSb7payBhf7VSBVAICao2SPikdL-U5SXB1pGt6B2Tr3-WfxaU77Y6oe7N2A")
time.sleep(5)

answer = {}

for element in driver.find_elements(By.CLASS_NAME, "Qr7Oae"):

    question = element.find_element(By.CLASS_NAME, "OxAavc")
    questionTitle = element.find_element(By.CLASS_NAME, "M7eMe").text
    questionType = question.get_attribute("jscontroller")

    match getQuestionType(questionType=questionType):
      case "date":
        answer[questionTitle] = getDate(element=question)
      case "text_field":
        answer[questionTitle] = getTextField(element=question)
        pass
      case "multiple_choice":
        answer[questionTitle] = getRadioOption(element=question)
    

pprint(answer)

time.sleep(5)
driver.quit()