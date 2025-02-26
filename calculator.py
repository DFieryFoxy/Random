def main(): 
    x = float(input("Qual o valor de x?\n"))
    print("x ao quadrado é =", square(x))


def square(n):
    return pow(n, 2)


if __name__ == "__main__":
    main()