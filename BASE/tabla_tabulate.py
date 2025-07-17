from tabulate import tabulate

encabezado = ["ID", "Nombre", "Programación", "Inglés", "Habilidades"]

estudiantes = [
  [101, "Juan Pérez", 4.0, 3.5, 2.8],
  [102, "Ana Gómez", 2.9, 3.8, 3.0]
]

headers = encabezado; #dependiendo de la entidad, se envian por parametro
print(tabulate(estudiantes,
         headers = headers,
         tablefmt='fancy_grid',
         stralign='left',
         floatfmt=",.1f"))
