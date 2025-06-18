# 1. Escreva uma função que receba uma lista de números e retorne outra lista com os números ímpares.

def filter_odd_numbers(numbers: list) -> list:

    odd_numbers = []

    for number in numbers:
        try:
            if isinstance(number, int) and number % 2 != 0:
                odd_numbers.append(number)   
     
        except (TypeError, ValueError) as error:
            print(f"[Error found]: {error}")
            return []
            
    return odd_numbers        


# TEST:
test_list = [1, 2, 3.5, 'a', 5, [7, 8], 9, None, 11]
result = filter_odd_numbers(test_list)
print(f"Odd Numbers: {result}")
