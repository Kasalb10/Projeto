# entidade.py

Get-Content "Untitled-1.py" | Select-Object -First 40

class Entidade:
    """Classe base para qualquer ser vivo no jogo."""

    def __init__(self, nome: str, vida: int):
        self.nome = nome
        self.vida = vida
        self.vida_maxima = vida
        self.estavivo = True

    def receber_dano(self, dano: int) -> int:
        """Aplica dano e retorna o dano REAL aplicado."""
        if not self.estavivo:
            print(f"{self.nome} já está derrotado.")
            return 0

        dano_real = min(dano, self.vida)  # não passa do que tem
        self.vida -= dano_real

        if self.vida <= 0:
            self.vida = 0
            self.estavivo = False
            print(f"💀 {self.nome} PERDEU!")
        else:
            print(f"❤️ {self.nome} recebeu {dano_real} de dano. Vida: {self.vida}")

        return dano_real

    def curar(self, quantidade: int) -> None:
        """Cura sem passar do máximo."""
        if not self.estavivo:
            print(f"{self.nome} está morto e não pode ser curado.")
            return

        self.vida = min(self.vida + quantidade, self.vida_maxima)
        print(f"✨ {self.nome} foi curado. Vida: {self.vida}")

    def esta_vivo(self) -> bool:
        return self.estavivo

    def __str__(self):
        status = "vivo" if self.estavivo else "derrotado"
        return f"{self.nome} ({status}) - Vida: {self.vida}/{self.vida_maxima}"


# ---------- Classes filhas ----------

class Personagem(Entidade):

    
    def __init__(self, nome: str, vida: int):
        super().__init__(nome, vida)  # chama o __init__ da classe mãe


class Inimigo(Entidade):
    """Herda tudo de Entidade + tem dano de ataque."""

    def __init__(self, nome: str, vida: int, dano: int):
        super().__init__(nome, vida)
        self.dano = dano

    def atacar(self, alvo: Entidade) -> None:
        if not self.estavivo:
            print(f"{self.nome} está derrotado e não pode atacar.")
            return
        print(f"⚔️ {self.nome} ataca {alvo.nome}!")
        alvo.receber_dano(self.dano)

    def __str__(self):
        base = super().__str__()
        return f"{base} | Dano: {self.dano}"

    # main.py
from entidade import Personagem, Inimigo

heroi = Personagem("Aragorn", 100)
orc = Inimigo("Orc Selvagem", 80, 15)

print("=== BATALHA ===")
print(heroi)
print(orc)
print()

# Turno 1
orc.atacar(heroi)
heroi.receber_dano(35)

# Turno 2
orc.atacar(heroi)
heroi.receber_dano(50)  # Orc morre

# Testa cura
heroi.curar(20)
heroi.curar(100)  # não passa do máximo

print()
print(heroi)
print(orc)