text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz' #a es 0, a partir de b es 1
encrypted_text = ''
for char in text.lower(): #recorre linea por linea text pero en minuscula (lower)
    index = alphabet.find(char)  #busca la posicion de la letraen alphabet
    print(index) #numero de las letras
    new_index = index + shift #numero de las letras + 3, si es z se suma 25 + 3 y se divide en 2 (c en este caso)
    encrypted_text = encrypted_text + alphabet[new_index] #agarra la nueva letra cifrada (+3) y la manda a encrypted text
    print('char:', char, 'encrypted text:', encrypted_text)
    print(new_index)