# O código é dividido em três partes principais: Definição das classes, criação dos objetos e execução das ações

* Definição das classes

No arquivo jogador.py é feito a Superclasse Jogador que representa um jogador genérico, com atributos como nome, altura, velocidade, passe, drible e precisão.

Funcionamento:

O método __init__ é o construtor da classe. Ele inicializa os atributos do jogador quando um objeto é criado.

Os métodos passar(), chutar() e defender() são ações que um jogador pode realizar.

O método __str__ define como o objeto será exibido quando convertido para string (por exemplo, ao usar print(jogador1)).


No arquivo jogadorGoleiro.py é feita a Subclasse JogadorGoleiro que por meio do "import Jogador" herdará  a classe Jogador. Essa classe representa um jogador goleiro, que tem habilidades específicas, como agarrar a bola.

Funcionamento:

O método agarrar() é específico para goleiros.

O método defender() é sobrescrito para incluir lógica específica de goleiros (por exemplo, defender com qualquer parte do corpo dentro da área).

No arquivo jogadorLinha.py é feita a Subclasse JogadorLinha que por meio do "import Jogador" herdará a classe Jogador. Essa classe representa um jogador de linha, que tem habilidades específicas, como defender com os pés, cabeça ou ombro. 

O método defender() é sobrescrito para incluir lógica específica de jogadores de linha (por exemplo, roubar a bola).

No arquivo time_futebol.py foi feito a Subclasse TimeFutebol que por meio do "import Jogador" herdará  a classe Jogador. Essa classe representa um time, que contém uma lista de jogadores.

Funcionamento:

O método __init__ inicializa o nome do time e uma lista vazia de jogadores.

O método adicionar_jogador(jogador) adiciona um jogador à lista, desde que seja uma instância da classe Jogador.

O método remover_jogador(nome_jogador) remove um jogador da lista pelo nome.

O método listar_jogadores() exibe todos os jogadores do time.

O método __str__ define como o objeto Time será exibido quando convertido para string.


* criação dos objetos

No arquivo main.py estará importado as classes JogadorGoleiro, JogadorLinha e TimeFutebol. O main.py vai ser responsavel por criar os objetos jogadores e time

Criando jogadores

jogador1 = JogadorGoleiro("Hugo Sousa", 196, 60, 60, 50, 70):

Cria um objeto da classe JogadorGoleiro com os atributos fornecidos.

O método __init__ da classe Jogador é chamado para inicializar os atributos.

jogador2 = JogadorLinha("Menphis", 178, 80, 50, 85, 90):

Cria um objeto da classe JogadorLinha com os atributos fornecidos.

jogador3 = JogadorLinha("Romero", 175, 85, 40, 80, 85):

Cria outro objeto da classe JogadorLinha.

Criando o time

time1 = TimeFutebol("Corinthians"):

Cria um objeto da classe TimeFuncio com o nome "Corinthians".

O método __init__ da classe Time é chamado para inicializar o nome e a lista vazia de jogadores.

* Execução das ações 

O código simula ações de jogadores em um time de futebol usando métodos específicos de cada classe:

Goleiro: agarrar() → Tenta agarrar a bola.

Jogador de linha: chutar() → Tenta chutar a bola.

Jogador de linha: defender() → Tenta defender a bola.

Jogador de linha: defender() → Tenta defender a bola.

Cada ação usa os atributos do jogador (como força, reflexos, precisão) para determinar o sucesso e exibe uma mensagem correspondente. Por exemplo:

"Hugo Sousa agarrou a bola!"

"Menphis chutou com força!"

"Romero defendeu com sucesso!"

# Resultado esperado

Hugo Sousa foi adicionado ao Time Corinthians.

Menphis foi adicionado ao Time Corinthians.

Romero foi adicionado ao Time Corinthians.


Jogadores do Time Corinthians:

Jogador(nome = Hugo Sousa, altura = 196, velocidade = 60, passe = 60, drible = 50, precisao = 70)

Jogador(nome = Menphis, altura = 178, velocidade = 80, passe = 50, drible = 85, precisao = 90)

Jogador(nome = Romero, altura = 175, velocidade = 85, passe = 40, drible = 80, precisao = 85)


Realizando ações dos jogadores:

Hugo Sousa está tentanto agarrar a bola

Menphis está chutando a bola com força de 100 km/h.

Romero está defendendo com os pés, cabeça ou ombro.

Romero está tentando tirar a bola do adversário.

Removendo um jogador:

Romero foi removido do Time Corinthians.



Jogadores do Time Corinthians:

Jogador(nome = Hugo Sousa, altura = 196, velocidade = 60, passe = 60, drible = 50, precisao = 70)

Jogador(nome = Menphis, altura = 178, velocidade = 80, passe = 50, drible = 85, precisao = 90)


Informações do time:

Corinthians, total de jogadores = 2
