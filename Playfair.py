def playfair(key, text, mode='encrypt'):

    def create_matrix(key):
        matrix = []
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        used = set()
        for char in key.upper():
            if char not in used and char in alphabet:
                matrix.append(char)
                used.add(char)
        for char in alphabet:
            if char not in used:
                matrix.append(char)
        return [matrix[i:i+5] for i in range(0, 25, 5)]

    def find_position(matrix, char):
        for i in range(8):
            for j in range(8):
                if matrix[i][j] == char:
                    return i, j

    text = text.upper().replace(' ', '')
    if len(text) % 2:
        text += 'X'
    print(text)

    # Creăm matricea cheie
    key_matrix = create_matrix(key)
    print(key_matrix)

    result = ''
    for i in range(0, len(text), 2):
        char1, char2 = text[i], text[i+1]
        row1, col1 = find_position(key_matrix, char1)
        row2, col2 = find_position(key_matrix, char2)

        if mode == 'encrypt':
            # Правила шифрования
            if row1 == row2:
                col1 = (col1 + 1) % 8
                col2 = (col2 + 1) % 8
                result += key_matrix[row1][col2] + key_matrix[row2][col1]
            elif col1 == col2:
                row1 = (row1 + 1) % 8
                row2 = (row2 + 1) % 8
                result += key_matrix[row1][col2] + key_matrix[row2][col1]
            else:
                result += key_matrix[row1][col2] + key_matrix[row2][col1]
            print(result)
        elif mode == 'decrypt':
            # Правила дешифрования
            if row1 == row2:
                col1 = (col1 - 1) % 8
                col2 = (col2 - 1) % 8
                result += key_matrix[row1][col2] + key_matrix[row2][col1]
            elif col1 == col2:
                row1 = (row1 - 1) % 8
                row2 = (row2 - 1) % 8
                result += key_matrix[row1][col2] + key_matrix[row2][col1]
            else:
                result += key_matrix[row1][col2] + key_matrix[row2][col1]
            print(result)

    return result

###
key = "PASSWORD"
text = "PREDEAL"
ciphertext = playfair(key, text)
plaintext = playfair(key, ciphertext, mode='decrypt')

print("Ciphertext:", ciphertext)
print("Plaintext:", plaintext)