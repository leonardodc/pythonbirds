"""
Você deve criar uma classe carro que vai possuir 2 atributos compostos por outras 2 classes:

1 - Motor
2 - Direção

O Motor terá a responsábilidade de controlar a velocidade
Ele oferece os seguinte atributos:
1 - Atributo de dado Velocidade
2 - Método Acelerar que deverá incrementar a velocidade de uma unidade
3 - Método Frear que deverá decrementar a velocidade em 2 unidades

A Direção tera a responsábildiade de controlar a direção.
Ela oferece os seguintes atributos:
1 - Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste
2 - Método girar_a_direita
3 - Método girar_a_esquerda

  N
O   L
  S
"""
# Exemplo:
# testando Motor  

class Carro():
  def __init__(self, direcao, motor):
    self.direcao = direcao
    self.motor = motor
  
  def calcular_velocidade(self):
    return self.motor.velocidade

  def acelerar(self):
    self.motor.acelerar()

  def frear(self):
    self.motor.frear()

  def calcular_direcao(self):
    return self.direcao.valor

  def girar_a_direita(self):
    self.direcao.girar_a_direita()

  def girar_a_esquerda(self):
    self.direcao.girar_a_esquerda()

class Motor:
  def __init__(self):
    self.velocidade = 0

  def acelerar(self):
    self.velocidade += 1

  def frear(self):
    self.velocidade -= 2
    self.velocidade = max(0, self.velocidade)

direcoes = ['Norte', 'Leste', 'Sul', 'Oeste']

class Direcao:
  def __init__(self):
    self.valor = 'Norte'

  def girar_a_direita(self):
    index = direcoes.index(self.valor)
    if index == len(direcoes) - 1:
      self.valor = direcoes[0]
    else:
      self.valor = direcoes[index + 1]

  def girar_a_esquerda(self):
    index = direcoes.index(self.valor)
    if index == 0:
      self.valor = direcoes[len(direcoes) - 1]
    else:
      self.valor = direcoes[index - 1]

motor = Motor()
print(motor.velocidade)
# 0
motor.acelerar()
print(motor.velocidade)
# 1
motor.acelerar()
print(motor.velocidade)
# 2
motor.acelerar()
print(motor.velocidade)
# 3
motor.frear()
print(motor.velocidade)
# 1
motor.frear()
print(motor.velocidade)
# 0

# testando Direção    
direcao = Direcao()
print(direcao.valor)
# 'Norte'
direcao.girar_a_direita()
print(direcao.valor)
# 'Leste'
direcao.girar_a_direita()
print(direcao.valor)
# 'Sul'
direcao.girar_a_direita()
print(direcao.valor)
# 'Oeste'
direcao.girar_a_direita()
print(direcao.valor)
# 'Norte'
direcao.girar_a_esquerda()
print(direcao.valor)
# 'Oeste'
direcao.girar_a_esquerda()
print(direcao.valor)
# 'Sul'
direcao.girar_a_esquerda()
print(direcao.valor)
# 'Leste'
direcao.girar_a_esquerda()
print(direcao.valor)
# 'Norte'

carro = Carro(direcao, motor)
print(carro.calcular_velocidade())
# 0
carro.acelerar()
print(carro.calcular_velocidade())
# 1
carro.acelerar()
print(carro.calcular_velocidade())
# 2
carro.frear()
print(carro.calcular_velocidade())
# 0

print(carro.calcular_direcao())
# 'Norte'
carro.girar_a_direita()
print(carro.calcular_direcao())
# 'Leste'
carro.girar_a_esquerda()
print(carro.calcular_direcao())
# 'Norte'
carro.girar_a_esquerda()
print(carro.calcular_direcao())
# 'Oeste'
