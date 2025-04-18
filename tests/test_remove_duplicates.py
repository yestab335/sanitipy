import unittest
import pandas as pd
from sanitipy.sanitipy import DataCleaner

class TestRemoveDuplicates(unittest.TestCase):
  def set_up(self):
    self.data = pd.DataFrame({
      'A': [1, 1, 2, 2],
      'B': [3, 3, 4, 4]
    })
    self.cleaner = DataCleaner(self.data)

  def test_remove_duplicates_removes_duplicate_rows(self):
    # Call the remove_duplicates() method from the Validator class
    cleaned_data = self.cleaner.validator.remove_duplicates()

    # Check the length of the cleaned DataFrame
    self.assertEqual(len(cleaned_data), 2)

    # Check the contents of the cleaned DataFrame
    expected_data = pd.DataFrame({
      'A': [1, 2],
      'B': [3, 4]
    })

    pd.testing.assert_frame_equal(cleaned_data.reset_index(drop=True), expected_data)

if __name__ == '__main__':
  unittest.main()
