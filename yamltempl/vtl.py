#! /usr/bin/env python

import os
import airspeed


_templates_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'Templates'))

class PythonUtils(object):

    """
    Exports some built-in Python functions to be used in templates

    This class provides some very simple python functions, which are
    not easily available from the templates, as static
    methods. An instance of this class is available
    in the templates as $python.
    """

    @staticmethod
    def isnone(obj):
        """Returns ``obj is None``"""
        return obj is None

    @staticmethod
    def len(obj):
        """Returns ``len(obj)``"""
        return len(obj)

    @staticmethod
    def clean_final_new_line(string):
        """Returns a copy of the string, removing the final \\n characters"""
        if not isinstance(string, str):
            return string
        while string.endswith('\n'):
            string = string[0:(len(string)-1)]
        return string

    @staticmethod
    def islist(obj):
        """Returns"""
        return isinstance(obj, list)

    @staticmethod
    def isdict(obj):
        return isinstance(obj, dict)


def merge(yamldata, templ):
    """
    Merges yaml data into a string template

    This method invokes airspeed module's:
    ``airspeed.Template(templ).merge(data)``,
    where data is a dictionary containing the passed `yamldata` object
    with key `data` and a ``yamltempl.templates.PythonUtils`` object
    with key `python`.

    Args:
        yamldata (object, tipically dict or list): The object passed to the
            template as ``$data``
        templ (str or unicode): The template

    Returns:
        str or unicode.  The result of merging data

    Raises: TODO

    Examples:
    >>> from yamltempl import vtl
    >>> yaml_data = {'name': 'Will', 'age': 30, 'interests': ['programming', 'sports', 'eating']}
    >>> vtl_template = '''My name is ${data.name} and I am ${data.age}.
    ... I like to format my interests using VTL templates:
    ... #foreach( $interest in ${data.interests} )##
    ...     - $interest
    ... #end##
    ... '''
    >>> result = vtl.merge(yaml_data, vtl_template)
    >>> print result
    My name is Will and I am 30.
    I like to format my interests using VTL templates:
        - programming
        - sports
        - eating
    <BLANKLINE>

    """
    yaml_dict = {'data': yamldata}
    yaml_dict['python'] = PythonUtils()
    #loader = airspeed.CachingFileLoader("/home/guiller/work/yamltempl/yamltempl/Templates/", True)
    loader = airspeed.CachingFileLoader(_templates_path)
    #t = loader.load_template(templ)
    t = airspeed.Template(str(templ))
    result = t.merge(yaml_dict, loader=loader)
    #t = airspeed.Template(templ)
    #result = t.merge(yaml_dict)
    return result


def mergefiles(yamlpath, templpath, outpath):
    from . import yamlutils
    with open(yamlpath) as f:
        yamldata = yamlutils.ordered_load(f)

    with open(templpath) as f:
        templ = f.read().decode('utf8')

    result = merge(yamldata, templ)

    with open(outpath, 'w') as f:
        f.write(tex.encode('utf8'))
