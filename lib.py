def joinTwoArrays(key_array: list, value_array: list):
  """
  Make a dictionary from 2 arrays
  :Args
    - key_array: Array that will be used to set keys
    - value_array: values for the 2 keys

  :rtype: dict
  """
  if(len(key_array) != len(value_array)):
    raise Exception("Key array and value array are not the same length.")
  
  output = {}

  for key, value in zip(key_array, value_array):
    output[key] = value
  
  return output

def getQuestionType(questionType: str):
  """
  Return type of question
  :Args
    - questionType: String found in jscontroller attribute

  :rtype: str
  """

  match questionType:
    case "qDmeqc":
      return "date"

    case "rDGJeb":
      return "text_field"
    
    case "pkFYWb":
      return "multiple_choice"
    
    case _:
      return None

