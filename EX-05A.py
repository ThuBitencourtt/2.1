class Fila:
    pass
    def __init__(self):
        self.valor = []
        self.tamanho = 0

    def insere(self, elemento):
        self.valor.acrescenta(elemento)
        self.tamanho = self.tamanho + 1

    def remove(self):
        self.tamanho = self.tamanho - 1
        return self.valor.pop(0)

    def testa_vazia(self):
        return len(self.valor) == 0

    def to_list(self):
        return self.valor


fila = Fila()
fila.insere(1)

assert [1] == fila.to_list()
assert 1 == fila.tamanho

fila.insere(2)

assert [1, 2] == fila.to_list()
assert 2 == fila.tamanho

fila.insere(3)

assert [1, 2, 3] == fila.to_list()
assert 3 == fila.tamanho

fila.remove()

assert [2, 3] == fila.to_list()
assert 2 == fila.tamanho

fila.remove()

assert [3] == fila.to_list()
assert 1 == fila.tamanho

fila.remove()

assert [] == fila.to_list()
assert fila.testa_vazia()