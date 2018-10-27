class bichinhoVirtual:
    def __init__(self, nome, fome, saude, idade):
         self.nome = nome
         self.fome = 1
         self.saude = saude
         self.idade = idade
    def altera_nome(self, novo_nome):
        self.nome = novo_nome
    def alterar_fome(self, nova_fome):
        self.fome = nova_fome
    def altera_saude(self, nova_saude):
        self.saude = nova_saude
    def altera_idade(self, nova_idade):
        self.idade = nova_idade
    def returnFome(self):
        return self.fome
    def returnSaude(self):
        return self.saude
    def returnIdade(self):
        return self.idade
    def returnHumor(self):
        humor = self.saude - self.fome 
        return humor

teste = bichinhoVirtual(0,0,3,0,)

print(teste.returnHumor())