import random
from datetime import datetime, timedelta

from flight import Flight
from person import Passenger, CrewMember
from enums import CrewRole
from exceptions.booking_exceptions import SeatAlreadyBookedError

def main():
    """Função principal para demonstrar o sistema de reserva de voos."""
    print("Bem-vindo ao Sistema de Reservas de Voo!")
    print("=" * 60)

    # 1. Criar Tripulantes (Funcionários) com nomes fixos por enquanto
    crew = [
        CrewMember(101, "Carlos Souza", CrewRole.PILOT),
        CrewMember(102, "Mariana Viana", CrewRole.COPILOT),
        CrewMember(201, "Ana Pereira", CrewRole.FLIGHT_ATTENDANT),
        CrewMember(202, "Bruno Lima", CrewRole.FLIGHT_ATTENDANT),
        CrewMember(203, "Clara Faria", CrewRole.FLIGHT_ATTENDANT),
        CrewMember(204, "Diego Martins", CrewRole.FLIGHT_ATTENDANT),
    ]
    print("Tripulação disponível para alocação criada.")

    # 2. Criar 10 Voos
    flights: list[Flight] = []
    origins_destinations = [("São Paulo", "Rio de Janeiro"), ("Belo Horizonte", "Salvador"), ("Porto Alegre", "Recife")]
    
    for i in range(10):
        flight_id = f"AD{4000 + i}"
        route = random.choice(origins_destinations)
        departure = datetime.now() + timedelta(days=i+1, hours=random.randint(1, 23))
        price = random.uniform(450.50, 2500.75)
        
        flight = Flight(flight_id, route[0], route[1], departure, price)
        
        # Associar tripulantes a um voo
        pilots = [m for m in crew if m.role == CrewRole.PILOT or m.role == CrewRole.COPILOT]
        attendants = [m for m in crew if m.role == CrewRole.FLIGHT_ATTENDANT]
        
        # Garante pelo menos 1 piloto e 2 comissários
        flight.add_crew_member(random.choice(pilots))
        for member in random.sample(attendants, k=2):
            flight.add_crew_member(member)

        flights.append(flight)
    
    print(f"\n{len(flights)} voos criados e programados com sucesso!")
    print("-" * 60)

if __name__ == "__main__":
    main()