def calculadora(operacion):
    if operacion == "rectangulo":
        base = int(input("Ingrese la base del rectángulo: "))
        altura = int(input("Ingrese la altura del rectángulo: "))
        print(f"Un rectángulo de base {base} cm y altura {altura} cm, "
              f"su área es: {base * altura} cm² y su perímetro es: {2 * (base + altura)} cm")

    elif operacion == "cuadrado":
        lado = int(input("Ingrese el lado del cuadrado: "))
        print(f"Un cuadrado de lado {lado} cm, "
              f"su área es: {lado ** 2} cm² y su perímetro es: {4 * lado} cm")

    elif operacion == "circulo":
        radio = int(input("Ingrese el radio del círculo: "))
        area = 3.1416 * radio ** 2
        perimetro = 2 * 3.1416 * radio
        print(f"Un círculo de radio {radio} cm, "
              f"su área es: {area:.2f} cm² y su perímetro es: {perimetro:.2f} cm")

    elif operacion == "triangulo":
        base = int(input("Ingrese la base del triángulo: "))
        altura = int(input("Ingrese la altura del triángulo: "))
        lado1 = int(input("Ingrese el primer lado del triángulo: "))
        lado2 = int(input("Ingrese el segundo lado del triángulo: "))
        
        area = (base * altura) / 2
        perimetro = base + lado1 + lado2
        
        print(f"Un triángulo de base {base} cm y altura {altura} cm, "
              f"su área es: {area} cm² y su perímetro es: {perimetro} cm")

    else:
        print("Syntax Error")
operacion = input("Ingrese una operacion: ")
calculadora(operacion)