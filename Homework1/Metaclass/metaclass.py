class TypeChecking(type):

    def __new__(cls, name, bases, dct):
        X = super().__new__(cls, name, bases, dct)
        for i, j in X.__dict__.items():
            if not i.startswith("__"):
                if type(X.__dict__[i]) != X.__annotations__[i]:
                    raise Exception("Incorrect type")
        return X


class P(metaclass=TypeChecking):

    x: int = 2          #correct
    y: str = "fgd"      #correct
    z: float = 2.5      #correct



class G(metaclass=TypeChecking):
    g: int = 6          #correct
    h: str = 2.5        #incorrect - Error

