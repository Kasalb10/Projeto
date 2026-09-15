import winsound

class Entidade:

    def __init__(self, nome: str, vida: int):
        self.nome = nome
        self.vida = max(0, vida)
        self.vida_maxima = vida
        self.estavivo = self.vida > 0

    def receber_dano(self, dano: int) -> int:
        if not self.estavivo:
            print(f"{self.nome} já está derrotado.")
            return 0

        dano_real = min(dano, self.vida)
        self.vida -= dano_real

        if self.vida <= 0:
            self.vida = 0
            self.estavivo = False
            print(f"{self.nome} PERDEU!")
        else:
            print(f"{self.nome} recebeu {dano_real} de dano. Vida: {self.vida}")

        return dano_real

    def curar(self, quantidade: int) -> None:
        if not self.estavivo:
            print(f"{self.nome} está morto e não pode ser curado.")
            return

        self.vida = min(self.vida + quantidade, self.vida_maxima)
        print(f"{self.nome} foi curado. Vida: {self.vida}")

    def esta_vivo(self) -> bool:
        return self.estavivo

    def __str__(self):
        status = "vivo" if self.estavivo else "derrotado"
        return f"{self.nome} ({status}) - Vida: {self.vida}/{self.vida_maxima}"


class Personagem(Entidade):

    def __init__(self, nome: str, vida: int):
        super().__init__(nome, vida)

        print(f"{self.nome} não possui música tema definida.")


class Musica:

    def __init__(self, titulo: str, artista: str):
        self.titulo = titulo
        self.artista = artista

        
        mucica = "videoplayback.wav"
        winsound.PlaySound(mucica, winsound.SND_FILENAME)

class Inimigo(Entidade):

    def __init__(self, nome: str, vida: int, dano: int):
        super().__init__(nome, vida)
        self.dano = dano
        self.musica_tema = None

    def adicionar_musica_tema(self, musica: Musica) -> None:
        self.musica_tema = musica
        print(f"Música tema de {self.nome} definida como: {musica.titulo}")

    def tocar_musica_tema(self, musica: Musica = None) -> None:
        m = musica or self.musica_tema
        if m:
            print(f"Tocando tema de {self.nome}: {m.titulo} - {m.artista}")
        else:
            print(f"{self.nome} não possui música tema definida.")
        mucica = "videoplayback.wav"
        winsound.PlaySound(mucica, winsound.SND_FILENAME)

    def atacar(self, alvo: Entidade) -> None:
        if not self.estavivo:
            print(f"{self.nome} está derrotado e não pode atacar.")
            return
        print(f"{self.nome} ataca {alvo.nome}!")
        alvo.receber_dano(self.dano)

    def __str__(self):
        base = super().__str__()
        return f"{base} | Dano: {self.dano}"


argom = Personagem("Argom", 100)
orc = Inimigo("Orc Selvagem", 80, 15)

print(argom)
print(orc)
print()

orc.atacar(argom)
argom.receber_dano(35)

orc.atacar(argom)
argom.receber_dano(50)

argom.curar(20)
argom.curar(100)

print()
print(argom)
print(orc)

musica1 = Musica("War Pigs", "Black Sabbath")
falcao = Inimigo("Falcão", 80, 15)

falcao.adicionar_musica_tema(musica1)
falcao.tocar_musica_tema()


