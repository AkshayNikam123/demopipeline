from setuptools import setup,find_packages

setup(name="Census-income",
      version="0.0.1",
      author="akshay",
      author_email="nikam.ak152@gmail.com",
      packages=find_packages(),
      install_requires=["pandas","numpy","flask"]
      )