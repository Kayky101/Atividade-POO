from datetime import datetime
from enums import SeatStatus, FlightStatus
from person import Passenger, CrewMember
from exceptions.booking_exceptions import SeatAlreadyBookedError, InvalidSeatNumberError
from exceptions.flight_exceptions import NoAvailableSeatsError
# A importação da classe Booking foi movida para dentro do método para evitar dependência circular
# from booking import Booking

class Seat:
    # ... (código da classe Seat permanece o mesmo) ...
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
    # ... (código do __init__ e propriedades permanece o mesmo até add_crew_member) ...
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
        self._crew: list[CrewMember] = []

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

    @property
    def crew(self) -> list[CrewMember]:
        return self._crew

    def add_crew_member(self, member: CrewMember):
        """Adiciona um membro da tripulação ao voo."""
        if not isinstance(member, CrewMember):
            raise TypeError("O membro deve ser uma instância de CrewMember.")
        self._crew.append(member)

    def get_available_seats(self) -> list[Seat]:
        """Retorna uma lista de todos os assentos disponíveis."""
        return [seat for seat in self._seats.values() if seat.status == SeatStatus.AVAILABLE]

    def book_seat(self, seat_number: str, passenger: Passenger):
        """
        Associa um cliente a um voo e um lugar.
        """
        if seat_number not in self._seats:
            raise InvalidSeatNumberError(seat_number, self.flight_id)

        seat = self._seats[seat_number]
        if seat.status == SeatStatus.BOOKED:
            raise SeatAlreadyBookedError(seat_number, self.flight_id)

        seat.book(passenger)
        
        # Importação local para evitar dependência circular
        from booking import Booking
        new_booking = Booking(passenger, self.flight_id, seat)
        return new_booking

    def __repr__(self) -> str:
        return (f"Flight(ID: {self.flight_id}, From: {self.origin}, To: {self.destination}, "
                f"Price: R${self.price:.2f})")