from jogador import Jogador

class JogadorGoleiro(Jogador):
    def agarrar(self):
        print(f"{self.nome} está tentanto agarrar a bola")

    def defender(self):
        esta_fora_area = False
        if esta_fora_area:
            print(f"{self.nome} está defendendo com os pés, cabeça ou corpo ")
        else:
            print(f"{self.nome} está defendendo principalmente com as mãos ")
        print(f"{self.nome} está tentando defender o gol")

