import os
import sys
import time
from tabulate import tabulate
import re
import pickle
from datetime import datetime

from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Image
from reportlab.lib import colors
from reportlab.lib.units import inch

from colorama import Fore, Back, Style, init
init()

import time 
import msvcrt

#valida que un codigo se encuentre en un diccionario
def leerCodigoValidado (lista, mensaje):
      while True:
          print(f"{mensaje}", end="", flush=True)
          codigoBuscar = input().upper()
          encontrado = buscar(lista, codigoBuscar)
          if encontrado >= 0:
            return codigoBuscar, encontrado
          else:
            print("Error: Código NO existe", end="", flush=True)
            time.sleep(1) # Pausa breve de 1 segundo
            print(end="\r\033[K\033[F") # Mueve el cursor al inicio de la linea y limpia la línea
            
#-------------------------------------------------------------------#
#recibe un diccionario lo muestra y validad la opcion del usuario   #
#VALIDA que sea un valor numerio en el rango enviado por parametro  #
#-------------------------------------------------------------------#
def leerDiccionario (diccionario, mensaje):            
      tabla = [[clave, descripcion] for clave, descripcion in diccionario.items()]
      print(tabulate(tabla, headers=["Clave", "Descripción"], tablefmt="fancy_grid"))
      while True:
        #   opcion = LeerCaracter( mensaje ).upper()
          opcion = input( mensaje ).upper()
          if opcion in diccionario:
                return opcion
          else:
            print("Error: Opción NO válida", end="", flush=True)
            time.sleep(1) # Pausa breve de 1 segundo
            print(end="\r\033[K") # Mueve el cursor al inicio de la linea y limpia la línea


###############################################
#función lee un solo carácter NO espera ENTER #
###############################################
def LeerCaracter (mensaje):
  print(mensaje, end="", flush=True)
  return msvcrt.getch().lower().decode('utf-8')  #getch captura un solo caracter No hay que dar enter

##############################################################################################
# Función que valida el ingreso de una cadena que no sea vacia y limitar un maximo caracteres#
# SI se quiere que retorne recortado usar return cadena[:maximoCaracteres]
##############################################################################################
def leerCadena( mensaje, maximoCaracteres ):
    while True:
        #print(f"{mensaje}", end="", flush=True)
        cadena = input( f"{mensaje} (Máx. {maximoCaracteres} caracteres): ").strip()
        if 0 < len(cadena) <= maximoCaracteres:  #Retorna la cadena válida
           return cadena[:maximoCaracteres] #cadena
        else:
            print(f"❌ Error: La cadena no debe estar vacía y debe tener máximo {maximoCaracteres} caracteres.", end="", flush=True)
            time.sleep(1)                 # Pausa breve de 1 segundo)
            print("\r\033[K", end="")     # \r Mueve cursor al inicio de la línea y limpia la línea con \033[K
            print("\033[F\033[K", end="") # Mueve cursor al final de la línea de arriba y limpia la línea
            continue
        
############################################################################
# Función que valida el ingreso de la fecha en un formato y rango correcto #
############################################################################
def leerFecha( mensaje ):
    while True:
        #print(f"{mensaje}", end="", flush=True)
        fecha_str = input( mensaje )
        try:
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
            return fecha.strftime("%Y-%m-%d")  #fecha  # Retorna un objeto datetime (fecha y hora)
        except ValueError:
            print("❌ Error: Formato incorrecto. Intente de nuevo.", end="", flush=True)
            time.sleep(1)                 # Pausa breve de 1 segundo)
            print("\r\033[K", end="")     # \r Mueve cursor al inicio de la línea y limpia la línea con \033[K
            print("\033[F\033[K", end="") # Mueve cursor al final de la línea de arriba y limpia la línea
            continue

############################################################################
# Función que valida el ingreso del mail en un formatro correcto           #
############################################################################
def leerMail ( mensaje ):
      while True:
          #print(f"{mensaje}", end="", flush=True) 
          email = input ( mensaje )
          #correo valido verifica antes y despues del @
          patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'          
          if re.match(patron, email.lower()):
            return email
          else:
            print("Error: Email NO es correcto", end="", flush=True)
            time.sleep(1) # Pausa breve de 1 segundo
            print(end="\r\033[K\033[F") # Mueve el cursor al inicio de la linea y limpia la línea

############################################################################
# Función que valida el ingreso de un decimal en un rango minimo y maximo  #
############################################################################
def  leerEntero (mensaje, minimo, maximo):
  while True:
    print(f"{mensaje} ({minimo}-{maximo}): ", end="", flush=True)
    valor = input().strip()
    # Verificar que no esté vacío ni tenga espacios intermedios
    if not valor or " " in valor:
      print(f"❌Error: {mensaje} no debe estar vacío ni contener espacios.", end="", flush=True)
      time.sleep(1)                 # Pausa breve de 1 segundo)
      print("\r\033[K", end="")     # \r Mueve cursor al inicio de la línea y limpia la línea con \033[K
      print("\033[F\033[K", end="") # Mueve cursor al final de la línea de arriba y limpia la línea
      continue
      # Verificar si es un número decimal válido
    try:
      numero = int(valor)
      if minimo <= numero <= maximo:  # numero >= minimo and numero <= maximo
        return numero
      else:
        print(f"❌Error: {mensaje} debe estar entre {minimo} y {maximo}.", end="", flush=True)
        time.sleep(1)                 # Pausa breve de 1 segundo
        print("\r\033[K", end="")     # Mueve cursor al inicio de la línea y limpia la línea
        print("\033[F\033[K", end="") # Mueve cursor al final de la línea de arriba y limpia la línea
    except ValueError:
      print("❌Error: {mensaje} inválida. ", end="", flush=True)
      time.sleep(1)                 # Pausa breve de 1 segundo
      print("\r\033[K", end="")     # Mueve cursor al inicio de la línea y limpia la línea
      print("\033[F\033[K", end="") # Mueve cursor al final de la línea de arriba y limpia la línea

############################################################################
# Función que valida el ingreso de un decimal en un rango minimo y maximo  #
############################################################################
def  leerFlotante (mensaje, minimo, maximo):
  while True:
    print(f"{mensaje} ({minimo}-{maximo}): ", end="", flush=True)
    valor = input().strip().replace(",", ".")
    # Verificar que no esté vacío ni tenga espacios intermedios
    if not valor or " " in valor:
      print(f"❌Error: {mensaje} no debe estar vacío ni contener espacios.", end="", flush=True)
      time.sleep(1)                 # Pausa breve de 1 segundo)
      print("\r\033[K", end="")     # \r Mueve cursor al inicio de la línea y limpia la línea con \033[K
      print("\033[F\033[K", end="") # Mueve cursor al final de la línea de arriba y limpia la línea
      continue
      # Verificar si es un número decimal válido
    try:
      numero = float(valor)
      if minimo <= numero <= maximo:  # numero >= minimo and numero <= maximo
        return numero
      else:
        print(f"❌Error: {mensaje} debe estar entre {minimo} y {maximo}.", end="", flush=True)
        time.sleep(1)                 # Pausa breve de 1 segundo
        print("\r\033[K", end="")     # Mueve cursor al inicio de la línea y limpia la línea
        print("\033[F\033[K", end="") # Mueve cursor al final de la línea de arriba y limpia la línea
    except ValueError:
      print("❌Error: {mensaje} inválida. ", end="", flush=True)
      time.sleep(1)                 # Pausa breve de 1 segundo
      print("\r\033[K", end="")     # Mueve cursor al inicio de la línea y limpia la línea
      print("\033[F\033[K", end="") # Mueve cursor al final de la línea de arriba y limpia la línea

#La función devuelve el nombre del sistema operativo y aplica el comando respectivo
def limpiarPantalla ():    
    if os.name == 'nt':  # Para sistemas Windows
        os.system('cls')
    else:  # Para sistemas Unix/Linux/Mac
        os.system('clear')
    
def cabecera ( titulo ): 
    print(Fore.RED + f"\n   {titulo}    \n" + Style.RESET_ALL )


def mensajeEsperaSegundos( mensaje, segundos ):
    print(Fore.YELLOW + Style.BRIGHT + mensaje + Style.RESET_ALL)
    time.sleep( segundos )

def mensajeErrorEsperaSegundos( mensaje, segundos ):
    print(Fore.RED + Style.BRIGHT + mensaje + Style.RESET_ALL)
    time.sleep( segundos )

##################################################################
# Procedimiento que espera que el usuario presione Enter         #
##################################################################
def mensajeEsperaEnter( mensaje ):
    print("\n" + Fore.GREEN + Style.BRIGHT + mensaje + Style.RESET_ALL, end="")
    input()

#-----------------------------------------------------------#
#Función con las opciones del CRUD para cualquier entidad   #
#-----------------------------------------------------------#
def menuCrud( titulo ): 
    limpiarPantalla()    #os.system('cls')
    print(tabulate([['' + Fore.GREEN + "ALMACÉN MARKET \n" + Style.RESET_ALL + '' + Fore.LIGHTYELLOW_EX + "MENU: " + titulo + '' + Style.RESET_ALL + ''],],
                     tablefmt='fancy_grid',
                     stralign='center'))
    print(tabulate([ 
                     ['*' * (len(titulo) + 6)],
                     ["\t" + Back.YELLOW + "[1]" + Style.RESET_ALL + "  INSERTAR  "],
                     ["\t" + Back.YELLOW + "[2]" + Style.RESET_ALL + "  LISTAR    "],
                     ["\t" + Back.YELLOW + "[3]" + Style.RESET_ALL + "  CONSULTAR "],
                     ["\t" + Back.YELLOW + "[4]" + Style.RESET_ALL + "  ACTUALIZAR"],
                     ["\t" + Back.YELLOW + "[5]" + Style.RESET_ALL + "  ELIMINAR  "],
                     ["\t" + Back.YELLOW + "[6]" + Style.RESET_ALL + "  SALIR     "]
                     ],
                     tablefmt='fancy_grid',
                     stralign='left'))
    
#-----------------------------------------------------------#
#Función con las opciones del CRUD para nómina  #
#-----------------------------------------------------------#
def menuCrudDos( titulo ): 
    limpiarPantalla()    #os.system('cls')
    print(tabulate([['' + Fore.GREEN + "ALMACÉN MARKET \n" + Style.RESET_ALL + '' + Fore.LIGHTYELLOW_EX + "MENU: " + titulo + '' + Style.RESET_ALL + ''],],
                     tablefmt='fancy_grid',
                     stralign='center'))
    print(tabulate([ 
                     ['*' * (len(titulo) + 6)],
                     ["\t" + Back.YELLOW + "[1]" + Style.RESET_ALL + "  INSERTAR  "],
                     ["\t" + Back.YELLOW + "[2]" + Style.RESET_ALL + "  LISTAR    "],
                     ["\t" + Back.YELLOW + "[3]" + Style.RESET_ALL + "  CONSULTAR "],
                     ["\t" + Back.YELLOW + "[4]" + Style.RESET_ALL + "  ACTUALIZAR"],
                     ["\t" + Back.YELLOW + "[5]" + Style.RESET_ALL + "  PAGO NOMINA"],
                     ["\t" + Back.YELLOW + "[6]" + Style.RESET_ALL + "  SALIR     "]
                     ],
                     tablefmt='fancy_grid',
                     stralign='left'))

#----------------------------------------------------------------------------#
#Función para listar cualquier lista, le debo enviar la lista y el encezado  #
#----------------------------------------------------------------------------#
def listar(encabezado, listas): 
    # Formatear columnas de numeros que no salga exponencial
    limpiarPantalla()
    headers = encabezado
    #headers =[Fore.GREEN + 'PLACA', 'MARCA', 'MODELO', 'COLOR', 'PRECIO' ]
    print(tabulate(listas,
                   headers = headers,
                   tablefmt='fancy_grid',
                   stralign='left',
                   floatfmt=",.0f"))
#-------------------------------------------------------------------------------------#
# Función Mostrar un solo registro, con la cabecera y los datos de la entidad enviada #
#-------------------------------------------------------------------------------------#
def mostrar(encabezado, lista): 
    os.system('cls')
    # Formatear columnas de numeros que no salga exponencial
    lista = [lista]   #CONVERTIMOS A LISTA DE LISTAS POR QUE TABULATE LO EXIGE
    headers = encabezado; #dependiendo de la entidad, se envian por parametro
    print(tabulate(lista,
                   headers = headers,
                   tablefmt='fancy_grid',
                   stralign='left',
                   floatfmt=",.0f"))
    
#-----------------------------------------------------------#
# Función para buscar elemento en lista por su codigo PK,   #
# devolver indice si lo encuentra o -1 si no lo encuentra   #
#-----------------------------------------------------------#
def buscar(lista, codigoBuscar):
    posicion = -1
    for indice, registro in enumerate(lista):   #recorre toda la lista y extrae registro a registro con su indice
        #print(indice, " -- ", fila)  0.placa 1.marca 2.color......
        if str(registro[0]).upper() == str(codigoBuscar).upper():
            return indice
    return posicion

#---------------------------------------------------------#
# Función para guardar Información en Archivos - MODO  w, # 
# si existe lo borra, si no existe lo crea                #
#---------------------------------------------------------#
def guardar(lista, filename):
    archivo = open( filename, 'wb') #W se abre solo para escritua y si existe lo borra y crea uno nuevo y B indica que un archivo binario
    pickle.dump(lista, archivo)
    archivo.close()
    print(""+Fore.LIGHTYELLOW_EX+"\n\n>>> Guardando Información en los archivos correspondientes <<< " + Style.RESET_ALL)
    time.sleep(2)

#----------------------------------------------------------------------#
# Función para cargar Información en Archivos, MODO R, de solo lectura #
#----------------------------------------------------------------------#
def cargar(lista, filename):
    try:
        archivo = open(filename, 'rb')   #R se abre solo para lectura y B indica que un archivo binario
        lista = pickle.load(archivo)
        archivo.close()
        print("" + Fore.RED+"\n>>> Cargando Información : "+filename + '' + Style.RESET_ALL)
        time.sleep(1)
        return lista
    except:
        print("" + Fore.RED+"\n>>> Error al cargar el archivo o no se ha creado: " + filename + '' + Style.RESET_ALL)
        time.sleep(1)
    return lista

#GENERA Y ABRE LOS PDF GENERADOS


def abrirPDF( archivo_pdf):
    #directorio = "reportesPDF"
    #archivo_pdf = os.path.join(directorio, "clientes.pdf") 
    try:
        if sys.platform == "win32":  # Windows
            os.startfile(archivo_pdf)
        elif sys.platform == "darwin":  # macOS
            os.system(f"open {archivo_pdf}")
        elif sys.platform.startswith("linux"):  # Linux
            os.system(f"xdg-open {archivo_pdf}")
        else:
            print("⚠ No se pudo abrir el PDF automáticamente.")
    except Exception as e:
        print(f"❌ Error al abrir el PDF: {e}")


# Función para generar PDF con logo y tabla ajustada
def generarPDF (encabezado, clientes, archivo_pdf):

    # Márgenes y ajuste extra para margen visual
    margen = 28
    extra_margen_visual = 10  # Espacio extra visual
    ancho_total = 792  
    ancho_util = (ancho_total - (2 * margen)) - (2 * extra_margen_visual)

    doc = SimpleDocTemplate(archivo_pdf, pagesize=landscape(letter),
                            leftMargin=margen, rightMargin=margen,
                            topMargin=margen, bottomMargin=margen)

    elementos = []

    # Agregar logo alineado a la izquierda
    logo_path = "imagenes/logo.jpg"  # Asegúrate de que este archivo está en la misma carpeta
    #logo = Image(logo_path, width=1.5 * inch, height=1 * inch)  # Tamaño ajustado del logo
    #elementos.append(logo)
    try:
        img = Image(logo_path, width=1.5 * inch, height=0.75 * inch)  # Ajusta el tamaño del logo
        img.hAlign = 'RIGHT'  # Alinea a la derecha
        elementos.append(img)
    except:
        print("⚠️ No se encontró el logo, el PDF se generará sin él.")

    # Espaciado antes del título
    elementos.append(Spacer(1, 10))

    # Título centrado con espacio arriba
    titulo = [["LISTADO DE CLIENTES"]]
    tabla_titulo = Table(titulo, colWidths=[ancho_util])
    tabla_titulo.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 16),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 16),
    ]))
    elementos.append(tabla_titulo)

    # Nueva versión de cabeceras más cortas
    #datos = [["Código", "Identif.", "Nombres", "Nacimiento", "Dirección", "Teléfonos", "Email", "Estado"]]
    datos = [encabezado]
    datos.extend(clientes)

    # Distribución del ancho
    col_widths = [60, 70, 115, 90, 100, 100, 135, 55]
    #col_widths = anchoColumnas 

    tabla = Table(datos, colWidths=col_widths)

    # Estilos de la tabla
    tabla.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    
    elementos.append(tabla)

    # Generar el PDF
    doc.build(elementos)
    print(f"PDF generado correctamente con membrete y logo: {archivo_pdf}")



