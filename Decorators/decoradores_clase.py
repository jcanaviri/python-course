import inspect

def dec_rpr(cls):
    print('Decorating')
    print(f'cls value is {cls.__name__}')

    # Recuperar atributos con vars()
    attrs = vars(cls)
    for name, attr in attrs.items():
        print(f'{name} -> {attr}')

    # Se ha sobreescrito el Constructor
    if '__init__' not in attrs:
        raise TypeError(f'{cls.__name__} do not have a constructor')
    
    sign_init = inspect.signature(cls.__init__)
    print(f'Firma {sign_init}') # (self, first_name, last_name)

    params_init = list(sign_init.parameters)[1:]
    print(f'Params {params_init}') # [first_name, last_name]

    for param in params_init:
        is_property = isinstance(attrs.get(param), property)
        if not is_property:
            raise TypeError(f'{param} it is not a property')

    # Creamos el metodo repr
    def method_rep(self):
        class_name = self.__class__.__name__

        generator_arg =(f'{name}={getattr(self, name)!r}' for name in params_init)
        list_args = list(generator_arg)
        print(f'The list {list_args}')

        args = ', '.join(list_args)

        return f'<{class_name} {args}>'

    # Agregar el método
    setattr(cls, '__repr__', method_rep)

    return cls

@dec_rpr
class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def first_name(self):
        return self._first_name
    
    @property
    def last_name(self):
        return self._last_name

john = Person('John', 'Snow')
sansa = Person('Sansa', 'Stark')
print(john)
print(sansa)
