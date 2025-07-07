from abc import ABC, abstractmethod

class IPerson(ABC):
    """Define uma interface para uma pessoa no sistema."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Retorna o nome da pessoa."""
        pass

    @name.setter
    @abstractmethod
    def name(self, value: str):
        """Define o nome da pessoa."""
        pass
