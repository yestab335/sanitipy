import pandas as pd

class Validator:
  def __init__(self, data: pd.DataFrame):
    self.data = data
  
  def validate_data_types(self):
    # Check for consistent data types
    if self.empty:
      return True
    
    data_types = self.dtypes

    if data_types.nunique() == 1:
      return True
    else:
      return False
    
  def check_missing_values(self):
    # Identify missing values in the dataset
    return self.data.isnull().sum()
