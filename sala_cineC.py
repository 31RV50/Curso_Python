# sala_cine.py
from asientoC import Asiento
from preciosC import calcular_precio
from exceptionsC import AsientoNoEncontradoException, AsientoYaRegistradoException, AsientoNoReservadoException

class SalaCine:
    def __init__(self, precio_base):
        self.__asientos = []
        self.__precio_base = precio_base

    # Agregar un asiento
    def agregar_asiento(self, numero, fila):
        for asiento in self.__asientos:
            if asiento.get_numero() == numero and asiento.get_fila() == fila:
                raise AsientoYaRegistradoException("El asiento ya está registrado.")
        self.__asientos.append(Asiento(numero, fila, self.__precio_base))

    # Reservar asiento
    def reservar_asiento(self, numero, fila, edad, dia):
        asiento = self.buscar_asiento(numero, fila)
        if not asiento:
            raise AsientoNoEncontradoException("El asiento no existe.")
        
        # Calcular precio con descuentos
        precio = calcular_precio(self.__precio_base, dia, edad)
        asiento.set_precio(precio)
        asiento.reservar()
        return precio

    # Cancelar reserva
    def cancelar_reserva(self, numero, fila):
        asiento = self.buscar_asiento(numero, fila)
        if not asiento:
            raise AsientoNoEncontradoException("El asiento no existe.")
        asiento.cancelar_reserva()

    # Mostrar asientos
    def mostrar_asientos(self):
        for asiento in self.__asientos:
            estado = "Reservado" if asiento.is_reservado() else "Disponible"
            print(
                f"Asiento {asiento.get_numero()} en fila {asiento.get_fila()} - {estado} - Precio: ${asiento.get_precio():.2f}"
            )

    # Buscar asiento
    def buscar_asiento(self, numero, fila):
        for asiento in self.__asientos:
            if asiento.get_numero() == numero and asiento.get_fila() == fila:
                return asiento
        return None
