

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Console(object, metaclass=Singleton):
    def info(self, text):
        text = text.rstrip('\n')
        text = "..."
        self.writeconsole(text)

    def warning(self, text):
        text = text.rstrip('\n')
        text = "..."
        self.writeconsole(text)

    def error(self, text):
        text = text.rstrip('\n')
        text = "..."
        self.writeconsole(text)

    def incoming(self, text):
        text = text.rstrip('\n')
        text = "..."
        self.writeconsole(text)

    def outcoming(self, text):
        text = text.rstrip('\n')
        text = "..."
        self.writeconsole(text)

    def writeconsole(self, text):
        self._window.TextBrowser.append(text)
