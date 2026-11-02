from modelos.tutor import Tutor

""" Guarda o nome, espécie, porte e tutor """
PORTE : dict[int, str] = {
    1 : "PEQUENO",
    2 : "MEDIO",
    3 : "GRANDE"
}

pets : list[Pet] = []

class Pet():
        
    def __init__(self, nome : str, especie : str, porte : str, tutor : Tutor) -> None:
        self._nome =  nome.upper()
        self._especie = especie.upper()
        self._porte = self.validar_porte(self, porte)
        self._tutor = tutor
        
    @property
    def porte(self) -> str:
        return self._porte
    
    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def especie(self) -> str:
        return self._especie
    
    @property
    def tutor(self) -> Tutor:
        return self._tutor
    
    @porte.setter
    def alterar_porte(self, porte : str):
        self.validar_porte(self, porte)
    
    @staticmethod
    def validar_porte(self, porte : str) -> None :
        if porte.upper() not in PORTE.values():
            print(f"Não é possível definir o porte deste valor, tente: {PORTE.values()}")
        self._porte = porte.upper()
    
    def __str__(self) -> str:
        return f"{self.nome} - {self.especie} sob cuidados do {self.tutor}"
    
def cadastrar_pet() -> None:
    nome_pet : str = input("Digite o nome do pet: ").upper()
    espec_pet : str = input("Digite a especie do pet: ").upper()
    porte_pet : str = input("Pequeno, médio ou grande: ").upper()
    tutor_nome_pet : str = input("Digite o nome do tutor: ")
    tutor_telefone_pet : str = input("Digite o telefone do tutor: ")
    tutor_pet : Tutor = Tutor(tutor_nome_pet, tutor_telefone_pet)
    novo_pet : Pet = Pet(nome_pet, espec_pet, porte_pet, tutor_pet)
    pets.append(novo_pet)

def procurar_pet(nome_pet : str) -> str :
    for pet in pets:
        if pet._nome == nome_pet.upper():
            return pet
            continue
    print("Não encontrado.")
        