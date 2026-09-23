import random
import time

class Personagem:
    def __init__(self, nome: str, vida: int, forca: int):
        self.nome = nome
        self.vida = vida
        self.forca = forca

    def esta_vivo(self) -> bool:
        "Retorna Verdadeiro se o personagem ainda tiver vida."
        return self.vida > 0

    def receber_dano(self, quantidade_dano: int):
        "Reduz a vida do personagem e impede que ela fique menor que zero."
        self.vida -= quantidade_dano
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nome} recebeu {quantidade_dano} de dano! Vida restante: {self.vida}")

    def atacar(self, alvo) -> int:
        "Método geral de ataque que será personalizado nas classes filhas."
        dano = self.forca + random.randint(1, 5)
        print(f"{self.nome} avança para atacar!")
        alvo.receber_dano(dano)
        return dano


class Heroi(Personagem):
    def __init__(self, nome: str, vida: int, forca: int, classe_heroi: str):
       
        super().__init__(nome, vida, forca)
        self.classe_heroi = classe_heroi  
        self.pocoes = 3

   
    def atacar(self, alvo) -> int:
        dano = self.forca + random.randint(3, 8)  
        print(f"O {self.classe_heroi} {self.nome} golpeia com sua arma!")
        alvo.receber_dano(dano)
        return dano

    def usar_pocao(self):
        "Mecânica exclusiva do herói para recuperar vida."
        if self.pocoes > 0:
            cura = 25
            self.vida += cura
            self.pocoes -= 1
            print(f"{self.nome} tomou uma poção e recuperou {cura} de vida! (Poções restantes: {self.pocoes})")
        else:
            print("Você não tem mais poções!")


class Monstro(Personagem):
    def __init__(self, nome: str, vida: int, forca: int, tipo_monstro: str):
        super().__init__(nome, vida, forca)
        self.tipo_monstro = tipo_monstro  

   
    def atacar(self, alvo) -> int:
        dano = self.forca + random.randint(1, 6)
        print(f"O {self.tipo_monstro} {self.nome} ataca com garras brutas!")
        alvo.receber_dano(dano)
        return dano


if __name__ == "__main__":
        
   
    nome_jogador = input("Digite o nome do seu herói: ")
    heroi = Heroi(nome=nome_jogador, vida=100, forca=10, classe_heroi="Guerreiro")
    monstro = Monstro(nome="Malakar", vida=80, forca=8, tipo_monstro= "Orc")

    print(f"\nUm {monstro.tipo_monstro} selvagem chamado {monstro.nome} apareceu!")
    print(f"Prepare-se, {heroi.nome}!\n")
    
    
    while heroi.esta_vivo() and monstro.esta_vivo():
       
        print("-" * 40)
        print(f"Turno de {heroi.nome} ({heroi.vida} HP) | Inimigo: {monstro.nome} ({monstro.vida} HP)")
        print("1. Atacar")
        print("2. Usar Poção de Vida")
        opcao = input("Escolha sua ação: ")
        print("-" * 40)

        if opcao == "1":
            heroi.atacar(monstro)
        elif opcao == "2":
            heroi.usar_pocao()
        else:
            print("Comando inválido! Você perdeu a oportunidade de agir.")

     
        time.sleep(1.5)

         
        print(f"\nTurno de {monstro.nome}...")
        time.sleep(1)
        monstro.atacar(heroi)
        print()
        time.sleep(1.5)

  
    print("=" * 40)
    if heroi.esta_vivo():
        print(f"PARABÉNS! {heroi.nome} derrotou o {monstro.tipo_monstro} {monstro.nome}!")
    else:
        print(f"GAME OVER! {heroi.nome} foi derrotado por {monstro.nome}.")
    print("=" * 40)
