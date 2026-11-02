def mostrar_menu():
    print("\n--- CONVERSOR DE UNIDADES ---")
    print("1. Kilómetros a Millas")
    print("2. Grados Celsius a Fahrenheit")
    print("3. kilogramos a Libras")
    print("4. Salir")

def conversor_unidades():
        while True:
            mostrar_menu()
            opcion = input("\nElige una opción (1-4): ")

            if opcion == "1":
                try: 
                    km = float(input("Ingresa la cantidad en kilómetros "))
                    millas = km * 0.621371
                    print(f"👉 {km} km equivalen a {millas: .2f} millas.")
                except ValueError:
                    print("⚠️ Error: Por favor ingresa un número válido.")

            elif opcion == "2":
                try:
                    celsius = float(input("Ingresa los grados Celsius: "))
                    fahrenheit = (celsius * 9/5) + 32
                    print(f"👉 {celsius}°C equivalen a {fahrenheit:.2f}°F.")
                except ValueError:
                    print("⚠️ Error: Por favor ingresa un número válido.")

            elif opcion == "3":
                try:
                    kg = float(input("Ingresa los kilogramos: "))
                    libras = kg * 2.20462
                    print(f"👉 {kg} kg equivalen a {libras:.2f} libras.")
                except ValueError:
                    print("⚠️ Error: Por favor ingresa un número válido.")

            elif opcion == "4": 
                    print("¡Gracias por usar el conversor! Hasta luego. 👋")
                    break
            else: 
                print("⚠️ Opción no válida. Elige un número del 1 al 4.")
# Ejecutar el programa
if __name__ == "__main__":
    conversor_unidades()