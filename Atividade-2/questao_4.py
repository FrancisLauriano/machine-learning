# 4. Dada uma lista de números inteiros, 
# escreva uma função para encontrar o segundo maior valor na lista.

def second_largest(numbers: list) -> int | None:

    try:
        # Remove duplicados
        unique_numbers = list(set(numbers))  

        if len(unique_numbers) < 2:
            print("The list does not have a second highest value.")
            return None

        unique_numbers.sort(reverse=True)
        return unique_numbers[1]

    except (TypeError, ValueError) as error:
        print(f"[Error found]: {error}")
        return None


# TEST:
test_list = [4, 2, 9, 5, 9, 7, 7, 8]
# test_list_one_value = [4]
result = second_largest(test_list)
print(f"Second Largest Number: {result}")
