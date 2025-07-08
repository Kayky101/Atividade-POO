import uuid
from datetime import datetime
from flight import Seat
from person import Passenger

class Booking:
    """Representa uma reserva de assento feita por um passageiro."""
    def __init__(self, passenger: Passenger, flight_id: str, seat: Seat):
        self._booking_id = uuid.uuid4()
        self._passenger = passenger
        self._flight_id = flight_id
        self._seat = seat
        self._booking_date = datetime.now()

    @property
    def booking_id(self):
        return self._booking_id

    @property
    def passenger(self) -> Passenger:
        return self._passenger

    @property
    def flight_id(self) -> str:
        return self._flight_id

    @property
    def seat(self) -> Seat:
        return self._seat

    def __repr__(self):
        return (f"Booking(ID: {self._booking_id}, Passenger: {self.passenger.name}, "
                f"Flight: {self.flight_id}, Seat: {self.seat.seat_number})")
