"""
Clase abstracta 'Entidad' de la que heredan todas las entidades del sistema.
Cumple el principio de abstracción.
"""
from abc import ABC, abstractmethod

class Entidad(ABC):
    def __init__(self, identificador):
        if not identificador:
            raise ValueError("El identificador es obligatorio.")
        self._identificador = identificador

    @property
    def identificador(self):
        return self._identificador

    @abstractmethod
    def describir(self):
        """Devuelve una descripción textual legible de la entidad."""
        pass

    @abstractmethod
    def validar(self):
        """Valida la consistencia interna. Lanza excepción si falla."""
        pass