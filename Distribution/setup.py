from setuptools import setup

setup(name='VedicCityNames',
      version='0.2.3',
      description='Translates current city names in India to their original names',
      long_description='Long description - Translates current city names in India to their original names',
      url='http://github.com/muditjai/Python.git/Distribution/VedicCityNames',
      author='muditjai',
      author_email='muditjai@gmail.com',
      license='MIT',
      packages=['VedicCityNames'],
      install_requires=['pyyaml'],
      include_package_data=True,
      zip_safe=False,
      tests_require=['pytest'],
      setup_requires=['pytest-runner'])
