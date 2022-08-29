def recall_password(cipher_grille, ciphered_password):
    list = ""                                                          #Список, где будут храниться полученные данные
    turn = 0                                                           #Счетчик
    while turn < 4:
        for elem1, elem2 in zip(ciphered_password, cipher_grille):
            for word1, word2 in zip(elem1, elem2):
                if word2 == "X":
                    list += word1
        cipher_grille = tuple(zip(*cipher_grille[::-1]))
        turn += 1
    print(list)
    return list