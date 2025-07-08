from interfaces import IPerson
from enums import CrewRole

class Person(IPerson):
    """
    Classe base que representa uma pessoa no sistema.
    Implementa a interface IPerson.
    """
    def __init__(self, person_id: int, name: str):
        self._person_id = person_id
        self._name = name

    @property
    def person_id(self) -> int:
        return self._person_id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("O nome não pode ser vazio.")
        self._name = value.strip()

class Passenger(Person):
    """Representa um passageiro."""
    def __init__(self, person_id: int, name: str, passport_number: str):
        super().__init__(person_id, name)
        self._passport_number = passport_number

    @property
    def passport_number(self) -> str:
        return self._passport_number

    def __repr__(self) -> str:
        return f"Passenger(ID: {self.person_id}, Name: {self.name})"

class CrewMember(Person):
    """Representa um membro da tripulação."""
    def __init__(self, person_id: int, name: str, role: CrewRole):
        super().__init__(person_id, name)
        self._role = role

    @property
    def role(self) -> CrewRole:
        return self._role

    def __repr__(self) -> str:
        return f"CrewMember(Name: {self.name}, Role: {self.role.name})"
