from datetime import date
from typing import List, Optional

class Cliente:
    def __init__(self, nombre_completo: str, telefono: str, correo: str, direccion: str):
        self.__nombre_completo = nombre_completo
        self.__telefono = telefono
        self.__correo = correo
        self.__direccion = direccion
        
    # Métodos para cumplir requerimientos
    def buscar_habitacion(self, tipo: str, calendario: 'Calendario') -> List['Habitacion']:
        return [hab for hab in self.__habitaciones if hab.tipo == tipo and calendario.consultar_disponibilidad(hab)]

    def realizar_reserva(self, habitacion: 'Habitacion', fecha_inicio: date, fecha_fin: date) -> 'Reserva':
        """Requerimiento: Crear una reserva."""
        return Reserva(fecha_inicio, fecha_fin, "Pendiente", habitacion)

    def calificar_estadia(self, comentario: 'Comentario') -> None:
        """Requerimiento: Calificar la estadía."""
        pass

class Reserva:
    def __init__(self, fecha_inicio: date, fecha_fin: date, estado: str, habitacion: 'Habitacion'):
        self.__fecha_inicio = fecha_inicio
        self.__fecha_fin = fecha_fin
        self.__estado = estado
        self.__habitacion = habitacion

    # Métodos para cumplir requerimientos
    def realizar_pago(self) -> None:
        """Requerimiento: Procesar pago."""
        self.__estado = "Pagada"

    def cancelar_reserva(self) -> None:
        """Requerimiento: Cancelar reserva."""
        self.__estado = "Cancelada"

    def get_estado(self) -> str:
        return self.__estado
    
class Habitacion:
    def __init__(self, tipo: str, descripcion: str, precio: float, capacidad: int, estado: str):
        self.__tipo = tipo
        self.__descripcion = descripcion
        self.__precio = precio
        self.__servicios_incluidos: List[str] = []
        self.__capacidad = capacidad
        self.__fotos: List[str] = []
        self.__estado = estado

        # Métodos para cumplir requerimientos
    def consultar_disponibilidad(self, calendario: 'Calendario') -> bool:
        """Requerimiento: Verificar disponibilidad en fechas."""
        pass

class Calendario:
    def __init__(self):
        self.__fechas_ocupadas: List[date] = []

    # Métodos para cumplir requerimientos
    def consultar_disponibilidad(self, fecha: date) -> bool:
        """Requerimiento: Consultar fechas ocupadas."""
        return fecha not in self.__fechas_ocupadas

class Hotel:
    def __init__(self, nombre: str, direccion: str, telefono: str, correo: str, ubicacion: str):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__correo = correo
        self.__ubicacion = ubicacion
        self.__descripcion: Optional[str] = None
        self.__fotos: List[str] = []
        self.__habitaciones: List[Habitacion] = []

        # Métodos para cumplir requerimientos
    def registrar_oferta(self, descripcion: str) -> None:
        """Requerimiento: Registrar ofertas."""
        self.__descripcion = descripcion

    def calcular_calificacion_promedio(self, comentarios: List['Comentario']) -> float:
        """Requerimiento: Calcular calificación promedio."""
        return sum(c.calificacion for c in comentarios) / len(comentarios)

class Comentario:
    def __init__(self, autor: str, contenido: str, calificacion: int):
        self.__autor = autor
        self.__contenido = contenido
        self.__calificacion = calificacion

# Crear objetos
hotel = Hotel("Hotel nueva vista", "Calle 123", "555-456", "hotel@gmail.com", "Cali")
habitacion = Habitacion("Habitacion una cama", "Habitación con cama doble", 150.0, 2, "Activa")
cliente = Cliente("Lorena Q", "555-458", "loreq@gmail.com", "Calle 78")

# Simular reserva
reserva = cliente.realizar_reserva(habitacion, date(2024, 6, 1), date(2024, 6, 5))
reserva.realizar_pago()
print(f"\033[1mReserva estado: {reserva.get_estado()}\033[0m")
