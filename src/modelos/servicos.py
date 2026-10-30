from abc import ABC, abstractmethod

class Servico(ABC):
    """Define o que todos os serviços do pet shop devem ter."""

    def __init__(self, nome:str) -> None:
        self.nome_servico = nome


    @abstractmethod
    def calcular_preco(self) -> float:
        """Retorna o preço do serviço e obriga as subclasses
        a utilizarem esse atributo."""
        pass

    def __str__(self) -> str:
        """Retorna o nome e o preço do serviço."""
        return f"{self.nome_servico} - R$ {self.calcular_preco():.2f}"


class Banho(Servico):
    """Representa o serviço de banho."""

    PRECO = 40.0

    def __init__(self) -> None:
        super().__init__("Banho")

    def calcular_preco(self) -> float:
        """Retorna o preço do banho. Uso do Polimorfismo."""
        return self.PRECO

class Tosa(Servico):
    """ Retorna o serviço de tosa """

    PRECO = 65.0

    def __init__(self) -> None:
        super().__init__("Tosa")

    def calcular_preco(self) -> float:
        """Retorna o preço da tosa. Uso do Polimorfismo."""
        return self.PRECO

class Hospedagem(Servico):
    """ Retorna o serviço de hospedagem do pet """
    PRECO_DIARIA = 50.5
    
    def __init__(self) -> None:
        super().__init__("Hospedagem")
        
    def calcular_preco(self) -> float:
        """Retorna o preço da Hospedagem pelo peso. Uso do Polimorfismo."""
        return self.PRECO_DIARIA

def listar_servicos() -> None:
    servicos: list[Servico] = [Banho(), Tosa(), Hospedagem()]
    print(f"""
    {'=' * 10} SERVIÇOS DO PET SHOP {'=' * 10}
    """)
    for numero, servico in enumerate(servicos, start=1):
        print(f"""
            {numero} - {servico}
            """)
        """
        Uso do Polimorfismo para percorrer os três objetos
        em uma mesma lista e cada um exibe seu valor.
        """