from enum import Enum, auto

class SeatStatus(Enum):
    """Enumeração para o status de um assento."""
    AVAILABLE = auto()
    BOOKED = auto()

class FlightStatus(Enum):
    """Enumeração para o status de um voo."""
    SCHEDULED = auto()
    DEPARTED = auto()
    ARRIVED = auto()
    CANCELLED = auto()

class CrewRole(Enum):
    """Enumeração para a função de um membro da tripulação."""
    PILOT = auto()
    COPILOT = auto()
    FLIGHT_ATTENDANT = auto()