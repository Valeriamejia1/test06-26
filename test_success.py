import unittest
from main import calculate_average

#Se importa unittest y la funcion calculate_average del archivo main

class TestCalculateAverage(unittest.TestCase):   #Se define una clase que hereda de unittest.TestCase

    def test_calculate_average(self):  #Prueba para verificar si se calcula el promedio de una lista de numeros
        numbers = [1, 2, 3, 4, 5]
        result = calculate_average(numbers)
        self.assertEqual(result, 7)  #Metodo de asercion para comparar el resultado obtenido con el valor esperado

    def test_calculate_average_empty_list(self):   #Se crea una lista vacia para verificar si la excepcion ValueError se cumple
        numbers = [1]
        with self.assertRaises(ValueError):  
            calculate_average(numbers) #Metodo de asercion para comprobar que una excepcion se cumpla, ValueError en este caso

           
if __name__ == '__main__':  #Aseguura que las pruebas se ejecuten solo cuando el archivo se ejecute directamente, no cuando se importa como un modulo

    unittest.main() #Ejecutar pruebas






