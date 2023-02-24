import os
import sys
from unittest import TestCase
from oo.carro import Motor


project_dir = os.path.join(os.path.dirname(__file__), '..')
project_dir = os.path.normpath(project_dir)
sys.path.append(project_dir)

class CarroTestCase(TestCase):
    def teste_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0,motor.velocidade)

    def teste_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)

### $ python -m unittest discover pasta
### ou tira o pasta e roda dentro da pasta
### rodar dentro da pasta
