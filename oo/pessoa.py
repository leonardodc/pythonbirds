class Pessoa:

    olhos = 2
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
        
    def cumprimentar(self):
        return f'Olá {id(self)}'
    
    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos { cls.olhos}'    

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

    # Atributo de Classe
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    carlos.olhos = 2
    
    print(carlos.olhos)
    print(leo.olhos)
    del carlos.olhos
    print(carlos.olhos)

    #Método de Classe
    print(Pessoa.metodo_estatico(), carlos.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), carlos.nome_e_atributos_de_classe())
