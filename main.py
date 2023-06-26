def calculate_average(numbers):
    if not numbers:
        raise ValueError("The list of numbers cannot be empty")
    total = sum(numbers)
    average = total / len(numbers)
    return average


#En esta funcion, se calcula el promedio de una lista de numero,
#si la lista esta vacia, debe arrojar un error.