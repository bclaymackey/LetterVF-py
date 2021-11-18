from distutils.core import setup

setup(name='LetterVF',
      version='0.0.1',
      description='automatic cluster analysis of phonemic verbal fluency task data',
      author='Brandon C. Mackey',
      author_email='bclaymackey@gmail.com',
      packages=['LetterVF'],
      url='https://github.com/Visscher-Lab/LetterVF',
      long_description=open('README.txt').read(),
      license='MIT license',
      install_requires=['xlsxwriter',
                        'numpy']
     )
