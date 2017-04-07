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

    """def saludo(self, *args, **kwargs):
        print(kwargs['saludo'])
        print(args[0])
        Llamada --> saludo(saludo = "Hola mi hermanito", nombre = "Mi nombre es ") """

    def __str__(self):
        return "Este es un Robot llamado %s" % self.name

    def __repr__(self):
        return "Object Robot with name = %s, last_name = %s & age = %s " % (self.name, self._last_name, (self.getAge()))

    def __del__(self):  # Destruye los objetos cuando ya no son utilizados
        texto = "Objeto Destruido llamado = %s" % self.name
        print(texto)

    def saluda(self):
        return "Hola mi nombre es %s y tengo %s años" % (self.name, str(self.getAge()))

if __name__ == '__main__' :

    robot = Robot('Diego', 'Barriga', 21)
    robot_2 = Robot('Eren', 'Suazo', 23)
    print("Llamando el objeto robot: ", robot)  # Manda llamar el método __str__
    print("Llamando el objeto robot: ", robot_2)
    print(repr(robot))  # repr funciona para mostrar detalles de objetos (DEBUG)
    print(Robot.__dict__)
    dic = robot.__dict__.copy()
    dic['saludo'] = "Hola a todos"
    print(dic)
    print(robot.saluda())
    print(robot._last_name)

