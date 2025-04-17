import pandas as pd
from .validator import Validator
from .preprocessor import Preprocessor

class DataCleaner:
  def __init__(self, data: pd.DataFrame):
    self.data = data
    self.validator = Validator(data)
    self.preprocessor = Preprocessor(data)
  
  def help(self):
    print('More information can be found on the offical docs')
    print('Link: https://link.netlify.app')
  
  def clean_data(self):
    self.validator.check_missing_values()
    self.validator.remove_na()
    self.validator.remove_duplicates()

    return self.data
  
  def AutoClean():
    print('This project has just started!')
    print('It is actively being worked on...')
    print('As of right now I have only published this project to reserve the name')
    print('Sorry for the inconvience')

if __name__ == '__main__':
  DataCleaner()
