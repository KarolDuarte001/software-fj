"""
Servicio abstracto. Incluye el método sobrecargado
'calcular_costo_con_impuestos' con parámetros opcionales
(impuesto, descuento) para simular sobrecarga en Python.
"""
from abc import ABC, abstractmethod
from entidad import Entidad
from excepciones import ValidacionError, ServicioNoDisponibleError


class Servicio(Entidad, ABC):
    IMPUESTO_DEFAULT = 0.19  # IVA Colombia

    def __init__(self, identificador, nombre, precio_base, disponible=True):
        super().__init__(identificador)
        if precio_base < 0:
            raise ValidacionError(f"Precio base inválido: {precio_base}")
        self._nombre = nombre
        self._precio_base = float(precio_base)
        self._disponible = disponible

    @property
    def nombre(self):       return self._nombre
    @property
    def precio_base(self):  return self._precio_base
    @property
    def disponible(self):   return self._disponible

    def validar(self):
        if not self._disponible:
            raise ServicioNoDisponibleError(
                f"Servicio '{self._nombre}' no está disponible."
            )
        if self._precio_base < 0:
            raise ValidacionError("Precio base no puede ser negativo.")
        return True

    @abstractmethod
    def calcular_costo(self, duracion, **kwargs):
        """Cada servicio concreto define su propia lógica (polimorfismo)."""
        pass

    @abstractmethod
    def describir(self):
        pass

    # ---- MÉTODO SOBRECARGADO (variantes por parámetros opcionales) ----
    def calcular_costo_con_impuestos(self, duracion, impuesto=None,
                                     descuento=0.0, **kwargs):
        """
        Variante con impuestos/descuento. Los kwargs se reenvían a
        calcular_costo (ej: personas, seguro, nivel).
        """
        if impuesto is None:
            impuesto = self.IMPUESTO_DEFAULT
        subtotal = self.calcular_costo(duracion, **kwargs)
        total = subtotal * (1 + impuesto) * (1 - descuento)
        if total < 0:
            raise ValidacionError("El total calculado no puede ser negativo.")
        return round(total, 2)

    def __str__(self):
        return f"Servicio[{self._identificador}] {self._nombre} ${self._precio_base}"