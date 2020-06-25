from setuptools import setup

setup(name='careerjet_api',
      version='3.1',
      description='Python interface to Careerjet\'s public search API',
      url='https://github.com/davebulaval/careerjet-api',
      author='Davebulaval',
      # author_email='',
      license='MIT',
      packages=['careerjet_api'],
      install_requires=['requests'],
      zip_safe=False)
