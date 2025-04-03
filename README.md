# Lorena Quiñones Rodriguez
- [@lorena quiñones](https://www.github.com/estudiante)
  
##Sistema de Reservas de Hotel

###Descripción
Este proyecto implementa un sistema de reservas de hotel utilizando Python. y principios de Programación Orientada a Objetos (POO) . Permite la gestión de clientes, habitaciones, reservas y comentarios de usuarios.

#Características principales
- Gestión de clientes : Registro de clientes y búsqueda de habitaciones.
- Reserva de habitaciones : Creación y cancelación de reservas.
- Gestión de hoteles : Manejo de información de hoteles y sus habitaciones.
- Comentarios y calificaciones : Los clientes pueden calificar su estadía.


## Documentación

Revisar la documentación en [`./docs`](./docs)

### Requerimientos

- R1. El sistema debe permitir el registro de hoteles con los siguientes datos: 
    nombre, dirección, teléfono, correo electrónico, ubicación geográfica, 
    descripción detallada de servicios (restaurante, piscina, gimnasio), y fotos. 
- R2. El sistema debe registrar promociones y ofertas especiales por hotel, 
  como descuentos en temporadas específicas o paquetes especiales. 
- R3. El sistema debe registrar las habitaciones de cada hotel con 
    información detallada: tipo de habitación, descripción, precio, servicios 
    incluidos, capacidad máxima y fotos. 
- R4. El sistema debe permitir el registro de condiciones de pago y 
      cancelación para cada hotel, como pago anticipado o al llegar, y políticas de 
      cancelación específicas. 
- R5. El sistema debe manejar el estado de actividad de los hoteles y 
habitaciones (activo, inactivo por mantenimiento, remodelación o limpieza). 
• R6. El sistema debe proporcionar calendarios detallados para cada 
habitación, indicando las fechas en las que está reservada y las fechas 
disponibles. 
• R7. El sistema debe calcular y mostrar automáticamente la calificación 
promedio de cada habitación y de cada hotel, basándose en las 
evaluaciones de los clientes. 
• R8. El sistema debe solicitar la siguiente información al cliente al momento 
de registrarse: nombre completo, número de teléfono, correo electrónico y 
dirección. 
• R9. El sistema debe implementar una función de búsqueda de habitaciones 
por varios criterios: fecha, ubicación, calificación, precio y combinación de 
estos. 
• R10. El sistema debe permitir al cliente acceder a los detalles completos de 
una habitación antes de reservarla, incluyendo descripción, servicios, fotos, 
calificación y comentarios de otros huéspedes. 
• R11. El sistema debe formalizar la reserva de una habitación una vez que el 
cliente haya confirmado su selección y realizado el pago correspondiente. 
• R12. El sistema debe enviar notificaciones automáticas a los clientes por 
correo electrónico o SMS, recordando fechas de reservas, confirmaciones 
de pago y estados de las habitaciones. 
• R13. El sistema debe garantizar la seguridad de los datos personales de 
clientes y hoteles. 
• R14. El sistema debe ser escalable para manejar un aumento en el número 
de clientes, hoteles y habitaciones. 
• R15. El sistema debe incluir un módulo para gestionar sugerencias y 
comentarios de clientes, permitiendo mejoras continuas.

### Diseño

![Diagrama de Clases](./docs/diagramas.png)


## Instalación

Morbi quam lectus, tempus sit amet mi non, facilisis dignissim erat. Aenean tortor libero, rhoncus eu eleifend ut, volutpat id nisi. Ut porta eros at ante rutrum pharetra. Integer nec nulla dictum, vestibulum ligula id, hendrerit ex. Morbi eget tortor metus.

1. Clonar el proyecto
```bash
git clone https://github.com/UR-CC/lpa1-taller-requerimientos.git
```

2. Crear y activar entorno virtual
```bash
cd lpa1-taller-requerimientos
python -m venv venv
venv/bin/activate
```

3. Instalar librerías y dependencias
```bash
pip install -r requirements.txt
```
    
## Ejecución

Maecenas sed lorem at arcu varius mollis. Sed eleifend nulla ut blandit interdum. Donec sollicitudin nunc at orci facilisis dignissim. Donec at arcu luctus, commodo magna eget, blandit leo.

1. Ejecutar el proyecto
```bash
cd lpa1-taller-requerimientos
python app.py
```
