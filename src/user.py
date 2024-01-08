class Usuario:

    def __init__(self, nombre, numero_de_telefono, mensaje):
        self._nombre = nombre
        self._numero_de_telefono = numero_de_telefono
        self._mensaje = mensaje

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser una cadena de caracteres")
        self._nombre = nombre

    @property
    def numero_de_telefono(self):
        return self._numero_de_telefono

    @numero_de_telefono.setter
    def numero_de_telefono(self, numero_de_telefono):
        if not isinstance(numero_de_telefono, str):
            raise ValueError("El número de teléfono debe ser una cadena de caracteres")
        if not numero_de_telefono.startswith("+"):
            numero_de_telefono = "+{}".format(numero_de_telefono)
        self._numero_de_telefono = numero_de_telefono

    @property
    def mensaje(self):
        return self._mensaje

    @mensaje.setter
    def mensaje(self, mensaje):
        if not isinstance(mensaje, str):
            raise ValueError("El mensaje debe ser una cadena de caracteres")
        self._mensaje = mensaje

