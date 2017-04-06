# DIA 2: Programación Orientaba a Objetos
class Robot:
    def __init__(self, name=None, last_name=None, age=None):
        self.name = name
        self._last_name = last_name  # Protected
        self.__age = age  # Private

    def getAge(self):
        return self.__age

    def setAge(self, age):
        self.__age = age

    def saludo(self, *args, **kwargs):
        print(kwargs['saludo'])
        print(args[0])

    def saluda(self):
        return "Hola mi nombre es %s y tengo %s años" % (self.name, str(self.getAge()))

# Llamada --> saludo(saludo = "Hola mi hermanito", nombre = "Mi nombre es ")