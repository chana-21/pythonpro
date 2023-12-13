def frequency_analytic(s):
    alph_lower = "abcdefghijklmnopqrstuvwxyz"
    alph_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet = {}

    for i in alph_lower:
        alphabet[i] = 0

    for i in alph_upper:
        alphabet[i] = 0

    for i in s:
        if i.isalpha():
            alphabet[i] += 1

    for key, val in alphabet.items():
        if not val == 0:
            print(key, val)


if __name__ == '__main__':
    msg = input('input your message : ')
    frequency_analytic(msg)
