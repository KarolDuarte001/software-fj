
# Software FJ
### Plataforma de administración de clientes, servicios y reservas

Software FJ es una solución desarrollada en Python para organizar y controlar las operaciones de una empresa dedicada a la prestación de servicios.

A través de una estructura orientada a objetos, el sistema permite relacionar clientes, diferentes modalidades de servicio y sus respectivas reservas, manteniendo separadas las responsabilidades de cada componente.

---

**UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA (UNAD)**

**Curso:** Programación (213023)

**Grupo:** 213023_553

**Estudiante:** Karol Daniela Duarte Centeno

*(Desarrollado de forma **individual**)*

---

## ¿Qué puedes gestionar?

El sistema reúne tres áreas principales de operación:

| Área | Descripción |
|---|---|
| Clientes | Registro, consulta y validación de información. |
| Servicios | Administración de salas, alquiler de equipos y asesorías especializadas. |
| Reservas | Creación, confirmación, procesamiento y cancelación de solicitudes. |

Cada servicio cuenta con características y comportamientos propios, permitiendo adaptar sus operaciones según la modalidad contratada.

## Dentro del sistema

El proyecto está construido mediante módulos que trabajan conjuntamente:

- **`cliente.py`** — Maneja la información y las operaciones relacionadas con los clientes.
- **`entidad.py`** — Establece la estructura general de las entidades.
- **`servicio.py`** — Define el modelo base para los servicios disponibles.
- **`servicios_especializados.py`** — Contiene las implementaciones particulares de cada modalidad de servicio.
- **`reserva.py`** — Coordina la relación entre clientes, servicios y estados de reserva.
- **`excepciones.py`** — Reúne los mecanismos personalizados para controlar errores.
- **`logger.py`** — Gestiona el registro de acontecimientos y errores.
- **`main.py`** — Coordina la ejecución principal de la aplicación.

## Diseño y funcionamiento

Uno de los aspectos centrales de Software FJ es la aplicación de la Programación Orientada a Objetos.

Su estructura incorpora:

- Clases abstractas para establecer modelos generales.
- Herencia para especializar los componentes del sistema.
- Encapsulación para proteger y validar la información.
- Polimorfismo para adaptar el comportamiento de los servicios.
- Variantes de métodos para realizar operaciones y cálculos.
- Excepciones personalizadas para controlar situaciones inesperadas.

### Control de errores

La aplicación contempla diferentes mecanismos para detectar y gestionar errores durante su funcionamiento, utilizando bloques `try`, `except`, `else` y `finally`, así como encadenamiento de excepciones.

Los eventos relevantes y los errores detectados pueden consultarse mediante el registro de logs, facilitando el seguimiento de la ejecución.

## ¿Cómo se maneja la información?

Software FJ no utiliza bases de datos.

Los objetos y las listas internas permiten administrar la información durante la ejecución del programa. Los archivos se destinan al registro de eventos y errores, no al almacenamiento de una base de datos.

## Puesta en marcha

**Requisitos previos**

- Python 3.10 o superior.
- Terminal o consola de comandos.

**Ejecución**

Desde la carpeta principal que contiene `main.py`, ejecuta:

```bash
python main.py
```

## Entorno de desarrollo

| Herramienta | Utilización |
|---|---|
| Python | Desarrollo de la aplicación. |
| Visual Studio Code | Edición y organización del código. |
| Git | Control de versiones. |
| GitHub | Repositorio y documentación del proyecto. |

---

*Software FJ — Gestión organizada, componentes independientes y control de operaciones.*
