from abc import ABC, abstractmethod
from modelos.tutor import Tutor

PORTE : dict[int, str] = {
    1 : "PEQUENO",
    2 : "MEDIO",
    3 : "GRANDE"
}

pets : list[Pet] = []

class Pet(ABC):
    """ Guarda o nome, espécie, porte e tutor que pertence"""
    def __init__(self, nome : str, especie : str, porte : str, tutor : Tutor, peso : float) -> None:
        self._nome =  nome.upper()
        self._especie = especie.upper()
        self._porte = self.validar_porte(self, porte)
        self._tutor = tutor
        self._peso = peso
        
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
    
    @staticmethod
    def procurar_pet(nome_pet : str) -> str :
        """ Procura o pet a partir do nome na lista. """
        for pet in pets:
            if pet._nome == nome_pet.upper():
                return pet
        print("Não encontrado.")
    
    @staticmethod
    def cadastrar_pet(pet_cadastrar : Pet) -> None:
        """ Cadastra um pet (seja que animal for) em uma lista """
        novo_pet : Pet = pet_cadastrar
        pets.append(novo_pet)
    
    def __str__(self) -> str:
        """ Retorna o descritivo do pet junto do animal que é """
        return f"{self.__class__.__name__} com o nome {self.nome} - {self.especie} sob cuidados do {self.tutor}"

class Cachorro(Pet):
    def __init__(self, nome, especie, porte, tutor, peso) -> None:
        super().__init__(nome, especie, porte, tutor, peso)
        self._animal : str = "Cachorro"

class Gato(Pet):
    def __init__(self, nome, especie, porte, tutor, peso) -> None:
        super().__init__(nome, especie, porte, tutor, peso)
        self._animal : str = "Gato"

class Cavalo(Pet):
    def __init__(self, nome, especie, porte, tutor, peso) -> None:
        super().__init__(nome, especie, porte, tutor, peso)
        self._animal : str = "Cavalo"

class Lontra(Pet):
    def __init__(self, nome, especie, porte, tutor, peso) -> None:
        super().__init__(nome, especie, porte, tutor, peso)
        self._animal : str = "Lontra"
        