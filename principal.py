from clases.vehiculos import Auto, Moto, Concesionaria

ford_ka = Auto('Forf Ka', 'Rojo', 4, 5)
toyota_ethios = Auto('Toyota Ethios', 'Blanco', 4, 4)

moto_enduro = Moto('Yamaha', 'Gris', 2, 4)

concesionaria = Concesionaria(ford_ka, toyota_ethios, moto_enduro)

for clave, valor in concesionaria.total_vehiculos_por_tipo().items():
    print(f"Tipo Vehiculo: {clave}, cantidad en stock: {valor}")


print(concesionaria.catalogar(4))
