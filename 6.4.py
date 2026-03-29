def is_lucky(ticket):
    n = len(ticket)
    half = n // 2
    first = sum(map(int, ticket[:half]))
    second = sum(map(int, ticket[half:]))
    return first == second

ticket = input("Введите номер билета: ")
print(is_lucky(ticket))