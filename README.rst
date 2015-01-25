=========
YamlTempl
=========

This project allows formatting data given in `YAML format`_
with templates using `Velocity Template Language`_ (VTL).

Installation
============
The typical installation methods for python packages should work:

* Manually:

  1. Download the compressed project, extract it and move to the
     project's base directory
  2. Execute the setup.py script::

        python setup.py install

* Using ``pip``::

    pip install -U yamltempl

Usage
=====
The script ``yaml_templates_command.py`` provides a command line interface.
The following command would combine the data given in yaml format in the 
``data.yaml`` file with the VTL template file ``templ.html`` to provide
the result in ``data.html``.::

    ./yaml_templates_command.py --template templ.html --output data.html data.yaml

For help on the command line utility usage:::

    ./yaml_templates_command.py --help

The following code shows the use within python:::

    >>> from yamltempl import yamlutils, vtl
    >>> yaml_text = """
    ... name: Will
    ... age: 30
    ... interests:
    ...     - programming
    ...     - sports
    ...     - eating
    ... """
    >>> yaml_data = yamlutils.ordered_load(yaml_text)
    >>> vtl_template = """My name is ${data.name} and I am ${data.age}.
    ... I like to format my interests using VTL templates:
    ... #foreach( $interest in ${data.interests} )##
    ...     - $interest
    ... #end##
    ... """
    >>> result = vtl.merge(yaml_data, vtl_template)
    >>> print result
    My name is Will and I am 30.
    I like to format my interests using VTL templates:
        - programming
        - sports
        - eating
    <BLANKLINE>



    

Dependencies
============
This project depends on the following python packages:

* PyYAML_. YAML support for python
* airspeed_. VTL template engine for python


.. _YAML format: yaml_
.. _Velocity Template Language: velocity_
.. _yaml: http://yaml.org/
.. _velocity: https://velocity.apache.org/engine/releases/velocity-1.5/user-guide.html#velocity_template_language_vtl:_an_introduction
.. _PyYAML: http://pyyaml.org/wiki/PyYAML
.. _airspeed: https://github.com/purcell/airspeed
