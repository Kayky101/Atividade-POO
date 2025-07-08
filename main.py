import random
from datetime import datetime, timedelta
from faker import Faker  

from flight import Flight
from person import Passenger, CrewMember
from enums import CrewRole
from exceptions.booking_exceptions import SeatAlreadyBookedError

def main():
    """Função principal para demonstrar o sistema de reserva de voos."""
    print("Bem-vindo ao Sistema de Reservas de Voo!")
    print("=" * 60)

    # Inicializa o Faker para gerar dados em português do Brasil
    faker = Faker('pt_BR')

    # 1. Criar Tripulantes (Funcionários) usando Faker
    crew = [
        CrewMember(101, faker.name(), CrewRole.PILOT),
        CrewMember(102, faker.name(), CrewRole.COPILOT),
        CrewMember(201, faker.name(), CrewRole.FLIGHT_ATTENDANT),
        CrewMember(202, faker.name(), CrewRole.FLIGHT_ATTENDANT),
        CrewMember(203, faker.name(), CrewRole.FLIGHT_ATTENDANT),
        CrewMember(204, faker.name(), CrewRole.FLIGHT_ATTENDANT),
    ]
    print("Tripulação com nomes realistas criada.")

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
        
        flight.add_crew_member(random.choice(pilots))
        for member in random.sample(attendants, k=2):
            flight.add_crew_member(member)

        flights.append(flight)
    
    print(f"\n{len(flights)} voos criados e programados com sucesso!")
    print("-" * 60)

if __name__ == "__main__":
    main()
