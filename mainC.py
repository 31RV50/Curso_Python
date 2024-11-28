# main.py
from sala_cineC import SalaCine
from exceptionsC import AsientoNoEncontradoException, AsientoYaRegistradoException, AsientoNoReservadoException

def main():
    sala = SalaCine(precio_base=10.0)

    # Agregar asientos
    try:
        sala.agregar_asiento(1, 'A')
        sala.agregar_asiento(2, 'A')
    except AsientoYaRegistradoException as e:
        print(e)

    # Mostrar asientos
    print("Asientos disponibles:")
    sala.mostrar_asientos()

    # Reservar un asiento
    print("\nReservando asiento 1A para una persona mayor de 65 años un miércoles:")
    try:
        precio = sala.reservar_asiento(1, 'A', edad=70, dia='miércoles')
        print(f"Reserva realizada. Precio: ${precio:.2f}")
    except (AsientoNoEncontradoException, AsientoYaRegistradoException) as e:
        print(e)

    # Mostrar asientos después de la reserva
    print("\nAsientos después de la reserva:")
    sala.mostrar_asientos()

    # Cancelar reserva
    print("\nCancelando la reserva del asiento 1A:")
    try:
        sala.cancelar_reserva(1, 'A')
        print("Reserva cancelada.")
    except AsientoNoReservadoException as e:
        print(e)

    # Mostrar asientos después de cancelar
    print("\nAsientos después de cancelar la reserva:")
    sala.mostrar_asientos()


if __name__ == "__main__":
    main()
