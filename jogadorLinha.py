from jogador import Jogador

class JogadorLinha(Jogador):
    def defender(self):
        print(f"{self.nome} está defendendo com os pés, cabeça ou ombro.")
        print(f"{self.nome} está tentando tirar a bola do adversário.")

