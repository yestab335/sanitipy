import pandas as pd
from data_cleaning.data_cleaner import DataCleaner
from data_cleaning.preprocessor import Preprocessor

def main():
  # Load sample data
  data = pd.read_csv('./sample_data/sample_data.csv')

  newData = Preprocessor.infer_data_types(data)

  # Initialize the DataCleaner
  cleaner = DataCleaner(newData)

  # Perform cleaning operations
  cleaned_data = cleaner.clean_data()

  # Display cleaned data
  print(cleaned_data.head())

if __name__ == '__main__':
  main()
