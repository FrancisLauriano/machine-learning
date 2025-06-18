# 5. Crie uma função que receba uma lista de tuplas, 
# cada uma contendo o nome e a idade de uma pessoa, e 
# retorne a lista ordenada pelo nome das pessoas em ordem alfabética.

def sort_by_name(people: list[tuple]) -> list[tuple]:

    try:
        return sorted(people, key=lambda person: person[0])
    except (TypeError, ValueError) as error:
        print(f"[Error found]: {error}")
        return []


# TEST:
people_list = [
    ("Maria", 30),
    ("João", 25),
    ("Ana", 22),
    ("Carlos", 28),
    ("Beatriz", 35)
]

result = sort_by_name(people_list)
print(f"Sorted List by Name: {result}")
    