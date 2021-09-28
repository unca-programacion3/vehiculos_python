from abc import ABCMeta


class Concesionaria:
    def __init__(self, *vehiculos):
        self.vehiculos = [v for v in vehiculos]

    def total_vehiculos_por_tipo(self):
        total_autos = sum(isinstance(x, Auto) for x in self.vehiculos)
        total_motos = sum(isinstance(y, Moto) for y in self.vehiculos)
        return {'Autos': total_autos, 'Motos': total_motos}

    def catalogar(self, ruedas=None):
        if ruedas:
            contador = 0
            for v in self.vehiculos:
                if v.ruedas == ruedas:
                    contador += 1
            print(f"Se han encontrado {contador} vehiculos con {ruedas} ruedas")

        for v in self.vehiculos:
            if ruedas is None:
                print(type(v).__name__, v)
            else:
                if v.ruedas == ruedas:
                    print(type(v).__name__, v)


class Vehiculo(metaclass=ABCMeta):
    def __init__(self, marca, color, ruedas):
        self.marca = marca
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Marca: {}, color: {}, ruedas: {}".format(self.marca, self.color, self.ruedas)


class Auto(Vehiculo):
    def __init__(self, marca, color, ruedas, puertas):
        super().__init__(marca, color, ruedas)
        self.puertas = puertas

    def __str__(self):
        return super().__str__() + ", puertas: {}".format(self.puertas)


class Moto(Vehiculo):
    CICLOMOTOR = 1
    SCOOTER = 2
    MOTOCROSS = 3
    ENDURO = 4

    TIPO_MOTO = {
        CICLOMOTOR: 'Ciclomotor',
        SCOOTER: 'Scooter',
        MOTOCROSS: 'Motocross',
        ENDURO: 'Enduro'
    }

    def __init__(self, marca, color, ruedas, tipo):
        super().__init__(marca, color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + ", tipo: {}".format(self.TIPO_MOTO[self.tipo])
