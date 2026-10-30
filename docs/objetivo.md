Trabalho
# 📘 Descritivo do Trabalho – Programação Orientada a Objetos


## 🎯 Objetivo

Modelar um **cenário do mundo real** em classes e objetos, aplicando os princípios da Orientação a Objetos estudados na disciplina, e disponibilizar um **sistema interativo via terminal** (menu em prompt) que permita ao usuário cadastrar, consultar e executar as operações do cenário.

O grupo deverá:

1. **Mapear as entidades** do cenário escolhido (quem são os "objetos" do problema, quais dados possuem e o que sabem fazer).
2. **Desenhar o modelo** (diagrama de classes simples) mostrando atributos, métodos e relacionamentos. (opcional)
3. **Implementar** o modelo em Python, aplicando os conceitos de POO.
4. **Criar um terminal interativo** (`input()` / `print()`) para operar o sistema.

---

## 🏫 Exemplo de Mapeamento — Cenário "Escola"

> ⚠️ Este cenário é **apenas um exemplo** para orientar o raciocínio. Ele **não deve** ser escolhido pelos grupos.

**Enunciado:** uma escola possui pessoas (alunos e professores), disciplinas e turmas. Professores lecionam disciplinas; alunos se matriculam em turmas e recebem notas. A escola precisa consultar boletins e a situação de cada aluno.

**Identificar as entidades (substantivos do enunciado):**

| Entidade | Atributos | Comportamentos (métodos) |
|---|---|---|
| `Pessoa` *(abstrata)* | nome, cpf, email | `apresentar()` *(abstrato)* |
| `Aluno` *(herda de Pessoa)* | matrícula, notas | `media` *(property calculada)*, `situacao()`, `apresentar()` |
| `Professor` *(herda de Pessoa)* | registro, salário, disciplinas | `atribuir_disciplina()`, `apresentar()` |
| `Disciplina` | código, nome, carga horária | `__str__()` |
| `Turma` | código, disciplina, professor, alunos | `matricular()`, `lancar_nota()`, `boletim()` |
| `Escola` | nome, pessoas, turmas | `cadastrar()`, `buscar_por_cpf()`, `listar()` |

**Identificar os relacionamentos:**

```
               Pessoa (ABC)
              /            \
          Aluno          Professor            → Herança ("é um")

Escola ◆── Turma ◆── Aluno                    → Composição ("tem um / possui")
              └──── Professor
              └──── Disciplina
```


**Terminal interativo (exemplo de execução esperada):**

```
========== SISTEMA ESCOLAR ==========
1 - Cadastrar aluno
2 - Cadastrar professor
3 - Criar turma
4 - Matricular aluno em turma
5 - Lançar nota
6 - Listar pessoas
7 - Emitir boletim da turma
0 - Sair
Escolha uma opção: 5
Código da turma: POO-2026
CPF do aluno: 12345678901
Nota: 11
❌ Nota 11.0 inválida. Use valores de 0 a 10.

Escolha uma opção: 6
🎓 Aluno Maria (Mat: 2026001) - Média: 8.5
👨‍🏫 Professor Carlos (Reg: P-104) - Disciplinas: POO, Banco de Dados
```
---

## 🗂️ Cenários Disponíveis

Cada grupo deve escolher **um cenário diferente**. Grupos podem propor um cenário próprio, desde que tenha complexidade equivalente.

| # | Cenário | Entidades sugeridas (mínimo) | Ideia de polimorfismo / hierarquia |
|---|---|---|---|
| 1 | **Clínica Veterinária** | Animal, Cachorro, Gato, Ave, Tutor, Veterinário, Consulta | Cada animal calcula o valor da consulta / vacinas de forma diferente |
| 2 | **Academia** | Pessoa, Aluno, Instrutor, Plano (Mensal, Trimestral, Anual), Treino | Cada plano calcula mensalidade e desconto de forma diferente |
| 3 | **Hotel** | Hóspede, Quarto (Standard, Luxo, Suíte), Reserva, Funcionário | Cada quarto calcula a diária e os serviços inclusos |
| 4 | **Locadora de Veículos** | Cliente, Veículo (Carro, Moto, Caminhão), Locação | Cada veículo calcula o valor do aluguel e a exigência de CNH |
| 5 | **Restaurante / Delivery** | Cliente, Pedido, ItemCardápio (Prato, Bebida, Sobremesa), Entregador | Cada item calcula preço/taxa; tipos de entrega (retirada, moto, app) |
| 6 | **Cinema** | Filme, Sala (2D, 3D, IMAX), Sessão, Ingresso (Inteira, Meia), Cliente | Cada ingresso/sala calcula o preço final |
| 7 | **Oficina Mecânica** | Cliente, Veículo, Mecânico, OrdemServiço, Serviço (Revisão, Funilaria, Elétrica) | Cada serviço calcula mão de obra e prazo |
| 8 | **Hospital / Pronto-Socorro** | Pessoa, Paciente, Médico, Enfermeiro, Atendimento, Triagem | Cada nível de triagem define prioridade na fila |
| 9 | **Eventos e Ingressos** | Evento (Show, Palestra, Esportivo), Participante, Ingresso, Organizador | Cada evento calcula lotação, preço e regras de acesso |
| 10 | **Estacionamento** | Veículo (Carro, Moto, Utilitário), Vaga, Ticket, Mensalista, Avulso | Cada tipo de cliente/veículo calcula a cobrança |
| 11 | **Pet Shop / Hotel para Pets** | Pet, Tutor, Serviço (Banho, Tosa, Hospedagem), Agendamento | Cada serviço calcula preço por porte do animal |
| 12 | **Companhia Aérea** | Passageiro, Voo, Assento (Econômica, Executiva, Primeira), Reserva | Cada classe calcula tarifa e franquia de bagagem |

---

## 🧩 Requisitos Técnicos

### Requisitos de Orientação a Objetos (obrigatórios)

Cada item abaixo deve aparecer **pelo menos uma vez** no código e o grupo deve saber **apontar onde** durante a apresentação.

| # | Conceito |  O que se espera |
|---|---|---|---|
| R1 | **Classes e objetos** | No mínimo **4 classes** de domínio (sem contar exceções e o menu) com `__init__` e `self` |
| R2 | **Composição** | Objetos que contêm outros objetos (ex.: `Turma` possui lista de `Aluno`) |
| R3 | **Encapsulamento** | Atributos protegidos (`_attr`) e/ou privados (`__attr`) acessados apenas via métodos/properties |
| R4 | **Métodos de classe e estáticos** | Pelo menos um `@classmethod` (ex.: construtor alternativo `from_string`, contador) e um `@staticmethod` (ex.: validador) |
| R5 | **Properties** | `@property` com **setter validando dados** e pelo menos uma **property calculada** |
| R6 | **Atributos de classe** | Constantes ou contadores compartilhados (ex.: `LIMITE_VAGAS`, `total_criados`) |
| R7 | **Herança e `super()`** | Pelo menos **uma hierarquia** com 1 classe base e **no mínimo 2 subclasses** |
| R8 | **Sobrescrita e polimorfismo** | Métodos reescritos nas subclasses e chamados de forma uniforme (ex.: loop sobre uma lista mista) |
| R9 | **Classe abstrata** | Uso de `ABC` e `@abstractmethod` definindo o contrato da hierarquia |
| R10 | **Interface / Protocol** | Pelo menos um `Protocol` (ex.: `Pagavel`, `Exportavel`, `Notificavel`) usado por classes **sem relação de herança** 

### Requisitos do Terminal Interativo

- Menu principal em loop com opção **Sair**.
- No mínimo **5 opções funcionais**, contemplando:
  - **Cadastrar** pelo menos 2 tipos de entidade diferentes;
  - **Listar / consultar** (incluindo uma listagem polimórfica);
  - **Buscar** um objeto por identificador (código, CPF, placa, etc.);
  - Pelo menos **2 operações de negócio** que relacionem objetos (ex.: matricular, reservar, alugar, fechar conta, lançar nota);
  - Pelo menos **1 relatório / cálculo** (ex.: faturamento do dia, boletim, ranking, ocupação).
- O sistema deve iniciar com alguns **dados de exemplo** já carregados (para agilizar a demonstração).
- As regras de negócio **devem estar nas classes de domínio**, não no menu. O menu apenas lê os dados, chama os métodos e exibe o resultado/erros.

### Organização do Código

Estrutura sugerida (pode ser adaptada):

```
trabalho-poo/
├── README.md
├── docs/
│   └── diagrama-classes.png      # ou .md com diagrama em texto / Mermaid
├── src/
│   ├── main.py                   # ponto de entrada: python src/main.py
│   ├── menu.py                   # terminal interativo
│   ├── excecoes.py               # exceções customizadas (opctional)
│   ├── interfaces.py             # Protocols
│   └── modelos/
│       ├── __init__.py
│       ├── pessoa.py
│       └── ...
```

- Usar **type hints** e **docstrings** nas classes e métodos públicos (padrão das aulas).
- Nomes de classes em `PascalCase`.
- Não utilizar bibliotecas externas (apenas biblioteca padrão do Python).


---

## 📂 Entregáveis

Repositório no GitHub (privado com acesso ao professor fernandodomeneghetti), contendo:

1. **Código-fonte** completo do sistema.
2. **Diagrama de classes** (imagem, Mermaid ou texto) com atributos, métodos, heranças e composições.
3. **README.md** com:
   - Nome dos integrantes;
   - Descrição do cenário e das regras de negócio;
   - Tabela de **mapeamento das entidades** (como no exemplo da Escola);
   - Tabela indicando **onde cada requisito (R1 a R13) foi aplicado** (arquivo + classe/método);
   - Instruções para executar (`python src/main.py`).

---

## 📆 Entrega e Apresentação

**Formato:** Apresentação presencial

**Tempo por grupo:** até 10 minutos

Durante a apresentação:

1. Apresentação rápida do cenário e do **diagrama de classes**.
2. **Demonstração no terminal**: cadastros, operações de negócio, relatório e tratamento de erros (o professor poderá digitar entradas inválidas).
3. **Navegação no código**: o professor poderá apontar requisitos (R1 a R10) e qualquer integrante deverá explicar o trecho correspondente.
4. **Alteração ao vivo**: o professor poderá solicitar uma pequena mudança, por exemplo:
   - criar uma **nova subclasse** na hierarquia (ex.: um novo tipo de quarto/plano/veículo) e mostrá-la funcionando no menu **sem alterar** o código que já usa a classe base;
   - adicionar uma nova regra de negócio com uma **nova exceção**;
   - alterar uma validação em uma property.

---

## 🧑‍🤝‍🧑 Grupos

Cada grupo deve ter **até 5 integrantes**.

Todos os membros devem participar da explicação ou execução durante a apresentação. O histórico de commits do repositório poderá ser consultado.

Trabalho 1 – Trabalho_22123_423_1