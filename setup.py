from setuptools import setup, find_packages
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'python_utils',         # How you named your package folder (MyLib)
  packages=find_packages(exclude=['tests*']),
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Basic python utilities',   # Give a short description about your library
  author = 'Stephen Swart',                   # Type in your name
  url = 'https://github.com/sdswart/python_utils.git',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/sdswart/python_utils/archive/v_01.tar.gz',    # Used for pipy
  keywords = ['utilities',],   # Keywords that define your package best
  long_description=long_description,
  long_description_content_type="text/markdown",
  install_requires=['numpy','re'],
  classifiers=[
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
  ]
)
