from yamltempl.vtl import merge

data = [
       ({'prop1': 'value1', 'prop2': 'value2'}, 
        '${data.prop1} \n ${data.prop2} ${data.prop1}', 
        'value1 \n value2 value1'
       ),
       (['val1', 'val2', {'k1': 'v31', 'k2': 'v32'}],
        '${data[0]}, ${data[1]}, ${data[2].k1}, ${data[2].get("k2")}',
        'val1, val2, v31, v32'
       ),
       ]

def check_merge(yaml_data, template, result):
    assert merge(yaml_data, template) == result


def test_merge():
    for (yaml_data, template, result) in data:
        yield check_merge, yaml_data, template, result
