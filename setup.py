from setuptools import setup, find_packages

setup(name='python_course',
      version='0.1',
      url='https://github.com/provider161/python_qa_course',
      license='MIT',
      author='Chaplygin Mikhail',
      author_email='provider8@yandex.ru',
      description='Otus qa python code',
      long_description=open('README.md').read(),
      packages=find_packages(exclude=['logs', 'allure_results']),
      setup_requires=['pytest==5.2.1',
                      'selenium',
                      'pylint',
                      'requests',
                      'selenium',
                      'pytest-html',
                      'allure-pytest',
                      'sqlalchemy',
                      'pymysql',
                      'paramiko'],
      python_requires='>=3.6',
      zip_safe=False
      )
