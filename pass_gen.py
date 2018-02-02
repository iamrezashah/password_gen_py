def make_me_a_password():
    import random
    pass_len = int(input('How many characters do you want? '))
    password = ''

    for i in range(pass_len):
        char = chr(random.randint(32,126))
        password += char

    return password

print(make_me_a_password())
