def main():
    x = int(input("Dfina o valor de x\n"))
    if is_even(x):
        print("par")
    else:
        print("Ímpar")

def is_even(n):
    return  n % 2 == 0 
        
main()