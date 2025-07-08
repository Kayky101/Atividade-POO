class SeatAlreadyBookedError(Exception):
    """Exceção levantada ao tentar reservar um assento que já está ocupado."""
    def __init__(self, seat_number: str, flight_id: str):
        super().__init__(f"O assento '{seat_number}' no voo '{flight_id}' já está reservado.")

class InvalidSeatNumberError(Exception):
    """Exceção levantada quando um número de assento não existe no voo."""
    def __init__(self, seat_number: str, flight_id: str):
        super().__init__(f"O assento '{seat_number}' não existe no voo '{flight_id}'.")