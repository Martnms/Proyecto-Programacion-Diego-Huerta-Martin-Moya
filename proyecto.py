#Importamos las librerias que nesecitaremos para desarrollar el codigo
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from pandas.core.frame import DataFrame
from pandas.io.pytables import IndexCol
#Lo primero que hacemos es leer el archivo .csv
data = pd.read_csv("TasaDeIncidencia.csv",index_col=1)
df = pd.DataFrame(data)#Con esto creamos el DataFrame y le asignamos la variable data

#Aqui creamos una lista vacia llamada comunas para poder despues ingresar los datos necesarios
comunas = []
for i in df["Comuna"]: #Aca creamos una estructura "for" i in" y dentro del DataFrame en el indice comuna
    if i == "Total": ##Aca creamos una condicional en la que si "i" es igual a "Total" se lo salta para asi poder marcar solo las comunas
      continue
    else:
      comunas.append(i) #Agregamos los valores a la lista vacia creada anteriormente

region=list(df.iloc[:,0]) #Esta variable la creamos para que se seleccionaran todos los valores de la columna "0" la cual pertenece a las regiones
counter=[] #Aqui creamos una lista vacia 
for i in region: #Usamos la estructura "for i in " en region para moverse dentro de los datos de regiones
  if i not in counter: #Aca verificamos si los valores de "i" no estan en "counter"
    counter.append(i) #Aca se agrega a la variable vacia
for j in counter: # Revisa todas las regiones de "counter"
    region.remove(j) #Verifica si los valores de "counter" no estan en region


codigos=list(df.iloc[:,2]) #Esta variable la usamos para que se lean solo los datos de la segunda linea que pertenece al codigo de cada region
codigocomuna=[x for x in codigos if pd.isnull(x) == False and x !='nan'] #Elimina los datos que tienen un valor nulo

#Aca creamos un diccionario para que la region, comuna y codigo las une en una sola lista
areas = {"region":region, "comunas":comunas,"codigo":codigocomuna}
conexion = pd.DataFrame(areas) #Crea la conexion al DataFrame

#Aca printeamos el menu   
print("""Bienvenido 
Para poder tener un correcto funcionamiento de la primera funcion ingrese el nombre de la comuna tal cual como aparece en el GitHub    

Si desea conocer los codigos de las comunas y mostrar un grafico de su tasa de incidencia ingrese [1]

Si desea conocer el codigo de las regiones ingrese [2]

Si desea desplegar la region con menor tasa de incidencia ingrese [3]

Si desea desplegar la region con mayor tasa de incidencia ingrese [4]

Si desea finalizar el menu ingrese [0]
      """)
num = "" #Aca a la variable num la dejamos vacia 
x = int #x la definimos como un valor entero
while x != 0: #Mientras x sea distinto a 0 despliega el menu
  menu_index= int(input("Ingrese la opcion elegida: ")) #Aca al input le asiganmos un valor entero para que funcione el menu y sus opciones
  if menu_index == 1: #Si el input es igual a 1 se activa la primera funcion del menu
      num = input("Ingrese la comuna a buscar: ") #Ponemos un input para que el usuario ingrese la comuna que quiere buscar
      for i in range(len(conexion)): #Aqui usamos la estructura "for i in range" para movernos en el largo de la conexion y moverse en indices enteros
        if num == conexion["comunas"][i]: #num se mueve en el indice de comunas y si encuentra una muestra su indice
              print("Codigo de la comuna: "+ str(conexion["codigo"][i]) + " comuna: "+ conexion["comunas"][i])   #Printea el codigo + la comuna
              x = list(df.columns.values) #Aca se crea una lista con el valor de todas las columnas del DataFrame
              xs = x[-7:] #Despliega en el eje X las ultimas 7 fechas 
              valores = pd.read_csv("TasaDeIncidencia.csv",",") #La variable valores se le asigna el .csv para que lea sus valores como enteros
              num = np.where(valores["Comuna"]==num) #Aqui se ocupa la funcion de numpy para poder buscar en el DataFrame la columna "comunas"
              print(num) #Printea "num"
              valores2 =valores.iloc[int(num[0]),[-7,-6,-5,-4,-3,-2,-1]] #A la variable valores2 le asignamos el valor entero de la variable "num" ya que la usamos en la primera funcion del menu para que nos entregue el indice la comuna que se esta buscando
              val3 = list(valores2) #A la variable "val13" se le asigna las lista "valores2"
              plt.bar(xs,val3)
              plt.show() #Despliega el grafico
  if menu_index == 2: #Si el input es igual a 2 se activa la segunda funcion del menu
          print("""
      Arica y Parinacota Codigo: 15
      Tarapaca Codigo: 01
      Antofagasta Codigo: 02
      Atacama Codigo: 03
      Coquimbo Codigo: 04
      Valparaiso Codigo: 05
      Metropolitana Codigo: 13
      Del Libertador General Bernardo OHiggins Codigo: 06
      Maule Codigo: 07
      Nuble Codigo: 16
      Biobio Codigo: 08
      La Araucania Codigo: 09
      Los Rios Codigo: 14
      Los Lagos Codigo: 10
      Aysen Codigo: 11
      Magallanes y la Antartica Codigo: 12
      """)

  if menu_index == 3: #Si el input es igual a 3 se activa la tercera funcion del menu
    plt.title("Region Coquimbo") #Titulo del grafico
    x = list(df.columns.values) #Aca se crea una lista con el valor de la region de Coquimbo
    xs = x[-7:]#Despliega en el eje X las ultimas 7 fechas
    valores = pd.read_csv("TasaDeIncidencia.csv",",") #Lee los valores del DataFrame
    valores2 =valores.iloc[50,[-7,-6,-5,-4,-3,-2,-1]] #Lee el indice de la region con sus ultimas 7 fechas
    val3 = list(valores2) #A la variable "val13" se le asigna las lista "valores2"
    print(val3)
    plt.bar(xs,val3)
    plt.show()  #Muestra el grafico 

    
  if menu_index == 4: #Si el input es igual a 4 se activa la cuarta funcion del menu
    plt.title("Region Magallanes y la Antartica") #Titulo del grafico
    x = list(df.columns.values) #Aca se crea una lista con el valor de la region de Magallanes y Antartica
    xs = x[-7:]#Despliega en el eje X las ultimas 7 fechas
    valores = pd.read_csv("TasaDeIncidencia.csv",",") #Lee los valores del DataFrame
    valores2 =valores.iloc[361,[-7,-6,-5,-4,-3,-2,-1]] #Lee el indice de la region con sus ultimas 7 fechas
    val3 = list(valores2) #A la variable "val13" se le asigna las lista "valores2"
    print(val3)
    plt.bar(xs,val3)
    plt.show() #Muestra el grafico
  if menu_index == 0: #Si el input es igual a 0 se pone fin al menu
    x = 0 #Si el valor es igual a 0 se finaliza el programa
    print("FIN")
  