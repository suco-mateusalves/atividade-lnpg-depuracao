# Atividade de Linguagens de Programação
## Introdução à Depuração

### problem_01.py
1. Adicionada uma verificação para garantir que a lista numbers não esteja vazia antes de calcular a média e o máximo.
2. Adicionada mensagem para caso de entrada vazia.
3. Correção da forma de cálculo da média.
4. Correção da conversão de string para inteiro.

### problem_02.py
1. Correção feita pra garantir que a janela percorra até o final da matriz, incluindo o último possível subarray de tamanho "k".
2. Adicionada verificação para garantir que a entrada é válida antes de chamar a função max_subarray_sum. Isso evita a chamada da função com listas vazias ou k = 0.

### problem_03.py
1. Correção no loop interno da multiplicação de matrizes.

Antes:
```python
for k in range(cols_B): # Linha 19
```
Depois:
```python
for k in range(cols_A):  # cols_B -> cols_A
```

### problem_04.py
1. Adicionada uma verificação para garantir que o from_account tem saldo suficiente antes de realizar a transferência.

Antes:
```python
def transfer(self, from_account, to_account, amount):
    from_account.withdraw(amount)  
    to_account.deposit(amount)
```
Depois:
```python
def transfer(self, from_account, to_account, amount):
    if from_account.get_balance() >= amount:  # Verificação de saldo antes de transferir
        from_account.withdraw(amount)
        to_account.deposit(amount)
    else:
        print("Transfer failed: Insufficient funds in the source account")
```
