import yaml
from collections import OrderedDict


def ordered_load(stream, Loader=yaml.Loader, object_pairs_hook=OrderedDict):

    class OrderedLoader(Loader):
        pass
    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        lambda loader, node: object_pairs_hook(loader.construct_pairs(node)))
    return yaml.load(stream, OrderedLoader)


def main():
    # usage example:
    # ordered_load(stream, yaml.SafeLoader, collections.OrderedDict)

    _test_yaml = """
    - b: B
    - a: A
    - c: C
    - d: 
         - 1
         - 2
         - 3
    - e: 
        - a: A
          b: B
    """
    _test_yaml2 = """ 
    b: B
    a: A
    c: C
    d: 
        - 1
        - 2
        - 3
    e: 
        a: A
        b: B
    """
    print ordered_load(_test_yaml2, yaml.SafeLoader)
    print yaml.load(_test_yaml)

if __name__ == '__main__':
    main()
