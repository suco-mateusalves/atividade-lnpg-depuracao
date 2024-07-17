def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)  # bug: cálculo da média.

def find_max(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

def get_numbers():
    numbers = input("Enter numbers separated by spaces: ").split()
    numbers = [int(num) for num in numbers]  # bug: conversão de string para inteiro.
    return numbers

def main():
    numbers = get_numbers()
    if numbers:  # big: Verifica se a lista não está vazia.
        print("Average:", calculate_average(numbers))
        print("Maximum:", find_max(numbers))
    else:
        print("No numbers entered.")  # bug: mensagem para caso de entrada vazia.

if __name__ == "__main__":
    main()
