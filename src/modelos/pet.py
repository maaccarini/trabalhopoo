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
        self._nome =  nome
        self._especie = especie
        self._porte = self.validar_porte(porte)
        self._tutor = tutor
        
    @property
    def porte(self):
        return self._porte
    
    @porte.setter
    def alterar_porte(self, porte : str):
        self.validar_porte
    
    def validar_porte(self, porte : str) -> None :
        if porte.upper() not in PORTE.values():
            print(f"Não é possível definir o porte deste valor, tente: {PORTE.values()}")
        self._porte = porte.upper()
    
    def __str__(self) -> str:
        return f"{self._id_pet} - {self._nome} - {self._especie} sob cuidados do {self._tutor}"
    
def cadastrar_pet() -> None:
    nome_pet = input("Digite o nome do pet: ")
    espec_pet = input("Digite a especie do pet: ")
    porte_pet = input("Pequeno, médio ou grande: ")
    tutor_nome_pet = input("Digite o nome do tutor: ")
    tutor_telefone_pet = input("Digite o telefone do tutor: ")
    tutor_pet : Tutor = Tutor(tutor_nome_pet, tutor_telefone_pet)
    novo_pet : Pet = Pet(nome_pet, espec_pet, porte_pet, tutor_pet)
    pets.append(novo_pet)