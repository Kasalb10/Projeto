class Entidade:
    
    def __init__(self, nome: str, vida: int):
        self.nome = nome
        self.vida = vida
        self.vida_maxima = vida
        self.estavivo = True

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

from Personagem import Personagem          


class Inimigo(Entidade):
    

    def __init__(self, nome: str, vida: int, dano: int):
        super().__init__(nome, vida)
        self.dano = dano

    def atacar(self, alvo: Entidade) -> None:
        if not self.estavivo:
            print(f"{self.nome} está derrotado e não pode atacar.")
            return
        print(f"{self.nome} ataca {alvo.nome}!")
        alvo.receber_dano(self.dano)

    def __str__(self):
        base = super().__str__()
        return f"{base} | Dano: {self.dano}"

 
from entidade import Personagem, Inimigo

heroi = Personagem("Aragorn", 100)
orc = Inimigo("Orc Selvagem", 80, 15)

print(heroi)
print(orc)
print()


orc.atacar(heroi)
heroi.receber_dano(35)

orc.atacar(heroi)
heroi.receber_dano(50)  

heroi.curar(20)
heroi.curar(100) 

print()
print(heroi)
print(orc)