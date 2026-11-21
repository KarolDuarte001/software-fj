"""
Logger centralizado tipo Singleton. Todos los errores y eventos
relevantes se escriben en logs/sistema.log.
"""
import logging
import os

class SistemaLogger:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._configurar()
        return cls._instancia

    def _configurar(self):
        os.makedirs("logs", exist_ok=True)
        self.logger = logging.getLogger("SoftwareFJ")
        self.logger.setLevel(logging.DEBUG)

        if not self.logger.handlers:
            fh = logging.FileHandler("logs/sistema.log", encoding="utf-8")
            fh.setLevel(logging.DEBUG)
            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)-8s | %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S"
            )
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)

    def info(self, m):     self.logger.info(m)
    def warning(self, m):  self.logger.warning(m)
    def error(self, m):    self.logger.error(m)
    def debug(self, m):    self.logger.debug(m)
    def critical(self, m): self.logger.critical(m)


log = SistemaLogger()   # instancia global lista para usar