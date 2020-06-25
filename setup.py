from setuptools import setup

setup(name='careerjet_api',
      version='3.0.1',
      description='Python interface to Careerjet\'s public search API',
      url='http://github.com/careerjet/careerjet-api-client-python',
      author='Careerjet',
      #author_email='',
      license='MIT',
      packages=['careerjet_api'],
      install_requires=['requests'],
      zip_safe=False)
