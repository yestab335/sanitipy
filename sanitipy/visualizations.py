import pandas as pd
import matplotlib.pyplot as plt
import missingno as msno
from .validator import Validator

class Visualizations(Validator):
  """
  Provides visualization utilities for exploring a dataset, 
  with a focus on missing values.
  
  This class extends the `Validator` class and adds methods to 
  graphically represent missing data in a pandas DataFrame.

  Parameters:
  -----------
  data: pd.DataFrame
  - The dataset to be validated and visualized.

  Methods:
  --------
  show_missing_values()
  - Displays a bar chart of missing values per column in the dataset.
  """
  def __init__(self, data: pd.DataFrame) -> None:
    super().__init__(data)

  def show_missing_values(self) -> None:
    """
    Display a bar chart of missing values in the dataset.

    The chart shows the number of non-missing (observed) values
    for each column in the DataFrame, helping to identify the
    extent and distribution of missing data.

    Parameters:
    -----------
    None
    - This method is not supposed to take any type of parameters.

    Returns:
    --------
    None
    - This method produces a matplotlib plot and does not return any value.

    See Also:
    ---------
    missingno.bar: Function from the `missingno` package used to generate the missing values bar chart.
    """
    data_frame = self.data
    
    plt.title('Missing Values in Dataset')
    plt.xlabel('Column Names')
    plt.ylabel('Total Observations')
    msno.bar(data_frame)
    plt.show()
