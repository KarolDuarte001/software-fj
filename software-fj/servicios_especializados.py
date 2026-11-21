"""
Tres servicios especializados que heredan de Servicio.
Cada uno sobrescribe calcular_costo y describir (polimorfismo).
"""
from servicio import Servicio
from excepciones import ValidacionError, ParametroFaltanteError


class ReservaSala(Servicio):
    def __init__(self, identificador, nombre, precio_base, capacidad, disponible=True):
        super().__init__(identificador, nombre, precio_base, disponible)
        if capacidad <= 0:
            raise ValidacionError("La capacidad debe ser positiva.")
        self._capacidad = capacidad

    @property
    def capacidad(self): return self._capacidad

    def calcular_costo(self, duracion, personas=1):
        if duracion <= 0:
            raise ValidacionError("La duración debe ser positiva.")
        if personas > self._capacidad:
            raise ValidacionError(
                f"Personas ({personas}) excede la capacidad ({self._capacidad})."
            )
        costo = self._precio_base * duracion
        # Recargo si la ocupación supera 80%
        if personas > self._capacidad * 0.8:
            costo *= 1.10
        return round(costo, 2)

    def describir(self):
        return (f"ReservaSala[{self._identificador}] '{self._nombre}' "
                f"capacidad={self._capacidad} precio/hora=${self._precio_base} "
                f"disponible={self._disponible}")


class AlquilerEquipo(Servicio):
    def __init__(self, identificador, nombre, precio_base, tipo_equipo, disponible=True):
        super().__init__(identificador, nombre, precio_base, disponible)
        if not tipo_equipo:
            raise ParametroFaltanteError("'tipo_equipo' es obligatorio.")
        self._tipo_equipo = tipo_equipo

    @property
    def tipo_equipo(self): return self._tipo_equipo

    def calcular_costo(self, duracion, seguro=False):
        if duracion <= 0:
            raise ValidacionError("La duración debe ser positiva.")
        costo = self._precio_base * duracion
        if seguro:
            costo *= 1.15
        return round(costo, 2)

    def describir(self):
        return (f"AlquilerEquipo[{self._identificador}] '{self._nombre}' "
                f"tipo={self._tipo_equipo} precio/día=${self._precio_base} "
                f"disponible={self._disponible}")


class AsesoriaEspecializada(Servicio):
    MULTIPLICADORES = {"basico": 1.0, "intermedio": 1.3, "avanzado": 1.6}

    def __init__(self, identificador, nombre, precio_base, especialista, disponible=True):
        super().__init__(identificador, nombre, precio_base, disponible)
        if not especialista:
            raise ParametroFaltanteError("'especialista' es obligatorio.")
        self._especialista = especialista

    @property
    def especialista(self): return self._especialista

    def calcular_costo(self, duracion, nivel="basico"):
        if duracion <= 0:
            raise ValidacionError("La duración debe ser positiva.")
        if nivel not in self.MULTIPLICADORES:
            raise ValidacionError(f"Nivel inválido: '{nivel}'.")
        return round(self._precio_base * duracion *
                     self.MULTIPLICADORES[nivel], 2)

    def describir(self):
        return (f"AsesoriaEspecializada[{self._identificador}] '{self._nombre}' "
                f"especialista={self._especialista} precio/hora=${self._precio_base} "
                f"disponible={self._disponible}")