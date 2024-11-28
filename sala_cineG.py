from asientoG import Asiento


class SalaCine:
    def __init__(self, precio_base):
        self.__asientos = []
        self.__precio_base = precio_base

    # Agregar un asiento
    def agregar_asiento(self, numero, fila):
        for asiento in self.__asientos:
            if asiento.get_numero() == numero and asiento.get_fila() == fila:
                raise Exception("El asiento ya está registrado.")
        self.__asientos.append(Asiento(numero, fila))

    # Reservar un asiento
    def reservar_asiento(self, numero, fila, edad, dia):
        asiento = self.buscar_asiento(numero, fila)
        if not asiento:
            raise Exception("El asiento no existe.")
        
        # Calcular precio con descuentos
        precio = self.__calcular_precio(edad, dia)
        asiento.set_precio(precio)
        asiento.reservar()
        return precio

    # Cancelar una reserva
    def cancelar_reserva(self, numero, fila):
        asiento = self.buscar_asiento(numero, fila)
        if not asiento:
            raise Exception("El asiento no existe.")
        asiento.cancelar_reserva()

    # Mostrar asientos
    def mostrar_asientos(self):
        for asiento in self.__asientos:
            estado = "Reservado" if asiento.is_reservado() else "Disponible"
            print(
                f"Asiento {asiento.get_numero()} en fila {asiento.get_fila()} - {estado} - Precio: ${asiento.get_precio():.2f}"
            )

    # Buscar un asiento
    def buscar_asiento(self, numero, fila):
        for asiento in self.__asientos:
            if asiento.get_numero() == numero and asiento.get_fila() == fila:
                return asiento
        return None

    # Método privado para calcular el precio
    def __calcular_precio(self, edad, dia):
        precio = self.__precio_base
        if dia.lower() == "miércoles":
            precio *= 0.8
        if edad >= 65:
            precio *= 0.7
        return precio
