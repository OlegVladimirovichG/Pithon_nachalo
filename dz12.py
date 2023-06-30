def create_argument_dictionary(**kwargs):
    argument_dictionary = {}
    for key, value in kwargs.items():
        if not isinstance(key, (int, float, str, bool)):
            key = str(key)
        argument_dictionary[value] = key
    return argument_dictionary

result = create_argument_dictionary(arg1='value1', arg2='value2', arg3='value3')
print(result)
