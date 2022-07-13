def solution(xs):
    alphabet = [chr(value) for value in range(97, 123)]
    reversed_alphabet = list(reversed(alphabet))

    alphabet_mapping = dict(zip(alphabet, reversed_alphabet))

    secret_message = ""

    for char in xs:
        if char in alphabet_mapping:
            secret_message += alphabet_mapping[char]
        else:
            secret_message += char

    setattr(solution, 'solution', secret_message)

    return getattr(solution, 'solution')
