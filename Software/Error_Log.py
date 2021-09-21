#from colorama import init, Fore, Back, Style
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class ErrorLog(metaclass=SingletonMeta):
    def __init__(self):
        self.log = ""

    def log_error(self, msg):
        self.log += msg + "\n"
        print("SE AGREGO UN NUEVO ERROR --> " + self.log)

    def print(self):
        print(self.log)

    def clean(self):
        self.log = ""