from jogador import Jogador

class TimeFutebol:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []

    def adicionar_jogador(self, jogador):
        if isinstance(jogador, Jogador):
            self.jogadores.append(jogador)
            print(f"{jogador.nome} foi adicionado ao Time {self.nome}.")
        else:
            raise TypeError("O objeto deve ser uma instância de Jogador.")

    def remover_jogador(self, nome_jogador):
        for jogador in self.jogadores:
            if jogador.nome == nome_jogador:
                self.jogadores.remove(jogador)
                print(f"{nome_jogador} foi removido do Time {self.nome}.")
                return
        print(f"Jogador {nome_jogador} não encontrado no Time {self.nome}.")

    def listar_jogadores(self):
        if not self.jogadores:
            print(f"Nenhum jogador no Time {self.nome}.")
        else:
            print(f"Jogadores do Time {self.nome}:")
            for jogador in self.jogadores:
                print(jogador)

    def __str__(self):
        return f"{self.nome}, total de jogadores = {len(self.jogadores)}"
