#fijamos el costo de mantencion de la tarjeta en UF
UFHoy = 39.179
COSTO_MANTENCION_UF = 0.04
#definimos la clase TarjetaCredito
class TarjetaCredito:
    todas_las_tarjetas = [] #atributo de clase
    def __init__(self, limite_credito=100.000, intereses=0.0, saldo_pagar=0):
        self.saldo_pagar = saldo_pagar + (UFHoy*0.04)
        self.limite_credito = limite_credito
        self.intereses = intereses
        self.id = len(TarjetaCredito.todas_las_tarjetas)+1
        TarjetaCredito.todas_las_tarjetas.append(self)
        print("Tarjeta creada con exito!")
#definimos los metodos de la clase
    def compra(self, monto, cuotas):
        if self.saldo_pagar + monto > self.limite_credito:
            print("No puedes exceder el limite de credito")
        else:
            if (cuotas > 3):
                self.saldo_pagar += monto*(1+self.intereses)
            else:
                self.saldo_pagar += monto  # sin interes
        return self
#definimos el metodo pago
    def pago(self, monto):
        self.saldo_pagar = self.saldo_pagar - monto
        return self
#definimos el metodo mostrar_info_tarjeta
    def mostrar_info_tarjeta(self):
        print("\nMostrando informacion de tarjeta de Credito")
        print("=" * 20)
        print(f"Saldo a pagar: ${self.saldo_pagar}")
        print(f"Limite de credito: ${self.limite_credito}")
        print(f"Intereses: {self.intereses*100}%")
        print("=" * 20)
        return self
#definimos el metodo para cobrar interes
    def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar * self.intereses
        return self
#definimos el metodo para mostrar informacion de todas las tarjetas creadas
    @classmethod
    def info_todas_tarjetas(cls):
        total_saldos = 0
        print("Informacion de todas las tarjetas:")
        print("="*40)
        for tarjeta in cls.todas_las_tarjetas: 
            print("ID:",tarjeta.id)
            print("SALDO:",tarjeta.saldo_pagar)
            print("CREDITO:",tarjeta.limite_credito)
            print("INTERES:",tarjeta.intereses)
            print("-"*40)
#definimos el metodo para mostrar el total de saldos
tarjeta1=TarjetaCredito(limite_credito=300.000,intereses=0.01)
tarjeta2=TarjetaCredito(limite_credito=200.000,intereses=0.01)
tarjeta3=TarjetaCredito(limite_credito=150.000,intereses=0.01)
tarjeta1.compra(16.000,4).compra(20.000,2).pago(25.000).mostrar_info_tarjeta()
tarjeta2.compra(2000,1).compra(12.000,2).compra(20.000,4).pago(5000).pago(15.000).cobrar_interes().mostrar_info_tarjeta()
tarjeta3.compra(10.000,1).compra(20.000,2).compra(10.000,3).compra(65.000,5).compra(50.000,7).mostrar_info_tarjeta()
print("*"*40)
print(TarjetaCredito.info_todas_tarjetas())