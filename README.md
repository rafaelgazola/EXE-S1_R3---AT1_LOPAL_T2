



# 🐍 AT2 — Exercícios de Lógica de Programação em Python

Repositório com as resoluções dos exercícios da **Atividade 2 (AT2)** da disciplina de Lógica de Programação (SENAI), cobrindo estruturas de repetição (`for`, `while`), condicionais, listas, dicionários e manipulação de strings.

---

## 📁 Estrutura do Repositório

```
📦 S1_R3_AT2_LOPAL
 ┣ 📄 Exe.1.py
 ┣ 📄 Exe.2.py
 ┣ 📄 Exe.3.py
 ┣ 📄 Exe.4.py
 ┣ 📄 Exe.5.py
 ┣ 📄 Exe.6.py
 ┣ 📄 Exe.7.py
 ┣ 📄 Exe.8.py
 ┣ 📄 Exe.9.py
 ┣ 📄 Exe.10.py
 ┣ 📄 Exe.11.py
 ┗ 📄 README.md
```



## 📝 Descrição dos Exercícios


### Exercício 01 — Par ou Ímpar (`Exe.1.py`)

Percorre todos os números de **0 a 100** usando um laço `for` e, para cada número, verifica se ele é **par ou ímpar** com o operador módulo (`%`), exibindo a classificação de cada um.

> Conceitos: `for`, `if/else`, operador `%`, `range()`, `format()`

<img width="930" height="283" alt="image" src="https://github.com/user-attachments/assets/23522384-dc8e-431a-bfb0-acc0b5922b9c" />


---

### Exercício 02 — Maior e Menor Valor (`Exe.2.py`)

Solicita ao usuário **três números inteiros**, armazena-os diretamente em uma lista e utiliza as funções nativas `max()` e `min()` para identificar e exibir de forma direta o **maior** e o **menor** valor digitado.

> Conceitos: `input()`, listas, `max()`, `min()`, f-strings

<img width="873" height="373" alt="image" src="https://github.com/user-attachments/assets/0be0933c-a0bd-4d25-a6d4-2a27cc41a11e" />


---

### Exercício 03 — Fatiamento Progressivo de String (`Exe.3.py`)

Recebe o nome digitado pelo usuário, converte todas as letras para maiúsculas com o método `.upper()` e utiliza um laço `for` junto com a função `len()` para realizar um fatiamento progressivo (`nome[:i]`), imprimindo o nome em formato de escada com um pequeno delay visual via `time.sleep()`.

> Conceitos: `input()`, `.upper()`, `for`, `range()`, `len()`, slicing de strings, `time.sleep()`

<img width="936" height="296" alt="image" src="https://github.com/user-attachments/assets/4d9a6248-ba18-4743-b113-d7ac4e2fb983" />


---

### Exercício 04 — Sequência de Fibonacci (`Exe.4.py`)

Gera a **sequência de Fibonacci** até a quantidade de termos informada pelo usuário. Utiliza um laço `for` para repetir o ciclo e variáveis auxiliares (`penultimo`, `ultimo`, `proximo`) que realizam a somatória matemática necessária para atualizar os valores a cada iteração.

> Conceitos: `input()`, `for`, `range()`, variáveis de controle, f-strings

<img width="949" height="386" alt="image" src="https://github.com/user-attachments/assets/47934be1-7a99-41c6-b19a-b1722d816a1d" />


---

### Exercício 05 — Validação de Cadastro (`Exe.5.py`)

Formulário de cadastro interativo que utiliza laços `while` independentes para aplicar regras de validação em tempo real. O programa impede o avanço do fluxo até que o usuário insira um dado válido:

| Campo | Regra de validação no código |
|---|---|
| Nome | Deve ter mais de 3 caracteres (`len(name) <= 3` repete) |
| Idade | Deve ser menor que 151 anos (`idade >= 151` repete) |
| Salário | Deve ser um valor maior que zero (`salario <= 0` repete) |
| Gênero | Aceita estritamente as opções `f` ou `m` |
| Estado Civil | Aceita estritamente as opções `s`, `c`, `v` ou `d` |

Ao final, exibe um resumo completo com todos os dados cadastrados no sistema.

> Conceitos: `while`, operadores lógicos (`and`, `!=`), `len()`, conversão de tipos (`int`, `float`), f-strings

<img width="1005" height="836" alt="image" src="https://github.com/user-attachments/assets/4385732c-9d17-4482-8569-0b10b4dafb11" />


---

### Exercício 06 — Verificador de Número Primo (`Exe.6.py`)

Verifica se um número inteiro informado pelo usuário é **primo**. Utiliza um laço `for` que percorre de 1 até o número digitado incrementando um contador toda vez que a divisão tem resto zero (`inteiro % i == 0`). Se ao final o número de divisões for igual a 2, confirma que ele é primo.

> Conceitos: `input()`, `for`, `range()`, `if/else`, operador módulo (`%`), contadores

<img width="947" height="325" alt="image" src="https://github.com/user-attachments/assets/cd115b4d-ce22-4df3-9076-de3b104e00c0" />


---

### Exercício 07 — Fatorial (`Exe.7.py`)

Calcula o **fatorial** do número inteiro digitado pelo usuário. Utiliza uma variável acumuladora inicializada em 1 (`fatorial = 1`) e, por meio de um laço `for`, multiplica sequencialmente todos os valores contidos no intervalo de 1 até o número fornecido.

> Conceitos: `input()`, `for`, `range()`, operadores aritméticos de atribuição cumulativa

<img width="931" height="228" alt="image" src="https://github.com/user-attachments/assets/9dedd581-5a78-49ae-8819-9a9443a5b4ae" />


---

### Exercício 08 — Funções Nativas de Lista (`Exe.8.py`)

Demonstra a aplicação prática das principais **funções nativas do Python** para análise e manipulação de uma lista pré-definida `L = [5, 7, 2, 9, 4, 1, 3]`:

- `len(L)`: Retorna a quantidade de elementos.
- `max(L)`: Identifica o maior elemento.
- `min(L)`: Identifica o menor elemento.
- `sum(L)`: Realiza a somatória de todos os itens.
- `sorted(L, reverse=True)`: Organiza e imprime a lista em ordem decrescente.
- `sorted(L)`: Organiza e imprime a lista em ordem crescente.

> Conceitos: listas, funções embutidas (`len`, `max`, `min`, `sum`), ordenação com `sorted()`

<img width="938" height="237" alt="image" src="https://github.com/user-attachments/assets/16cbbb2d-af79-49b3-b5a1-35f12fc5a29e" />


---

### Exercício 09 — Dicionário de Lanchonete (`Exe.9.py`)

Estrutura o cardápio de uma lanchonete utilizando um **dicionário** (`dict`), onde associa o nome dos produtos (chaves) aos seus respectivos preços (valores). Para garantir uma exibição organizada e legível no terminal, faz uso da função `pprint` (Pretty Print).

| Produto (Chave) | Preço (Valor) |
|---|---|
| Salgado | R$ 4.50 |
| Lanche | R$ 6.50 |
| Suco | R$ 3.00 |
| Refrigerante | R$ 3.50 |
| Doce | R$ 1.00 |

> Conceitos: dicionários (`dict`), mapeamento de chave-valor, biblioteca `pprint`

<img width="940" height="203" alt="image" src="https://github.com/user-attachments/assets/867fa337-afdd-4419-ab7f-465b1fa3257e" />

---

### Exercício 10 — Sistema de Senha (`Exe.10.py`)

Garante o controle de acesso numérico utilizando um laço de repetição `while`. O programa estabelece uma senha padrão obrigatória (`676767`) e mantém o usuário preso no loop exibindo uma mensagem de erro até que a entrada correta seja digitada.

> Conceitos: laço `while`, operadores de comparação (`!=`), entrada de dados, fluxo condicional

<img width="930" height="235" alt="image" src="https://github.com/user-attachments/assets/175fd5a5-4b7d-4ee2-921a-789e86ef39be" />

---

### Exercício 11 — Tabuada (`Exe.11.py`)

Solicita um número inteiro ao usuário e exibe sua **tabuada completa** de 1 a 10. O cálculo da multiplicação é feito dinamicamente em cada iteração dentro de um laço `for` e impresso de forma organizada na tela.

> Conceitos: `input()`, `for`, `range()`, operações aritméticas, f-strings

<img width="933" height="218" alt="image" src="https://github.com/user-attachments/assets/68aa12dc-bf04-4bca-8124-a2b88fa7b307" />

---

## 🛠️ Como Executar

Certifique-se de ter o **Python 3** instalado. Para rodar qualquer exercício, abra o terminal na pasta do projeto e execute:

```bash
python Exe.1.py
```

<div style="text-align: center;">
    FEITO POR GAZOLA
</div>


