def is_primitive(variable) -> bool:
    primitives = (int, str, bool, float)
    return isinstance(variable, primitives)

def clone_list(array: list):
    output = []
    for item in array:
        if isinstance(item, list):
            cloned = clone_list(item)
            output.append(cloned)
            continue

        if is_primitive(item):
            output.append(item)
            continue

        raise TypeError('Can\'t clone variable which is not nested list of primitive types')

def to_array(tuple: tuple):
    output = []
    for i in tuple:
        output.append(i)
    
    return output