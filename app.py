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
        print("Trayecto iniciado. Use 'm' cuando esté en movimiento, 'p' cuando esté parado y 'f' para finalizar el trayecto.")

        while self.en_trayecto:
            if keyboard.is_pressed('m'):
                print("Calculando tarifa en movimiento...")
                self.calcular_tarifa(0.05, modo='m')

            if keyboard.is_pressed('p'):
                print("Calculando tarifa en parada...")
                self.calcular_tarifa(0.02, modo='p')

            if keyboard.is_pressed('f'):
                self.finalizar_trayecto()
                return  # Continua con el menú principal sin salir del bucle

    def calcular_tarifa(self, tarifa_por_segundo, modo):
        inicio = time.time()

        if modo == 'm':
            while keyboard.is_pressed('m'):
                time.sleep(0.1)
        elif modo == 'p':
            while keyboard.is_pressed('p'):
                time.sleep(0.1)

        fin = time.time()
        duracion = fin - inicio
        costo = duracion * tarifa_por_segundo
        self.total += costo
        print(f"Duración: {duracion:.2f} segundos. Costo añadido: {costo:.2f} €.")

    def finalizar_trayecto(self):
        self.en_trayecto = False
        print(f"Trayecto finalizado. Total a cobrar: {self.total:.2f} €.")


def main():
    print("Bienvenido al Taxímetro Digital TaxiGo")
    taximetro = Taximetro()
    while True:
        opcion = input("¿Desea iniciar un nuevo trayecto? (s/n): ").lower()
        if opcion == 's':
            taximetro.iniciar_trayecto()
        elif opcion == 'n':
            print("Gracias por usar Taxímetro Digital TaxiGo. ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
