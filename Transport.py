class Transport:

    def __init__(self, tipo):
        self.tipo = tipo

    def get_tipo(self):
        return "Mi tipo es: %s" % self.tipo