class Cliente:
    def __init__(self,__cpf, __nome, __endereco):
        self.cpf = __cpf
        self.nome = __nome
        self.endereco = __endereco

cliente = Cliente(1,'rafa', 'saudade')
cliente.__endereco='prado'
print(cliente.endereco )