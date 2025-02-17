![Banner Proyectos](https://github.com/user-attachments/assets/bc6e34f7-4031-43dd-8cfc-805c935ba3c4)

# 🚖 Taxímetro Digital - TaxiGo

¡Bienvenido a TaxiGo, tu taxímetro digital en Python! 🚖  
Con TaxiGo, puedes calcular el costo de un trayecto en taxi basado en el tiempo en movimiento y en parada.  
Ideal para conductores y pasajeros que desean conocer el costo estimado de un viaje en tiempo real.

---

## 📖 Índice  
- 🎮 Descripción 
- 🛠 Características 
- 📌 Cómo usar    
- 🔥 Posibles mejoras  
- 🛠 Instalación y ejecución 
- 🏆 Contribuciones  

---

## 🛠 Características  

✅ Cálculo en tiempo real del costo del trayecto.  
✅ Detección de estado del taxi mediante el teclado:  

- `m` para indicar movimiento.  
- `p` para indicar parada.  
- `f` para finalizar el trayecto.  

✅ Diferentes tarifas para movimiento y parada.  
✅ Registro del tiempo transcurrido y su costo asociado.  
✅ Interfaz de consola simple e intuitiva.  

---

## 📌 Cómo usar  

1. Ejecuta el programa desde la terminal.  
2. Presiona `m` cuando el taxi esté en movimiento.  
3. Presiona `p` cuando el taxi esté detenido.  
4. Presiona `f` para finalizar el trayecto y ver el total.  
5. Consulta el costo del trayecto en pantalla.  

## Ejemplo de salida
```bash
🚖 ¡Bienvenido a TaxiGo, tu taxímetro digital! 🚖
¿Desea iniciar un nuevo trayecto? (s/n): s
Trayecto iniciado. Presione 'm' cuando esté en movimiento, 'p' cuando esté parado y 'f' para finalizar el trayecto.
🟢 Calculando tarifa en movimiento...
⏱️ Duración: 10.00 segundos. 💰 Costo añadido: 0.50 €.
🔴 Calculando tarifa en parada...
⏱️ Duración: 5.00 segundos. 💰 Costo añadido: 0.10 €.
✅ Trayecto finalizado. Total a cobrar: 0.60 €.
```
---

## ⚠️ Problemas detectados  

🔹 No hay una interfaz gráfica: Todo funciona desde la terminal.  
🔹 No guarda historiales de trayectos.  
🔹 No permite configurar tarifas personalizadas.  
🔹 No detecta automáticamente el estado del vehículo.  

---

## 🔥 Posibles mejoras  

### 🟡 Nivel Medio  
- Implementar un sistema de logs para la trazabilidad del código.  
- Agregar tests unitarios para asegurar el correcto funcionamiento del programa.  
- Crear un registro histórico de trayectos pasados en un archivo de texto plano.  
- Permitir la configuración de precios para adaptarse a la demanda actual.  

### 🟠 Nivel Avanzado  
- Refactorizar el código utilizando un enfoque orientado a objetos (OOP).  
- Implementar un sistema de autenticación con contraseñas para proteger el acceso al programa.  
- Desarrollar una interfaz gráfica de usuario (GUI) para hacer el programa más amigable.  

### 🔴 Nivel Experto  
- Integrar una base de datos para almacenar los registros de trayectos pasados.  
- Dockerizar la aplicación para facilitar su despliegue y portabilidad.  
- Desarrollar una versión web de la aplicación accesible a través de internet.  

---

## 🛠 Instalación y ejecución  

Asegúrate de tener Python instalado en tu sistema.  
Si aún no lo tienes, descárgalo desde [python.org](https://www.python.org/downloads/).  

🔹 Creación de un entorno virtual

Se recomienda utilizar un entorno virtual para evitar conflictos con otras dependencias del sistema. Para crearlo y activarlo, ejecuta los siguientes comandos:

```sh
python -m venv env  # Crear el entorno virtual
source env/bin/activate  # Activar el entorno en Linux/Mac
env\Scripts\activate  # Activar el entorno en Windows
```

🔹 Instala las dependencias necesarias con:

Una vez activado el entorno virtual, instala las dependencias necesarias con:
```sh
pip install keyboard
```
🔹 Ejecutar el taxímetro

Finalmente, ejecuta el programa con:
```sh
python taximetro.py
```
## Requisitos
- Python 3.x
- Biblioteca `keyboard` (para capturar las teclas presionadas)

##  🏆 Gestión del proyecto con Scrum y Trello

TaxiGo se ha desarrollado siguiendo la metodología ágil Scrum, organizando tareas  y priorizando funcionalidades en un tablero de Trello. Esto nos ha permitido mejorar la productividad y la planificación del proyecto de manera eficiente. 

puedes revisar nuestro tablero de Trello en el siguiente enlace: [Enlace a Trello.](https://trello.com/invite/b/67a49c6dab53358e1ee7c410/ATTI91c91593a091a5dcda5cdc1f9da5181bAFCFE49C/taxigo-andreina-suescum). 

## 🏆 Contribuciones
¡Nos encantaría recibir sugerencias y mejoras! Si tienes ideas para mejorar el proyecto, abre un issue o envía un pull request en este repositorio.
📩 Contacto: [Github](https://github.com/mariasuescum). 


## Licencia
Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.

---
🚀 Desarrollado con ❤️ por Andreina Suescum

