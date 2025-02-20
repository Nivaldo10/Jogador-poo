class Jogador:
    def __init__ (self, nome, altura, velocidade, passe, drible, precisao):
        self.nome = nome
        self._altura = altura
        self._velocidade = velocidade
        self._passe = passe
        self._drible = drible
        self._precisao = precisao


    def get_altura(self):
        return self._altura

    def set_altura(self, value):
        if value > 0:
            self._altura = value
        else:
            raise ValueError("Altura deve ser maior que 0")

    def passar(self):
        print(f"{self.nome} está passando a bola com força {self._passe}.")

    def chutar(self):
        print(f"{self.nome} está chutando a bola com força de {2 * self._passe} km/h.")

    def defender(self):
        print(f"{self.nome} está tentando tirar a bola do adversário.")

    def __str__(self):
        return (f"Jogador(nome = {self.nome}, altura = {self._altura}, velocidade = {self._velocidade}, "
                f"passe = {self._passe}, drible = {self._drible}, precisao = {self._precisao})")


