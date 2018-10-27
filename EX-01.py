class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.area = 0
        self.perimetro = 0

    def mudar_valor_dos_lados(self, valor_x, valor_y):
        self.x = valor_x
        self.y = valor_y

    def retornar_valor_dos_lado(self):
        return self.x
        return self.y

    def calcula_area(self):
        self.area = self.y * self.x
        return self.area

    def calcula_perimetro(self):
        self.perimetro = 2 * (self.x + self.y)
        return self.perimetro


def calculo(self, altura, comprimento):
        result = Retangulo(altura, comprimento)
        rodape = result.calcula_perimetro()
        piso =  result.calcular_area()
              

print(f'Será necessario {rodape(10, 6)} metros quandrados de rodape')
print(f'Será necessario {piso(10, 6)} metros quadrados de piso')
