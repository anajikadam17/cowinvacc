from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='cowinvacc',
  version='0.0.1',
  description='Cowin Tracker for Covid-19 vaccine usng CoWin APIs.',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='anajikadam17',
  author_email='anajikadam17@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='cowin, covid, vaccine, cowinvacc',
  packages=['cowinvacc'],
  include_package_data=True,
  python_requires='>=3.6, <4',
  install_requires=['certifi==2020.12.5',
                  'chardet==4.0.0',
                  'idna==2.10',
                  'numpy==1.20.2',
                  'pandas==1.2.4',
                  'python-dateutil==2.8.1',
                  'pytz==2021.1',
                  'requests==2.25.1',
                  'six==1.16.0',
                  'urllib3==1.26.4'],
)


