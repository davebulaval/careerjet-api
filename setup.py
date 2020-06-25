import os

from setuptools import setup

current_file_path = os.path.abspath(os.path.dirname(__file__))


def get_readme():
    readme_file_path = os.path.join(current_file_path, 'README.md')
    with open(readme_file_path, 'r', encoding='utf-8') as f:
        return f.read()


def main():
    readme = get_readme()
    setup(name='careerjet_api',
          version='3.1',
          description='Python interface to Careerjet\'s public search API',
          url='https://github.com/davebulaval/careerjet-api',
          author='davebulaval',
          # author_email='',
          license='MIT',
          packages=['careerjet_api'],
          python_requires='>=3.6.1',
          install_requires=['requests'],
          long_description=readme,
          long_description_content_type='text/markdown',
          zip_safe=False)


if __name__ == '__main__':
    main()
