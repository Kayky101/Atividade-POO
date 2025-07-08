from datetime import datetime
from enums import SeatStatus, FlightStatus
from person import Passenger, CrewMember
from exceptions.booking_exceptions import SeatAlreadyBookedError, InvalidSeatNumberError
from exceptions.flight_exceptions import NoAvailableSeatsError

class Seat:
    """Representa um assento individual em um voo."""
    def __init__(self, seat_number: str):
        self._seat_number = seat_number
        self._status = SeatStatus.AVAILABLE
        self._passenger: Passenger | None = None

    @property
    def seat_number(self) -> str:
        return self._seat_number

    @property
    def status(self) -> SeatStatus:
        return self._status

    @property
    def passenger(self) -> Passenger | None:
        return self._passenger

    def book(self, passenger: Passenger):
        """Reserva o assento para um passageiro."""
        if self._status == SeatStatus.BOOKED:
            raise SeatAlreadyBookedError(self.seat_number, "N/A")
        self._status = SeatStatus.BOOKED
        self._passenger = passenger

    def __repr__(self):
        return f"Seat({self.seat_number}, Status: {self.status.name})"

class Flight:
    """Representa um voo no sistema de reservas."""
    _SEAT_ROWS = 42
    _SEAT_LETTERS = "ABCDEF"

    def __init__(self, flight_id: str, origin: str, destination: str, departure_time: datetime, price: float):
        self._flight_id = flight_id
        self._origin = origin
        self._destination = destination
        self._departure_time = departure_time
        self._price = price
        self._status = FlightStatus.SCHEDULED
        self._seats = self._initialize_seats()
        self._crew: list[CrewMember] = [] # Adicionado, mas a lógica de uso virá depois

    def _initialize_seats(self) -> dict[str, Seat]:
        """Cria os 252 assentos para o voo."""
        seats = {}
        for row in range(1, self._SEAT_ROWS + 1):
            for letter in self._SEAT_LETTERS:
                seat_number = f"{row}{letter}"
                seats[seat_number] = Seat(seat_number)
        return seats

    @property
    def flight_id(self) -> str:
        return self._flight_id

    @property
    def origin(self) -> str:
        return self._origin

    @property
    def destination(self) -> str:
        return self._destination

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("O preço deve ser um número não negativo.")
        self._price = float(value)

    def __repr__(self) -> str:
        return (f"Flight(ID: {self.flight_id}, From: {self.origin}, To: {self.destination}, "
                f"Price: R${self.price:.2f})")