# Atividade de Linguagens de Programação
## Introdução à Depuração

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
