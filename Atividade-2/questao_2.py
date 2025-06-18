# 2. Escreva uma função que receba uma lista de números e retorne outra lista com 
# os números primos presentes.

def is_prime(number: int) -> bool:
    # Números menores ou iguais a 1 não são primos 
    if number <= 1:
        return False
    # 2 é o único número par que é primo
    if number == 2:
        return True
    # Se o número for par e maior que 2, não é primo.
    if number % 2 == 0:
        return False
    # Se um número não tem nenhum divisor até sua raiz quadrada, 
    # ele não terá divisores maiores,ou seja, é primo. 
    # Portato, se ele tem divisores até sua raiz quadrada ele não é primo
    for divisor in range(3, int(number ** 0.5) + 1, 2):
        if number % divisor == 0:
            return False
    return True


def filter_prime_numbers(numbers: list) -> list:

    prime_numbers = []

    try:
        for n in numbers:
            if isinstance(n, int):
                if is_prime(n):
                    prime_numbers.append(n)

    except (TypeError, ValueError) as error:
        print(f"[Error found]: {error}")
        return []

    return prime_numbers



# TEST:
test_list = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
result = list(filter_prime_numbers(test_list))
print(f"Prime Numbers: {result}")

