import requests
import datetime
import json

class MindicadorUF:
    def __init__(self):
        self.url_base = "https://mindicador.cl/api/uf/"
    
    def obtener_valor_uf(self, fecha):
        fecha_minima = datetime.datetime(2013, 1, 1)
        if fecha < fecha_minima:
            return None

        url = self.url_base + fecha.strftime("%d-%m-%Y")
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return data["serie"][0]["valor"]
        else:
            return None

class ConsultaUF:
    def __init__(self, mindicador):
        self.mindicador = mindicador
    
    def consultar(self, fecha):
        valor_uf = self.mindicador.obtener_valor_uf(fecha)
        if valor_uf is not None:
            resultado = {"fecha": fecha.strftime("%d-%m-%Y"), "valor_uf": valor_uf}
            return json.dumps(resultado)
        else:
            return "No se pudo obtener el valor de UF para la fecha especificada."

# Ejemplo de uso
fecha = datetime.datetime(2023, 5, 1)
mindicador = MindicadorUF()
consulta_uf = ConsultaUF(mindicador)
resultado = consulta_uf.consultar(fecha)

print(resultado)


    
 #Este código utiliza la API de Mindicador para obtener el valor de la Unidad de Fomento para una fecha específica. 
 #La fecha se debe pasar como un objeto datetime en el parámetro fecha.

 #La clase MindicadorUF sigue el principio de responsabilidad única (SRP) al tener una única responsabilidad: obtener el valor de la Unidad de Fomento desde la API de Mindicador. Además, sigue el principio de inversión de dependencias (DIP) al depender de abstracciones en lugar de concreciones. En este caso, la abstracción es la interfaz de la clase, que se compone de un único método: obtener_valor_uf. De esta manera, el código es más fácil de mantener y extender.

#La clase ConsultaUF sigue el principio de responsabilidad única (SRP) al tener una única responsabilidad: consultar el valor de la Unidad de Fomento para una fecha específica y formatear la respuesta como un objeto JSON. Además, sigue el principio de segregación de interfaces (ISP) al no tener una interfaz con más métodos de los necesarios para su responsabilidad. En este caso, la única interfaz es el método consultar.

#De esta manera, el código es más fácil de probar, mantener y extender.
 






