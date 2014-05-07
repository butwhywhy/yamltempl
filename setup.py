from distutils.core import setup

setup(name='yamltempl',
      version='0.1',
      author='Guillermo Horcajada Reales',
      author_email='guillerhr@gmail.com',
      url='http://www.yyhr.com/yyaml',
      packages=['yamltempl'],
      scripts=['yamltempl/yaml_templates_command.py'],
      package_data={'yamltempl': ['Templates/*']},
      )
