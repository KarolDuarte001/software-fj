"""
Cliente con encapsulación estricta (properties con setters validantes).
Cualquier dato inválido lanza ClienteInvalidoError.
"""
import re
from entidad import Entidad
from excepciones import ClienteInvalidoError
from logger import log


class Cliente(Entidad):
    def __init__(self, identificador, nombre, email, telefono):
        super().__init__(identificador)
        self._nombre = None
        self._email = None
        self._telefono = None
        self._activo = True
        # Los setters validan al asignar
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    # ---------- nombre ----------
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or len(valor.strip()) < 3:
            raise ClienteInvalidoError(
                f"Nombre inválido: '{valor}'. Debe tener al menos 3 caracteres."
            )
        self._nombre = valor.strip()

    # ---------- email ----------
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not isinstance(valor, str) or not re.match(patron, valor):
            raise ClienteInvalidoError(f"Email inválido: '{valor}'.")
        self._email = valor.lower().strip()

    # ---------- teléfono ----------
    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        if not isinstance(valor, str) or not re.match(r'^\d{7,15}$', valor):
            raise ClienteInvalidoError(
                f"Teléfono inválido: '{valor}'. Debe tener 7 a 15 dígitos."
            )
        self._telefono = valor

    # ---------- estado ----------
    @property
    def activo(self):
        return self._activo

    def desactivar(self):
        self._activo = False
        log.info(f"Cliente {self._identificador} desactivado.")

    # ---------- abstractos implementados ----------
    def validar(self):
        if not self._activo:
            raise ClienteInvalidoError("El cliente no está activo.")
        return True

    def describir(self):
        return (f"Cliente[{self._identificador}] {self._nombre} "
                f"<{self._email}> tel:{self._telefono} activo:{self._activo}")

    def __str__(self):
        return self.describir()