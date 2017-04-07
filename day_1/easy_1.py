def find_item():

    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    aux = int(input("Enter item to find: "))
    if aux in lista:
        print("I find the element in te position", lista.index(aux))
    else:
        print("Sorry, i couldn't find your element :(")

find_item()

