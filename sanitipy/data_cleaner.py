import pandas as pd
from .validator import Validator
from .preprocessor import Preprocessor

class DataCleaner:
  def __init__(self, data: pd.DataFrame):
    self.data = data
    self.validator = Validator(data)
    self.preprocessor = Preprocessor(data)
  
  def clean_data(self):
    self.validator.check_missing_values()
    self.validator.remove_na()
    self.validator.remove_duplicates()

    return self.data
