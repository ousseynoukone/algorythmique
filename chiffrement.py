
def lettre_vers_numero(lettre):
    return ord(lettre) - ord("A")


def numero_vers_lettre(ascii):
    return chr(ascii + ord("A"))



def est_une_lettre(c):
    return "A" <= c <= "Z"



def cle_valide(cle):
    if len(cle) == 0:
        return False
    for c in cle:
        if not est_une_lettre(c):
            return False
    return True


def preparer_cle(cle, longueur_message):
    cle_etendue = ""
    i = 0
    while len(cle_etendue) < longueur_message:
        cle_etendue = cle_etendue + cle[i]
        i = (i + 1) % len(cle)
    return cle_etendue


def chiffrer(message, cle):
    message = message.upper()
    cle = cle.upper()

# On igncoare les caracteres speciaux
    nb_lettres = 0
    for c in message:
        if est_une_lettre(c):
            nb_lettres = nb_lettres + 1

    cle_etendue = preparer_cle(cle, nb_lettres)

    result = ""
    j = 0  

    for i in range(len(message)):
        char = message[i]
        if est_une_lettre(char):
            m = lettre_vers_numero(char)
            k = lettre_vers_numero(cle_etendue[j])
            c = (m + k) % 26
            result = result + numero_vers_lettre(c)
            j = j + 1
        else:
            result = result + char

    return result


message = input("Message à chiffrer : ")
cle = input("Clé (que des lettres) : ")
cle = cle.upper().replace(" ", "")  

if not cle_valide(cle):
    print("La cle doit contenir uniquement des lettres.")
else :

    resulst = chiffrer(message, cle)
    print("Message chiffré :", resulst)