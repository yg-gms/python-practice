equation = input("Expression: ").strip()

x_str, operator, z_str = equation.split(" ")

x = float(x_str)
z = float(z_str)

if operator == "+":
    print(x + z)

elif operator == "-":
    print(x - z)

elif operator == "/":
    print(x / z)

elif operator == "*":
    print(x * z)