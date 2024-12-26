def introspection_info(obj):
    info = {}

    info['Type'] = type(obj).__name__
    info['Attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    info['Methods'] = [method for method in dir(obj) if callable(getattr(obj, method))]
    info['Module'] = obj.__class__.__module__

    # Другие интересные свойства объекта
    if isinstance(obj, list):
        info['Length'] = len(obj)
    elif isinstance(obj, dict):
        info['Keys'] = list(obj.keys())
        info['Values'] = list(obj.values())

    return info


# Пример использования
my_list = [1, 2, 3]
print(introspection_info(my_list))

my_dict = {'a': 1, 'b': 2}
print(introspection_info(my_dict))
