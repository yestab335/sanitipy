from setuptools import setup, find_packages

setup(
  name='sanitipy',
  description='',
  author='Adam Ben-Aamr',
  author_email='adambenaamr@gmail.com',

  # Note: Always update the version number
  version='0.1.1',
  packages=find_packages(),
  install_requires=[
    # Add dependencies here.
    'pandas',
    'numpy',
    'scikit-learn',
    'matplotlib',
  ],
  url='https://github.com/yestab335/sanitipy',
  download_url='',
  keywords=[
    'data',
    'data cleaning',
    'missing data',
    'data science',
    'pandas',
    'python'
  ],
)
