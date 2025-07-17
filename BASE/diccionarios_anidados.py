persona = {
    "valeria": {"codigo": 'COD001', "nacimiento": {"anyo": 2000, "mes": 12, "dia": 31}},
    "ernesto": {"codigo": 'COD002', "nacimiento": {"anyo": 1964, "mes": 1, "dia": 6}}
}

print(f"ERNESTO CUMPLE AÑOS EN EL MES DE {persona["ernesto"]["nacimiento"]["mes"]} DIA {persona["ernesto"]["nacimiento"]["dia"]}")


meses = {
    1: "ENERO",
    2: "FEFRERO"
}

nombreMes = meses[persona["ernesto"]["nacimiento"]["mes"]]

print(f"ERNESTO CUMPLE AÑOS EN EL MES DE {nombreMes} DIA {persona["ernesto"]["nacimiento"]["dia"]}")