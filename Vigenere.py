def vigenere(key, text, mode='encrypt'):

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = key.upper()
    text = text.upper().replace(' ', '')

    def char_to_index(char):
        return ord(char) - ord('A')

    def index_to_char(index):
        return alphabet[index % len(alphabet)]  # Handle potential negative indices

    result = ''
    key_index = 0
    for char in text:
        char_index = char_to_index(char)
        key_char = key[key_index]
        key_index_num = char_to_index(key_char)

        if mode == 'encrypt':
            new_index = (char_index + key_index_num) % len(alphabet)
        else:
            new_index = (char_index - key_index_num + len(alphabet)) % len(alphabet)

        result += index_to_char(new_index)
        key_index = (key_index + 1) % len(key)

    return result

# Exemplu de utilizare
key = "CRYPTOGRAFY"
text = "TREBUIE DE VEREFICAT ALGORITMUL REALIZAT"
ciphertext = vigenere(key, text)
plaintext = vigenere(key, ciphertext, mode='decrypt')

print("Ciphertext:", ciphertext)
print("Plaintext:", plaintext)