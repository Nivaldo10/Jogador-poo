from jogadorGoleiro import JogadorGoleiro
from jogadorLinha import JogadorLinha
from time_futebol import TimeFutebol

time1 = TimeFutebol("Corinthians")

jogador1 = JogadorGoleiro("Hugo Sousa", 196, 60, 60, 50, 70)
jogador2 = JogadorLinha("Menphis", 178, 80, 50, 85, 90)
jogador3 = JogadorLinha("Romero", 175, 85, 40, 80, 85)

time1 = TimeFutebol("Corinthians")
time1.adicionar_jogador(jogador1)
time1.adicionar_jogador(jogador2)
time1.adicionar_jogador(jogador3)
print("\n")
time1.listar_jogadores()

print("\nRealizando ações dos jogadores:")
jogador1.agarrar()
jogador2.chutar()
jogador3.defender()

print("\nRemovendo um jogador:")
time1.remover_jogador("Romero")
print("\n")
time1.listar_jogadores()

print("\nInformações do time:")
print(time1)