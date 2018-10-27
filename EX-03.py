class carro:
    def __init__(self, consumo):
        self.quantidade = 0
        self.consumo = consumo
    def andar(self, distancia):
        self.quantidade = self.quantidade - (distancia / self.consumo)
    def obter_Gasolina(self, abastecida):
        self.quantidade = self.quantidade + abastecida
    def adicionar_gasolina(meuFusca):
      meuFusca = carro(15)
      meuFusca.quantidade = 20
      meuFusca.andar(100)
print(meuFusca.quantidade)
    