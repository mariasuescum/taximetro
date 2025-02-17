import time
import keyboard  

class Taximetro:
    def __init__(self):
        self.total = 0
        self.en_movimiento = False
        self.en_trayecto = False

    def iniciar_trayecto(self):
        self.total = 0
        self.en_trayecto = True
        print("Trayecto iniciado. Presione 'm' cuando esté en movimiento, 'p' cuando esté parado y 'f' para finalizar el trayecto.")

        while self.en_trayecto:
            if keyboard.is_pressed('m'):
                print("🟢 Calculando tarifa en movimiento...")
                self.calcular_tarifa(0.05, modo='m')

            elif keyboard.is_pressed('p'):
                print("🔴 Calculando tarifa en parada...")
                self.calcular_tarifa(0.02, modo='p')

            elif keyboard.is_pressed('f'):
                self.finalizar_trayecto()
                return 

            time.sleep(0.1)  # Add a small delay to prevent high CPU usage

    def calcular_tarifa(self, tarifa_por_segundo, modo):
        inicio = time.time()

        calculate_cost = lambda duracion, tarifa: duracion * tarifa

        if modo == 'm':
            while not keyboard.is_pressed('p') and not keyboard.is_pressed('f'):
                time.sleep(0.1)
        elif modo == 'p':
            while not keyboard.is_pressed('m') and not keyboard.is_pressed('f'):
                time.sleep(0.1)

        fin = time.time()
        duracion = fin - inicio
        costo = calculate_cost(duracion, tarifa_por_segundo)
        self.total += costo
        print(f"⏱️ Duración: {duracion:.2f} segundos. 💰 Costo añadido: {costo:.2f} €.")

    def finalizar_trayecto(self):
        self.en_trayecto = False
        print(f"✅ Trayecto finalizado. Total a cobrar: {self.total:.2f} €.")

def main():
    print("🚖 ¡Bienvenido a TaxiGo, tu taxímetro digital! 🚖")
    print("Con TaxiGo, puedes calcular el costo de un trayecto en taxi basado en el tiempo en movimiento y en parada.")
    print("\n💡 ¿Cómo funciona?")
    print("   - Si el taxi está en movimiento, el costo aumenta según el tiempo transcurrido.")
    print("   - Si el taxi deja de moverse, el costo aumenta a un ritmo más bajo.")
    print("   - Presiona 'm' para indicar movimiento, 'p' para indicar que está detenido y 'f' para finalizar el trayecto.")
    print("\n¡Vamos a empezar!\n")
    taximetro = Taximetro()
    while True:
        opcion = input("¿Desea iniciar un nuevo trayecto? (s/n): ").lower()
        if opcion == 's':
            taximetro.iniciar_trayecto()
        elif opcion == 'n':
            print("🚗💨 Gracias por usar Taxímetro Digital TaxiGo. ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()