import os
from funciones_menu import *



lista_principal_csv=[]


flag_A=False
flag_B=False
seguir="si"

while(seguir=="si"):

    
    opcion=mostrar_menu()
    match opcion:
        case 'A':
            lista_principal_csv=cargar_list_dict_csv("bicicletas.csv")
            print("Listar cargada correctamente.")
            flag_A=True

        case 'B':
            if(flag_A==True):
                mostrar_ciclistas(lista_principal_csv)
            else:
                print("Primero cargue el archivo csv")

        case 'C':
            if(flag_A==True):
                ingresar_data_tiempo(lista_principal_csv)
                mostrar_ciclistas(lista_principal_csv)
            else:
                print("Primero cargue el archivo csv")
                
        case 'D':
            if(flag_A==True):
                aux=buscar_menor_tiempo(lista_principal_csv)
                print("Personas que llegaron en mennor tiempo.")
                mostrar_lista_dic(aux)
            else:
                print("Primero cargue el archivo csv")
               
        case 'E':
            if(flag_A==True):
                while(True):

                    pedir_tipo=input("Ingrese tipo de bicicleta: ").upper()
                    if(pedir_tipo=="BMX" or pedir_tipo=="MTB" or pedir_tipo=="PLAYERA" or pedir_tipo=="PASEO"):

                        break
                    else:
                        print("Ese tipo de bicicleta no esta en el sistema.")

                lista_tipo_filtrado=mostrar_tipo_bicicleta(lista_principal_csv,"tipo",pedir_tipo)
                escribir_archivo_csv(pedir_tipo+".csv",lista_tipo_filtrado)
            else:
                print("Primero cargue el archivo csv")

        case 'F':
            if(flag_A==True):
                diccionario_aux=diccionarios_tipos_campo(lista_principal_csv,"tipo")
                for key in diccionario_aux:
                    diccionario_aux[key]=calcular_promedio_lista(diccionario_aux[key])
                for key in diccionario_aux:
                    print(f"El promedio de tiempo del tipo {key} es --> {diccionario_aux[key]:.2f}")
            else:
                print("Primero cargue el archivo csv")

        case 'G':
            if(flag_A==True):
                ordenar_ciclistas_doble_criterio(lista_principal_csv,"tipo","tiempo")
                mostrar_ciclistas(lista_principal_csv)
                flag_B=True
            else:
                print("Primero cargue el archivo csv")

        case 'H':
            if(flag_A==True and flag_B ==True):
                escribir_archivo_json("tipos_bicis_ordenadas.json",lista_principal_csv)
            else:
                print("Primero debe cargar la lista (A) y ordenarla (G).")
        case 'I':

            seguir=Salir_programa()
    print()
    os.system("pause")
    os.system("cls")
