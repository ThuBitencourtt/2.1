class Pilha:
    pass
    def __init__(self):
        self.valor = []
        self.tamanho = 0

    def empilha(self, elemento):
        self.tamanho = self.tamanho + 1
        self.valor.append(elemento)

    def desempilha(self):
        self.tamanho = self.tamanho - 1
        return self.valor.pop()

    def testa_vazia(self):
        return len(self.valor) == 0

    def to_list(self):
        return self.valor


pilha = Pilha()
pilha.empilha(1)

assert [1] == pilha.to_list()
assert 1 == pilha.tamanho

pilha.empilha(2)

assert [1, 2] == pilha.to_list()
assert 2 == pilha.tamanho

pilha.empilha(3)

assert [1, 2, 3] == pilha.to_list()
assert 3 == pilha.tamanho

assert 3 == pilha.desempilha()
assert [1, 2] == pilha.to_list()
assert 2 == pilha.tamanho

pilha.empilha(5)

assert [1, 2, 5] == pilha.to_list()
assert 3 == pilha.tamanho

assert 5 == pilha.desempilha()
assert [1, 2] == pilha.to_list()
assert 2 == pilha.tamanho

assert 2 == pilha.desempilha()
assert [1] == pilha.to_list()
assert 1 == pilha.tamanho

pilha.empilha(9)

assert [1, 9] == pilha.to_list()
assert 2 == pilha.tamanho