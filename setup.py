from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='printess',
  version='0.0.1',
  description='printer with cool add-ons',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='ahmed elnakeeb',
  author_email='ahmedelnakeeb2016@outlook.com',
  license=' GNU GPLv3', 
  classifiers=classifiers,
  keywords='printess', 
  packages=find_packages(),
  install_requires=[''] 
)
