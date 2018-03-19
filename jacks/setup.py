from setuptools import setup, find_packages

setup(name='jacks',
      version='0.1',
      description='JACKS package for processing CRISPR/Cas9 Screens',
      url='http://github.com/felicityallen/JACKS',
      author='Felicity Allen and Leopold Parts',
      license='MIT',
      include_package_data=True,
      packages=find_packages(),
      install_requires=['scipy','numpy'],
      zip_safe=False)
      
      