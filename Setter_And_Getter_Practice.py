class Humano:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    # definir el getter
    @property
    def nombre(self):
        return self._nombre

    # definir el setter
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if not type(nuevo_nombre) == str:
            raise ValueError("El nombre tiene que ser del tipo string [str]")
        self._nombre = nuevo_nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        if not type(nueva_edad) == int:
            raise ValueError("La edad tiene que ser de tipo integer [int]")
        self._edad = nueva_edad


persona1 = Humano(nombre="Mar", edad=32)

print(f"El nombre de persona1 es {persona1.nombre} y su edad es {persona1.edad}")

# tu puedes ahora mismo ponerle cuaquier valor tanto al atributo
# nombre y edad, porque no hemos definido ningun getter ni setter

# getter - get - coger, tomar, agarrar
# setter - set - establecer

persona1.nombre = "Maria"
persona1.edad = 78
print("Despues del cambio", "-" * 30)
print(f"El nombre de persona1 es {persona1.nombre} y su edad es {persona1.edad}")