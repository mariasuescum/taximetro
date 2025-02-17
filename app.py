import time
import keyboard  

class Taximeter:
    def __init__(self):
        self.total = 0
        self.is_moving = False
        self.on_trip = False

    def start_trip(self):
        self.total = 0
        self.on_trip = True
        print("Trayecto iniciado. Presione 'm' cuando esté en movimiento, 'p' cuando esté parado y 'f' para finalizar el trayecto.")

        while self.on_trip:
            if keyboard.is_pressed('m'):
                print("🟢 Calculando tarifa en movimiento...")
                self.calculate_fare(0.05, mode='m')

            elif keyboard.is_pressed('p'):
                print("🔴 Calculando tarifa en parada...")
                self.calculate_fare(0.02, mode='p')

            elif keyboard.is_pressed('f'):
                self.finish_trip()
                return 

            time.sleep(0.1)  # Add a small delay to prevent high CPU usage

    def calculate_fare(self, fare_per_second, mode):
        start_time = time.time()

        calculate_cost = lambda duration, fare: duration * fare

        if mode == 'm':
            while not keyboard.is_pressed('p') and not keyboard.is_pressed('f'):
                time.sleep(0.1)
        elif mode == 'p':
            while not keyboard.is_pressed('m') and not keyboard.is_pressed('f'):
                time.sleep(0.1)

        end_time = time.time()
        duration = end_time - start_time
        cost = calculate_cost(duration, fare_per_second)
        self.total += cost
        print(f"⏱️ Duración: {duration:.2f} segundos. 💰 Costo añadido: {cost:.2f} €.")

    def finish_trip(self):
        self.on_trip = False
        print(f"✅ Trayecto finalizado. Total a cobrar: {self.total:.2f} €.")

def main():
    print("🚖 ¡Bienvenido a TaxiGo, tu taxímetro digital! 🚖")
    print("TaxiGo calcula el costo de tu trayecto según el tiempo en movimiento y cuando el taxi está detenido.")
    print("\n💡 ¿Cómo funciona?")
    print("- Si el taxi está en movimiento, el costo aumenta según el tiempo transcurrido.")
    print("- Si el taxi deja de moverse, el costo aumenta pero es más bajo.")
    print("- Presione 'm' para indicar movimiento, 'p' para indicar que está detenido y 'f' para finalizar el trayecto.")
    print("\n¡Vamos a empezar!\n")
    taximeter = Taximeter()
    while True:
        option = input("¿Desea iniciar un nuevo trayecto? (s/n): ").lower()
        if option == 's':
            taximeter.start_trip()
            break
        elif option == 'n':
            print("🚗💨 Gracias por usar Taxímetro Digital TaxiGo. ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida. Por favor ingrese 's' o 'n'.")

if __name__ == "__main__":
    main()