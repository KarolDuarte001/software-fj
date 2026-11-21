"""
Reserva integra Cliente + Servicio + duración.
Transiciones permitidas:
    PENDIENTE -> CONFIRMADA -> PROCESADA
    PENDIENTE/CONFIRMADA -> CANCELADA
"""
from enum import Enum
from excepciones import (ReservaInvalidaError, OperacionNoPermitidaError)
from logger import log


class EstadoReserva(Enum):
    PENDIENTE  = "PENDIENTE"
    CONFIRMADA = "CONFIRMADA"
    CANCELADA  = "CANCELADA"
    PROCESADA  = "PROCESADA"


class Reserva:
    _contador = 1000

    def __init__(self, cliente, servicio, duracion, **opciones):
        self._id = Reserva._siguiente_id()
        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion
        self._estado = EstadoReserva.PENDIENTE
        self._opciones = opciones
        self._costo = None
        self._validar_creacion()

    @classmethod
    def _siguiente_id(cls):
        cls._contador += 1
        return f"RES-{cls._contador}"

    def _validar_creacion(self):
        if self._cliente is None or self._servicio is None:
            raise ReservaInvalidaError("Cliente y servicio son obligatorios.")
        if not isinstance(self._duracion, (int, float)) or self._duracion <= 0:
            raise ReservaInvalidaError(f"Duración inválida: {self._duracion}.")
        self._cliente.validar()   # puede lanzar ClienteInvalidoError
        self._servicio.validar()  # puede lanzar ServicioNoDisponibleError

    @property
    def id(self):     return self._id
    @property
    def estado(self): return self._estado
    @property
    def costo(self):  return self._costo

    def confirmar(self):
        if self._estado != EstadoReserva.PENDIENTE:
            raise OperacionNoPermitidaError(
                f"No se puede confirmar reserva en estado {self._estado.value}."
            )
        try:
            # Separamos opciones de cálculo de las específicas del servicio
            impuesto  = self._opciones.get("impuesto")
            descuento = self._opciones.get("descuento", 0.0)
            kwargs_servicio = {k: v for k, v in self._opciones.items()
                               if k not in ("impuesto", "descuento")}
            self._costo = self._servicio.calcular_costo_con_impuestos(
                self._duracion,
                impuesto=impuesto,
                descuento=descuento,
                **kwargs_servicio
            )
        except Exception as e:
            log.error(f"Error calculando costo reserva {self._id}: {e}")
            # Encadenamiento de excepciones
            raise ReservaInvalidaError(
                f"No se pudo calcular el costo: {e}"
            ) from e
        else:
            self._estado = EstadoReserva.CONFIRMADA
            log.info(f"Reserva {self._id} confirmada. Costo=${self._costo}")
            return self._costo
        finally:
            log.debug(f"Intento de confirmación finalizado para {self._id}")

    def cancelar(self, motivo="No especificado"):
        if self._estado == EstadoReserva.CANCELADA:
            raise OperacionNoPermitidaError("La reserva ya está cancelada.")
        if self._estado == EstadoReserva.PROCESADA:
            raise OperacionNoPermitidaError(
                "No se puede cancelar una reserva ya procesada."
            )
        self._estado = EstadoReserva.CANCELADA
        log.warning(f"Reserva {self._id} cancelada. Motivo: {motivo}")

    def procesar(self):
        if self._estado != EstadoReserva.CONFIRMADA:
            raise OperacionNoPermitidaError(
                f"Solo se procesan reservas CONFIRMADAS "
                f"(actual: {self._estado.value})."
            )
        self._estado = EstadoReserva.PROCESADA
        log.info(f"Reserva {self._id} procesada correctamente.")

    def describir(self):
        return (f"Reserva[{self._id}] cliente={self._cliente.nombre} "
                f"servicio={self._servicio.nombre} duración={self._duracion} "
                f"estado={self._estado.value} costo={self._costo}")

    def __str__(self):
        return self.describir()