def Salir_programa()->str:
    """
    Solicita al usuario que confirme si desea salir del programa.

    Returns:
    - str: "no" si el usuario elige no salir del programa, "si" si el usuario elige salir del programa.

    Note:
    - Esta función solicita al usuario que ingrese "si" o "no" para confirmar si desea salir del programa. Devuelve "si" si el usuario elige salir y "no" si elige no salir.
    """

    while(True):
        print()
        rta=input('Desea salir del programa? ')
        if(rta=="si"):
            seguir="no"
            return seguir
            
        elif(rta=='no'):
            seguir="si"
            return seguir
        else:
            
            print("Error. conteste con 'si' o 'no' ")

def mostrar_menu()->str:
    print("""
                                MENU DEL PARCIAL
            A --> cargar archivo csv
            B --> Imprimir lista:
            C --> Asignar tiempos:  
            D --> Informar ganador: 
            E --> Filtrar por tipo:  
            F --> Informar promedio por tipo: 
            G --> Mostrar posiciones: 
            H --> Guardar posiciones: 
          
            I --> Salir.
            
        
          
          """)
    opcion=input("Ingrese opciones a realizar: ")
    return opcion.upper()

def cargar_list_dict_json(nombre_archivo_csv):
    """
    Carga una lista de diccionarios desde un archivo JSON.

    Args:
    - nombre_archivo_csv (str): El nombre del archivo JSON que se cargará.

    Returns:
    - list: Una lista de diccionarios que contiene los datos del archivo JSON.
    """
    import json
    
    def dir_path_actual(nombre_archivo:str):
        import os
        dir_actual=path=os.path.dirname(__file__)
        return os.path.join(dir_actual,nombre_archivo)

    with open(dir_path_actual(nombre_archivo_csv),"r",encoding="utf-8") as archivo:
        personas= json.load(archivo)
        return personas

def escribir_archivo_json(nombre_archivo_escribir,lista):
    """
    Escribe una lista de diccionarios en un archivo JSON.

    Args:
    - nombre_archivo_escribir (str): El nombre del archivo JSON que se escribirá.
    - lista (list): La lista de diccionarios que se escribirá en el archivo.

    Returns:
    - None: Esta función no devuelve ningún valor, solo escribe los datos en el archivo JSON.
    """
    import json

    def dir_path_actual(nombre_archivo:str):
        import os
        dir_actual=path=os.path.dirname(__file__)
        return os.path.join(dir_actual,nombre_archivo)
    
    with open(dir_path_actual(nombre_archivo_escribir),"w",encoding="utf-8") as archivo:
       json.dump(lista,archivo,indent=4)


def cargar_list_dict_csv(nombre_archivo_csv):
    """
    Carga una lista de diccionarios desde un archivo CSV.

    Args:
    - nombre_archivo_csv (str): El nombre del archivo CSV que se cargará.

    Returns:
    - list: Una lista de diccionarios que contiene los datos del archivo CSV.
    """
    def dir_path_actual(nombre_archivo:str):
        import os
        dir_actual=os.path.dirname(__file__)
        return os.path.join(dir_actual,nombre_archivo)

    with open(dir_path_actual(nombre_archivo_csv),"r",encoding="utf-8") as archivo:
        lista=[]
        
        encabezado=archivo.readline().strip("\n").split(",")
        # lista.append(encabezado)
        print()
        
        for linea in archivo.readlines():
            dic={}
            
            linea=linea.strip("\n").split(",")
            
            id_bike,nombre,tipo,tiempo=linea
            
            dic["id_bike"]=id_bike
            dic["nombre"]=nombre
            dic["tipo"]=tipo
            dic["tiempo"]=int(tiempo)
            lista.append(dic)
            
    
    return lista

def escribir_archivo_csv(nombre_archivo_escribir,lista):
    """
    Escribe una lista de diccionarios en un archivo CSV.

    Args:
    - nombre_archivo_escribir (str): El nombre del archivo CSV que se escribirá.
    - lista (list): La lista de diccionarios que se escribirá en el archivo.

    Returns:
    - None: Esta función no devuelve ningún valor, solo escribe los datos en el archivo CSV.
    """
    def dir_path_actual(nombre_archivo:str):
        import os
        dir_actual=path=os.path.dirname(__file__)
        return os.path.join(dir_actual,nombre_archivo)
    
    with open(dir_path_actual(nombre_archivo_escribir),"w",encoding="utf-8") as archivo:
        encabezado=",".join(list(lista[0].keys())) + "\n"
        archivo.write(encabezado)
        for persona in lista:
            values=list(persona.values())
            l=[]
            for value in values:
                if(isinstance(value,int) or isinstance(value,float)):
                    l.append(str(value))
                else:
                    l.append(value)
            
            persona=",".join(l) + "\n"
            
            archivo.write(persona)

def mostrar_dic(dic:dict)->None:
    """
    Muestra las claves y valores de un diccionario.

    Args:
    - dic (dict): El diccionario cuyas claves y valores se mostrarán.

    Returns:
    - None: Esta función no devuelve ningún valor. Imprime las claves y valores del diccionario proporcionado.
    """

    for clave in dic:
        print(f"{clave}: {dic[clave]}")


def mostrar_lista_dic(lista:list)->None:
    """
    Muestra las claves y valores de cada diccionario en una lista de diccionarios.

    Args:
    - lista (list): La lista de diccionarios cuyas claves y valores se mostrarán.

    Returns:
    - None: Esta función no devuelve ningún valor. Imprime las claves y valores de cada diccionario en la lista.
    """

    for dic in lista:
        for clave in dic:
            print(f"{clave} --> {dic[clave]}")
        print()


def mostrar_tipo_bicicleta(lista,campo,valor)->list:
    """
    Devuelve una lista de diccionarios que tienen un valor específico en un campo dado.

    Args:
    - lista (list): La lista de diccionarios en la que se realizará la búsqueda.
    - campo (str): El nombre del campo en el que se realizará la búsqueda.
    - valor (str): El valor que se buscará en el campo especificado.

    Returns:
    - list: Una lista de diccionarios que cumplen con la condición de tener el valor especificado en el campo dado.
    """

    lista_aux=[]
    
    for dic in lista:
        
        if(dic[campo]==valor):
            lista_aux.append(dic)
            

    return lista_aux

def ingresar_data_tiempo(lista:list)->None:
    """
    Agrega un campo 'tiempo' con un valor aleatorio entre 50 y 120 a cada diccionario en una lista de diccionarios.

    Args:
    - lista (list): La lista de diccionarios a la que se agregarán los tiempos.

    Returns:
    - None: Esta función no devuelve ningún valor. Modifica la lista proporcionada añadiendo un campo 'tiempo' a cada diccionario.
    """
    from random import randint
    for i in range(len(lista)):
        aux=randint(50,120)
        lista[i]["tiempo"]=aux
        
def buscar_menor_tiempo(lista:list)->None:
    """
    Encuentra y devuelve una lista de diccionarios con el menor tiempo en una lista de diccionarios.

    Args:
    - lista (list): La lista de diccionarios que contienen el campo 'tiempo'.

    Returns:
    - list: Una lista de diccionarios que tienen el menor valor en el campo 'tiempo'.
    """
     

    lista_return=[]

    aux=lista[0]["tiempo"]

    for dic in lista:
        
        if(dic["tiempo"]<aux):
            aux=dic["tiempo"]
           
            
    for dic in lista:
        if(dic["tiempo"]==aux):
            lista_return.append(dic)
            
    return lista_return

def mapear_campo(lista:list,campo:str)->list:
    """
    Devuelve una lista con los valores de un campo específico de cada diccionario en una lista de diccionarios.

    Args:
    - lista (list): La lista de diccionarios de la que se extraerán los valores.
    - campo (str): El nombre del campo cuyos valores se extraerán.

    Returns:
    - list: Una lista de valores del campo especificado.
    """
    lista_retorno=[]
    for dic in lista:
            lista_retorno.append(dic[campo])
    return lista_retorno

def diccionarios_tipos_campo(lista:list,campo:str)->dict:
    """
    Agrupa diccionarios en una lista según los diferentes valores de un campo específico.

    Args:
    - lista (list): La lista de diccionarios que se agruparán.
    - campo (str): El nombre del campo que se utilizará para agrupar los diccionarios.

    Returns:
    - dict: Un diccionario donde las claves son los diferentes valores del campo especificado y los valores son listas de diccionarios que tienen ese valor.
    """
    tipos=list(set(mapear_campo(lista,campo)))
    dict_aux={}
    for tipo in tipos:
        
        aux=lista_campo_condicion(lista,campo,tipo)
        dict_aux[tipo]=aux
    return dict_aux
        


def lista_campo_condicion(lista:list,campo:str,condicion:str)->list:
    """
    Devuelve una lista de tiempos de diccionarios que cumplen con una condición específica en un campo dado.

    Args:
    - lista (list): La lista de diccionarios en la que se realizará la búsqueda.
    - campo (str): El nombre del campo en el que se realizará la búsqueda.
    - condicion (str): El valor que se buscará en el campo especificado.

    Returns:
    - list: Una lista de tiempos de los diccionarios que cumplen con la condición especificada.

    Raises:
    - ValueError: Si no se encuentra ningún diccionario que cumpla con la condición.
    """
    lista_return=[]
    flag=False
    for dic in lista:
        if(dic[campo]==condicion or dic[campo]==""):
            lista_return.append(dic["tiempo"])
            flag=True
    if(flag==False):
        raise ValueError("no se encontro ese campo")
    return lista_return

def totalizar_lista(lista:list)->int:
    """
    Calcula la suma de los elementos de una lista de números.

    Args:
    - lista (list): La lista de números que se sumarán.

    Returns:
    - int: La suma de los elementos de la lista.
    """
    suma=0
    for el in lista:
       suma=suma+el
    return suma
 
def  calcular_promedio_lista(lista:list)->float:
    """
    Calcula el promedio de los elementos de una lista de números.

    Args:
    - lista (list): La lista de números de la que se calculará el promedio.

    Returns:
    - float: El promedio de los elementos de la lista.

    Raises:
    - ValueError: Si la lista está vacía.
    - ValueError: Si el argumento pasado no es una lista.
    """
    if(isinstance(lista,list)):
        aux=len(lista)
        suma=totalizar_lista(lista)
        if(aux!=0):
            promedio=suma/aux
        else:
            raise ValueError("no esta definido el promedio de una lista vacia.")
        return promedio
    raise  ValueError("lo que ingreso no es una lista.")

def mostrar_ciclista(ciclista:dict)->None:
    """
    Muestra la información de un ciclista en un formato específico.

    Args:
    - ciclista (dict): Un diccionario que contiene la información del ciclista.

    Returns:
    - None: Esta función no devuelve ningún valor. Imprime la información del ciclista.
    """
    print(f"{ciclista["id_bike"]}       {"|"}  {ciclista["nombre"]:10}   {"|"}    {ciclista["tipo"]:10}      {"|"}       {ciclista["tiempo"]}    ")

def mostrar_ciclistas(ciclistas:list)->None:
    """
    Muestra una lista de ciclistas en un formato tabular.

    Args:
    - ciclistas (list): Una lista de diccionarios, cada uno conteniendo la información de un ciclista.

    Returns:
    - None: Esta función no devuelve ningún valor. Imprime la información de cada ciclista en la lista.
    """
    TAM=len(ciclistas)
    print("          ---> Lista de ciclistas<---")
    print("id bike     nombre              tipo               tiempo                ")             
    print("-------------------------------------------------------------")
    for i in range(TAM):
        mostrar_ciclista(ciclistas[i])
        print("-----------------------------------------------------------------")


def ordenar_ciclistas_doble_criterio(lista:list,campo1,campo2)->None:
    """
    Ordena una lista de diccionarios por dos criterios en orden descendente.

    Args:
    - lista (list): La lista de diccionarios que se ordenará.
    - campo1 (str): El primer campo por el cual se ordenará la lista.
    - campo2 (str): El segundo campo por el cual se ordenará la lista.

    Returns:
    - None: Esta función no devuelve ningún valor. Modifica la lista en su lugar.
    """
   
    tam=len(lista)

    for i in range(tam-1):
        for j  in range(i+1,tam):
           
            if(lista[i][campo1]==lista[j][campo1]):
                      
                if(lista[i][campo2]>lista[j][campo2]):
                    
                    aux=lista[i]
                    lista[i]=lista[j]
                    lista[j]=aux 

            elif((lista[i][campo1]>lista[j][campo1])):
                    
                    aux=lista[i]
                    lista[i]=lista[j]
                    lista[j]=aux