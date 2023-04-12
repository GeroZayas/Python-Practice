def caesarCipher(s, k):
    alpha= 'abcdefghijklmnopqrstuvwxyz'
    alpha_list = [ch for ch in alpha]
    rotated_string = ''
    capital = False
    for ch in s:
        if ch.isupper() == True:
            capital = True
        ch = ch.lower()
        if ch.isalpha() == True:
            rot = alpha_list.index(ch) + k
            if rot > 25:
                rot = rot % 26
            rotated_string += alpha_list[rot] if not capital else alpha_list[rot].upper()
            capital = False
        else:
            rotated_string += ch

    return rotated_string

    # Write your code here

s = "Hello_World!"

k  = 4

r = caesarCipher(s, k)

print(r)

expected = 'Lipps_Asvph!' 

print(" => ", r == expected)
