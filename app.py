temperaturas = []
print("Profavor Ingresa 10 temperaturas")

for i in range(10):
    temperatura = float(input(f"Temperatura {i + 1}: "))
    temperaturas.append(temperatura)

promedio = sum(temperaturas) / len(temperaturas)

print(f"\nEl promedio de las temperaturas es: {promedio:.2f}")