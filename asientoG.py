class Asiento:
    def __init__(self, numero, fila):
        self.__numero = numero
        self.__fila = fila
        self.__reservado = False
        self.__precio = 0.0

    # Getters y Setters
    def get_numero(self):
        return self.__numero

    def get_fila(self):
        return self.__fila

    def is_reservado(self):
        return self.__reservado

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio

    def reservar(self):
        if self.__reservado:
            raise Exception("El asiento ya está reservado.")
        self.__reservado = True

    def cancelar_reserva(self):
        if not self.__reservado:
            raise Exception("El asiento no está reservado.")
        self.__reservado = False
        self.__precio = 0.0
