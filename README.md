# TaxiGo - Taxímetro Digital 🚖

## Descripción
TaxiGo es una aplicación de taxímetro digital desarrollada en Python que permite calcular el costo de un trayecto en taxi basado en el tiempo transcurrido en movimiento y en parada.

## Características
✅ Calcula tarifas en tiempo real según el estado del taxi (movimiento o parada).  
✅ Interfaz en consola con interacción mediante el teclado.  
✅ Tarifas ajustables según el tiempo en cada estado.  
✅ Mensajes en tiempo real sobre el estado del trayecto.  

## Instalación
1. Clona este repositorio o descarga los archivos.
   ```bash
   git clone https://github.com/tuusuario/taxigo.git
   cd taxigo
   ```
2. Instala las dependencias necesarias (asegúrate de tener Python instalado).
   ```bash
   pip install keyboard
   ```

## Uso
Ejecuta el script principal:
```bash
python taximetro.py
```

### Controles
- **`m`** → Indica que el taxi está en movimiento.
- **`p`** → Indica que el taxi está detenido.
- **`f`** → Finaliza el trayecto y muestra el costo total.

## Funcionamiento
1. Al iniciar el programa, se pregunta si deseas iniciar un nuevo trayecto.
2. Durante el trayecto:
   - Presiona `m` para calcular la tarifa de movimiento.
   - Presiona `p` para calcular la tarifa de parada.
   - Presiona `f` para finalizar y ver el costo total.
3. El programa muestra el costo acumulado según la duración en cada estado.

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

## Requisitos
- Python 3.x
- Biblioteca `keyboard` (para capturar las teclas presionadas)

## Contribuciones
¡Las contribuciones son bienvenidas! Si deseas mejorar el proyecto, por favor abre un issue o envía un pull request.

## Licencia
Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.

---
🚀 Desarrollado con ❤️ por Andreina Suescum

