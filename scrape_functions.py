from pprint import pprint
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

def getDate(element: WebElement):
  """
  Get the date from a date question, DOESN'T RETURN IN DATETIME FORMAT.
  
  :Args
    - element: Question element, type date
  
  :rtype: list
  """
  date = [i.get_attribute("value") for i in element.find_elements(By.TAG_NAME, "input")]
  date = [date[0], date[2], date[4]] # Get the date values in DD/MM/YY format
  return date

def getTextField(element: WebElement):
  """
  Get the value from a text field question.

  :Args
    - element: Question element, type text field
  
  :rtype: str
  """

  text_value = element.find_element(By.CLASS_NAME, "Ih4Dzb").text
  return text_value

def getRadioOption(element: WebElement):
  """
  Get the chosen option from a multiple choice field.

  :Args
    - element: Question element, type multiple choice
  
  :rtype: str
  """

  for option in element.find_elements(By.CLASS_NAME, "docssharedWizToggleLabeledContainer"):
    checked = option.find_element(By.CLASS_NAME, "Od2TWd").get_attribute("aria-checked")

    # if it's the selected one
    if checked == "true":
      option_name = option.find_element(By.CLASS_NAME, "aDTYNe").text
      if option_name == "Otros:":
        other_text = option.find_element(By.XPATH, "..").find_element(By.CLASS_NAME, "rg3hrb").text
        pprint(f"the one selected is other one: {other_text}")
        return other_text
      return option_name
      
      