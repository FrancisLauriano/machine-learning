# 3. Escreva uma função que receba duas listas e retorne outra lista com os 
# elementos que estão presentes em apenas uma das listas.

def unique_elements(list1: list, list2: list) -> list:

    try:
        # ^ faz a diferença simetrica
        result = list(set(list1) ^ set(list2))  
        return result
    except (TypeError, ValueError) as error:
        print(f"[Error found]: {error}")
        return []


# TEST:
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

result = unique_elements(list1, list2)
print(f"Unique Elements: {result}")
