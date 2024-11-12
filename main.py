class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, nuevoColor):
        if nuevoColor in ["rojo", "verde", "amarillo", "negro", "blanco",]:
            self.color = nuevoColor



class Auto:
    cantidadCreados = 0

    def __init__(self, modelo, precio, asiento, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = [asiento]
        self.marca = marca
        self.motor = motor
        self.registro = registro
        Auto.cantidadCreados += 1

    def cantidadAsientos(self):
        return sum(1 for asiento in self.asientos if isinstance(asiento, Asiento))

    def verificarIntegridad(self):
        if self.registro != self.motor.registro:
            return "Las piezas no son originales"
            
        for asiento in self.asientos:
            if asiento and self.asientos.registro != self.registro:
                return "Las piezas no son originales"
            return "Auto original"



class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, nuevoRegistro):
        self.registro = nuevoRegistro


    def asignarTipo(self, nuevoTipo):
        if nuevoTipo in ["electrico", "gasolina"]:
            self.tipo = nuevoTipo