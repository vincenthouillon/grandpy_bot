import random

ADDRESS_MSG = [
    "Bien sûr mon poussin ! La voici : ",
    "Si je me rappelle bien c'est : ",
    "Il me semble que c'est : "
]

SUMMARY_MSG = [
    "Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ? ",
    "Est-ce que tu savais que... ",
    "Sais-tu que : "
]

ERROR_MSG = [
    "Hum, c'est embarassant, as-tu saisi correctement ta demande ? ",
    "Je ne trouve rien à ce sujet ! As-tu correctement saisi ta demande ? "
]


def address_msg():
    message = random.choice(ADDRESS_MSG)
    return message


def summary_msg():
    message = random.choice(SUMMARY_MSG)
    return message


def error_msg():
    message = random.choice(ERROR_MSG)
    return message
