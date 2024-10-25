def cifru_cezar(text, cheie, operatie):

    alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    text = text.upper().replace(" ", "")

    # ключ
    if cheie < 1 or cheie > 25:
        raise ValueError("Ключ должен быть между 1 и 25")

    # получение индекса буквы
    def index_litera(litera):
        return alfabet.index(litera)

    # получение буквы соответствующей индексу
    def litera_indice(indice):
        return alfabet[(indice) % len(alfabet)]

    rezultat = ""
    for litera in text:
        if litera in alfabet:

            if operatie == "шифровка":
                indice = index_litera(litera)
                # print(indice)
                # print(indice + cheie)
                indice += cheie
            else:
                indice = index_litera(litera)
                indice -= cheie
                # print(indice)
                # print(indice - cheie)
            rezultat += litera_indice(indice)
        else:
            # Caractere neacceptate
            rezultat += litera

    return rezultat

# Exemplu de utilizare
text = input("Введите текст: ")
cheie = int(input("Введите ключ (1-25): "))
operatie = input("Выберите операцию (шифровка/расшифровка): ")

try:
    rezultat = cifru_cezar(text, cheie, operatie)
    print(rezultat)
except ValueError as e:
    print(e)