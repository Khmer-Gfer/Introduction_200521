# def es_primo(numero):
#     contador = 0

#     for i in range(1, numero + 1):
#         if i == 1 or i == numero:
#             continue
#         if numero % i == 0:
#             contador += 1
#     if contador == 0:
#         return True
#     else:
#         return False

# def es_primo(numero):
#     fermat = 2 ** (numero - 1)
#     if fermat % numero == 1:
#         return True
#     else:
#         return False    


def es_primo(numero):
    contador = 0

    for i in range(2, numero + 1):
        if i == numero:
            continue
        if numero % i == 0:
            break
    if contador == 0:
        return True
    else:
        return False


# def run():
#     numero = int(input("Escribe un número: "))
#     if es_primo(numero):
#         print("Es primo")
#     else:
#         print("No es primo")


def run():
    numero = int(input("Escribe un número: "))
    if numero == 1:
        print("Es primo")
    elif es_primo(numero):
        print("Es primo")
    else:
        print("No es primo")


if __name__ == "__main__":
    run()