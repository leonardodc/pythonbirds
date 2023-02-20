class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
        
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    leo = Pessoa(nome = 'Leo')
    carlos = Pessoa(leo, nome = 'Carlos')
    print(Pessoa.cumprimentar(carlos))
    print(id(carlos))
    print(carlos.cumprimentar())
    print(carlos.nome)
    print(carlos.idade)
    for filho in carlos.filhos:
        print(f'filhos do for: {filho.nome}')
    
    # Adicionando um atributo dinamico no objeto de carlos. 
    # Não influencia no objeto leo
    carlos.sobrenome = 'Silva'
    del carlos.filhos # possivel remover um atributo
    print(carlos.__dict__)
    print(leo.__dict__)


