import pandas as pd

class Validator:
  """
  A utility class for validating and inspecting pandas DataFrames.

  This class provides methods to check for missing values and
  validate the consistency of data types across a dataset.

  Parameters:
  -----------
  data: pd.DataFrame
  - The dataset to be validated.

  Attributes:
  -----------
  data: pd.DataFrame
  - The input dataset.

  empty: bool
  - Indicates whether the dataset contains missing values.
  """
  def __init__(self, data: pd.DataFrame) -> None:
    self.data = data
    self.empty = self.check_missing_values(data) > 0

  def validate_data_types(self) -> bool:
    """
    Validate whether the dataset has consistent data types.

    Parameters:
    -----------
    None
    - This function does not take any parameters.

    Returns:
    --------
    bool
    - True if the dataset contains missing values or if all
    columns share the same data type, False otherwise.
    """
    # Check for consistent data types
    if self.empty:
      return True
    
    data_types = self.data.dtypes

    if data_types.nunique() == 1:
      return True
    else:
      return False
    
  def check_missing_values(self, data: pd.DataFrame) -> int:
    """
    Count the total number of missing values in the dataset.

    Parameters:
    -----------
    data: pd.DataFrame
    - The dataset in which to check for missing values

    Returns:
    --------
    int
    - The total number of missing values across the entire dataset.
    """
    if data is None:
      return 0

    # Identify missing values in the dataset
    return data.isnull().sum().sum()
