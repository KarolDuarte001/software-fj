"""
Demo del sistema Software FJ con 15 operaciones:
    - registros válidos e inválidos
    - creación correcta e incorrecta de servicios
    - reservas exitosas y fallidas
    - encadenamiento de excepciones
    - cálculos sobrecargados con impuestos/descuento
El programa NUNCA se detiene: cada operación está aislada con try/except.
"""
from excepciones import *
from logger import log
from cliente import Cliente
from servicios_especializados import (
    ReservaSala, AlquilerEquipo, AsesoriaEspecializada
)
from reserva import Reserva, EstadoReserva


def titulo(t):
    print(f"\n{'='*72}\n{t}\n{'='*72}")


def demo():
    log.info("=== INICIO DEMO SOFTWARE FJ ===")
    clientes, servicios, reservas = [], [], []
    ok, fallos = 0, 0

    # OP 1 — Cliente válido
    titulo("OP 1 | Registro cliente válido")
    try:
        c1 = Cliente("C001", "Juan Pérez", "juan@mail.com", "3001234567")
        clientes.append(c1)
        print(f"✅ {c1}")
        ok += 1
        log.info(f"Cliente creado: {c1}")
    except Exception as e:
        print(f"❌ {e}"); log.error(str(e)); fallos += 1

    # OP 2 — Cliente con email inválido
    titulo("OP 2 | Cliente con email inválido")
    try:
        c_bad = Cliente("C002", "Bad Email", "no-es-email", "3001234567")
        clientes.append(c_bad); print(f"✅ {c_bad}"); ok += 1
    except ClienteInvalidoError as e:
        print(f"⚠️  Rechazado: {e}"); log.warning(str(e)); fallos += 1

    # OP 3 — Cliente con nombre corto
    titulo("OP 3 | Cliente con nombre demasiado corto")
    try:
        c_bad = Cliente("C003", "AB", "ab@mail.com", "3001234567")
        clientes.append(c_bad); print(f"✅ {c_bad}"); ok += 1
    except ClienteInvalidoError as e:
        print(f"⚠️  Rechazado: {e}"); log.warning(str(e)); fallos += 1

    # OP 4 — Crear 3 servicios válidos (distintos tipos)
    titulo("OP 4 | Crear 3 servicios válidos")
    try:
        s1 = ReservaSala("S001", "Sala Conferencias", 50000, capacidad=20)
        s2 = AlquilerEquipo("S002", "Proyector HD", 30000, tipo_equipo="Proyector")
        s3 = AsesoriaEspecializada("S003", "Asesoría Legal", 80000,
                                   especialista="Dr. Ruiz")
        servicios.extend([s1, s2, s3])
        for s in servicios:
            print(f"✅ {s.describir()}")
        ok += 1
        log.info("3 servicios creados correctamente.")
    except Exception as e:
        print(f"❌ {e}"); log.error(str(e)); fallos += 1

    # OP 5 — Servicio inválido (precio negativo)
    titulo("OP 5 | Servicio con precio negativo")
    try:
        s_bad = ReservaSala("S_BAD", "Sala Mala", -100, capacidad=10)
        servicios.append(s_bad); print(f"✅ {s_bad}"); ok += 1
    except ValidacionError as e:
        print(f"⚠️  Rechazado: {e}"); log.warning(str(e)); fallos += 1

    # OP 6 — Servicio inválido (sin especialista)
    titulo("OP 6 | Asesoría sin especialista")
    try:
        s_bad = AsesoriaEspecializada("S_BAD2", "Asesoría X", 50000,
                                      especialista="")
        servicios.append(s_bad); print(f"✅ {s_bad}"); ok += 1
    except ParametroFaltanteError as e:
        print(f"⚠️  Rechazado: {e}"); log.warning(str(e)); fallos += 1

    # OP 7 — Reserva exitosa (confirmar + procesar)
    titulo("OP 7 | Reserva exitosa (confirmar + procesar)")
    try:
        r1 = Reserva(clientes[0], servicios[0], duracion=3,
                     impuesto=0.19, personas=10)
        reservas.append(r1)
        r1.confirmar()
        r1.procesar()
        print(f"✅ {r1.describir()}")
        ok += 1
    except Exception as e:
        print(f"❌ {e}"); log.error(str(e)); fallos += 1

    # OP 8 — Reserva con duración negativa
    titulo("OP 8 | Reserva con duración negativa")
    try:
        r_bad = Reserva(clientes[0], servicios[1], duracion=-2)
        reservas.append(r_bad); print(f"✅ {r_bad.describir()}"); ok += 1
    except ReservaInvalidaError as e:
        print(f"⚠️  Rechazado: {e}"); log.warning(str(e)); fallos += 1

    # OP 9 — Sala excede capacidad (error al confirmar)
    titulo("OP 9 | Sala excede capacidad")
    try:
        r2 = Reserva(clientes[0], servicios[0], duracion=2, personas=50)
        reservas.append(r2)
        r2.confirmar()
        print(f"✅ {r2.describir()}"); ok += 1
    except ReservaInvalidaError as e:
        print(f"⚠️  Rechazado: {e}"); log.warning(str(e)); fallos += 1

    # OP 10 — Cancelar reserva ya procesada (operación no permitida)
    titulo("OP 10 | Cancelar reserva ya procesada")
    try:
        reservas[0].cancelar("intento tardío")
        print("✅ cancelada"); ok += 1
    except OperacionNoPermitidaError as e:
        print(f"⚠️  Rechazado correctamente: {e}")
        log.warning(str(e)); fallos += 1

    # OP 11 — Servicio no disponible
    titulo("OP 11 | Reserva con servicio no disponible")
    try:
        s_no = AlquilerEquipo("S_NO", "Equipo roto", 1000,
                              tipo_equipo="X", disponible=False)
        r3 = Reserva(clientes[0], s_no, duracion=1)
        print(f"✅ {r3.describir()}"); ok += 1
    except ServicioNoDisponibleError as e:
        print(f"⚠️  Rechazado: {e}"); log.warning(str(e)); fallos += 1
    except Exception as e:
        print(f"⚠️  Rechazado: {e}"); log.warning(str(e)); fallos += 1

    # OP 12 — Encadenamiento de excepciones
    titulo("OP 12 | Encadenamiento de excepciones")
    try:
        try:
            raise ValidacionError("Falla interna simulada")
        except ValidacionError as inner:
            raise ReservaInvalidaError("Falla externa tras interna") from inner
    except ReservaInvalidaError as e:
        print(f"⚠️  Encadenada: {e} | Causa: {e.__cause__}")
        log.error(f"Excepción encadenada: {e}"); fallos += 1

    # OP 13 — Cálculo con descuento (método sobrecargado)
    titulo("OP 13 | Cálculo con descuento (método sobrecargado)")
    try:
        total = servicios[2].calcular_costo_con_impuestos(
            duracion=2, impuesto=0.19, descuento=0.10, nivel="avanzado"
        )
        print(f"✅ Costo final con descuento: ${total}")
        ok += 1
    except Exception as e:
        print(f"❌ {e}"); fallos += 1

    # OP 14 — Nivel inválido en asesoría
    titulo("OP 14 | Asesoría con nivel inválido")
    try:
        servicios[2].calcular_costo(2, nivel="ultra-mega")
        print("✅ calculado"); ok += 1
    except ValidacionError as e:
        print(f"⚠️  Rechazado: {e}"); log.warning(str(e)); fallos += 1

    # OP 15 — Estado final de todas las reservas
    titulo("OP 15 | Estado final de reservas")
    for r in reservas:
        print(f"   {r.describir()}")

    titulo(f"RESUMEN | {ok} exitosas | {fallos} controladas/rechazadas")
    log.info(f"=== FIN DEMO: {ok} exitosas, {fallos} controladas ===")


if __name__ == "__main__":
    demo()