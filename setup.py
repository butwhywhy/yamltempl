from setuptools import setup

setup(name='yamltempl',
      version='0.1',
      description='Apply Velocity Template Language to data in YAML format',
      author='Guillermo Horcajada Reales',
      author_email='guillerhr@gmail.com',
      url='https://github.com/butwhywhy/yamltempl',
      license='MIT',
      packages=['yamltempl'],
      scripts=['yamltempl/yaml_templates_command.py'],
      package_data={'yamltempl': ['Templates/*']},
      install_requires=['pyyaml', 'airspeed>=0.4dev'],
      )
