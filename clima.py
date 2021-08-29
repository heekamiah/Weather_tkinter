from tkinter import *
import requests

#9f37a033ca01870649559869fea13f1b
#api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

def mostrar_respuesta(clima):
    nombre_ciudad = clima["name"]
    temp = clima["main"]["temp"]
    pre = clima["main"]["pressure"]
    desc = clima["weather"][0]["description"]

    ciudad["text"] = nombre_ciudad
    temperatura["text"] = str(int(temp)) + "ºC"
    presion["text"] = pre
    descripcion["text"] = desc

def clima_JSON(ciudad):
    API_key = "9f37a033ca01870649559869fea13f1b"
    URL = "https://api.openweathermap.org/data/2.5/weather"
    parametros = {"APPID": API_key, "q": ciudad, "units": "metric", "lang": "es"}
    response = requests.get(URL, params = parametros) 
    clima = response.json()


    print(clima["name"])
    print(clima["weather"][0]["description"])
    print(clima["main"]["temp"])
    print(clima["main"]["pressure"])

    mostrar_respuesta(clima)

ventana = Tk()
ventana.geometry("250x450")

texto_ciudad = Entry(ventana, font = ("Helvetica", 20, "normal"), justify = "center")
texto_ciudad.pack(padx = 5, pady = 5)

obtener_clima = Button(ventana, text= "Obtener Clima",font = ("Helvetica", 15, "normal"), command = lambda: clima_JSON(texto_ciudad.get()))
obtener_clima.pack()

ciudad = Label(font = ("Helvetica", 20, "normal"))
ciudad.pack(padx = 20, pady = 10)

temperatura = Label(font = ("Helvetica", 50, "normal"))
temperatura.pack(padx = 30, pady = 10)

presion = Label(font = ("Helvetica", 20, "normal"))
presion.pack(padx = 10, pady = 10)

descripcion = Label(font = ("Helvetica", 20, "normal"))
descripcion.pack(padx = 10, pady = 10)

más_información = Button(ventana, text= "Más Información")
más_información.pack(padx = 10, pady = 40)

ventana.mainloop()
