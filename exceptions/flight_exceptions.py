class FlightNotFoundError(Exception):
    """Exceção levantada quando um voo específico não é encontrado."""
    def __init__(self, flight_id: str):
        super().__init__(f"O voo com ID '{flight_id}' não foi encontrado.")

class NoAvailableSeatsError(Exception):
    """Exceção levantada quando não há mais assentos disponíveis em um voo."""
    def __init__(self, flight_id: str):
        super().__init__(f"Não há mais assentos disponíveis no voo '{flight_id}'.")