"""
Preprocessor Class for Data Transformation and Cleaning

This file defines the `Preprocessor` class, designed to perform essential preprocessing operations on a dataset
stored as a pandas DataFrame. The class includes methods for inferring data types, normalizing numerical data, 
encoding categorical variables, and allowing users to ignore specified columns during transformations.

Key Features:
  - Infer Data Types (`infer_data_types`): This method attempts to convert columns to their appropriate data types.
  For instance, it identifies potential datetime columns and converts their format, fills missing values with 
  the most frequent value (mode), and converts numerical data into standardized formats.
  
  - Ignore Columns (`ignore_column`): Enables users to specify columns that should be ignored during preprocessing. 
  Note: The logic for ignoring columns needs to be implemented further for this feature.

  - Normalize Numerical Data (`normalize_data`): Normalizes numerical columns using `StandardScaler` to ensure 
  consistent scaling of features for machine learning models.

  - Encode Categorical Variables (`encode_categorical`): Automatically generates dummy variables for all categorical 
  columns in the dataset to facilitate their use in predictive modeling.
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler

class Preprocessor:
  def __init__(self, data: pd.DataFrame):
    self.data = data

  def remove_duplicates(self):
    self.data = self.data.drop_duplicates()

    return self.data
  
  def remove_na(self):
    self.data = self.data.dropna()

    return self.data
  
  def infer_data_types(self, df):
    for col in df.columns:
      if df[col].dtype == 'object':
        # Check for datetime columns
        try:
          pd.to_datetime(df[col], format="%Y/%m/%d")
          df[col] = pd.to_datetime(df[col], errors='coerce')
        except (ValueError, TypeError):
          pass
      
      # Fill in NaN values with the mode (mode frequent value) if applicable
      if df[col].dtype == 'object':
        df[col] = df[col].astype('string')
      elif df[col].dtype in ['float64', 'int64']:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    
    return df
  
  """
  Function will iterate though the dataset but ignore the columns that were
  specified by the user.
  """
  def ignore_column(self, column = []):
    column_to_ignore = column

    for x in column_to_ignore:
      print(x)
  
  def normalize_data(self):
    # Select only numeric columns for normalization
    numeric_data = self.data.select_dtypes(include=['float64', 'int64'])

    scaler = StandardScaler()
    normalized_data = pd.DataFrame(scaler.fit_transform(numeric_data), columns=numeric_data.columns)

    # Repalce the numeric columns in the originial DataFrame with the normalized one
    self.data[numeric_data.columns] = normalized_data
    self.data = pd.concat([self.data.drop(columns=numeric_data.columns), normalized_data], axis=1)

    return self.data
