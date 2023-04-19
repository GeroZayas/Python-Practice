
# a function that multiplies all input numbers
def multiply(*args):
    result = 1
    for arg in args:
        result *= arg
    return result

print(multiply(1, 4, 5))

def caesarCipher(s, k):
    alpha= 'abcdefghijklmnopqrstuvwxyz'
    alpha_list = [ch for ch in alpha]
    rotated_string = ''
    capital = False
    for ch in s:
        if ch.isupper() == True:
            capital = True
        ch = ch.lower()
        
        print("ch", ch)
        
        if ch.isalpha() == True:
            
            print("alpha_list.index(ch) => ",alpha_list.index(ch))
            
            rot = alpha_list.index(ch) + k
            
            print("rot", rot)
            
            if rot > 25:
                rot = rot % 26
                
            print("rot 2 = ", rot)
            print("alpha_list[rot] ", alpha_list[rot] )
            
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
