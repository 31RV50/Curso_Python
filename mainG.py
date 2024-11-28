from sala_cineG import SalaCine


def main():
    precio_base = 100.0
    sala = SalaCine(precio_base)

    # Agregar asientos a la sala
    print("Agregando asientos...")
    sala.agregar_asiento(1, 'A')
    sala.agregar_asiento(2, 'A')
    sala.agregar_asiento(3, 'B')

    # Mostrar asientos
    print("\nAsientos disponibles:")
    sala.mostrar_asientos()

    # Reservar un asiento
    print("\nReservando asiento 1A para una persona de 70 años un miércoles...")
    try:
        precio = sala.reservar_asiento(1, 'A', edad=70, dia="miércoles")
        print(f"Reserva realizada con éxito. Precio: ${precio:.2f}")
    except Exception as e:
        print(f"Error: {e}")

    # Mostrar asientos después de la reserva
    print("\nAsientos después de la reserva:")
    sala.mostrar_asientos()

    # Cancelar reserva
    print("\nCancelando la reserva del asiento 1A...")
    try:
        sala.cancelar_reserva(1, 'A')
        print("Reserva cancelada con éxito.")
    except Exception as e:
        print(f"Error: {e}")

    # Mostrar asientos después de la cancelación
    print("\nAsientos después de cancelar la reserva:")
    sala.mostrar_asientos()


if __name__ == "__main__":
    main()
