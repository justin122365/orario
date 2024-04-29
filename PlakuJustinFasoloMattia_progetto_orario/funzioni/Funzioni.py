STARTMESSAGGIO = 'Digita '  # Messaggio iniziale per ogni voce del menu
MIDMESSAGGIO = ' per '  # Parte centrale del messaggio per ogni voce del menu
VOCI_MENU = (
    'terminare',  # Voce del menu per terminare il programma
    'ottenere l\'elenco dei docenti di una classe',  # Voce del menu per ottenere l'elenco dei docenti di una classe
    'ottenere l\'orario di un determinato docente',  # Voce del menu per ottenere l'orario di un docente
    'ottenere le ore a disposizione di un docente',  # Voce del menu per ottenere le ore a disposizione di un docente
    'ottenere l\'elenco dei docenti che hanno lezione in un determinato giorno e ora'  # Voce del menu per ottenere i docenti che hanno lezione in un giorno e un'ora specifici
)


def vociMenu():
    """Stampa il menu delle opzioni disponibili."""
    for i in range(len(VOCI_MENU)):
        print(STARTMESSAGGIO + str(i) + MIDMESSAGGIO + VOCI_MENU[i])


def elencoDocentiClasse(righecsv, classe):
    """
    Restituisce un elenco dei docenti che insegnano in una determinata classe.

    Parametri:
        righecsv (list): Lista delle righe del file CSV.
        classe (str): Nome della classe da cercare.

    Ritorna:
        list: Lista dei docenti che insegnano nella classe specificata.
    """
    docs = []
    for i in range(len(righecsv)):
        for j in range(len(righecsv[i])):
            if righecsv[i][j].strip() == classe:
                docs.append(righecsv[i][0].strip())
                break

    return docs


def orarioDocente(righecsv, docente):
    """
    Restituisce l'orario di un docente.

    Parametri:
        righecsv (list): Lista delle righe del file CSV.
        docente (str): Nome del docente di cui ottenere l'orario.

    Ritorna:
        list: Orario del docente specificato.
    """
    for i in range(len(righecsv)):
        if righecsv[i][0].strip() == docente:
            return righecsv[i]


def oreDispDocente(righecsv, docente):
    """
    Restituisce il numero di ore a disposizione di un docente.

    Parametri:
        righecsv (list): Lista delle righe del file CSV.
        docente (str): Nome del docente di cui ottenere il numero di ore a disposizione.

    Ritorna:
        int: Numero di ore a disposizione del docente specificato.
    """
    ore_d = 0
    for i in range(len(righecsv)):
        if righecsv[i][0].strip() == docente:
            for j in range(len(righecsv[i])):
                if righecsv[i][j].strip() == 'D':
                    ore_d += 1

    return ore_d


def docentiGiornoOra(righecsv, giorno, ora):
    """
    Restituisce l'elenco dei docenti che hanno lezione in un determinato giorno e ora.

    Parametri:
        righecsv (list): Lista delle righe del file CSV.
        giorno (str): Giorno della settimana.
        ora (int): Ora della giornata.

    Ritorna:
        tuple: Tuple contenente l'elenco dei docenti che hanno lezione e l'ora effettiva.
    """
    # Rimuove le prime due righe che contengono intestazioni e orari
    righecsv.remove(righecsv[0])
    righecsv.remove(righecsv[0])

    docs_giorno_ora = []  # Lista per memorizzare i docenti che hanno lezione
    # Dizionario per mappare i giorni della settimana all'indice dell'orario
    dict_giorno_ora = {'Lu': 0, 'Ma': 8, 'Me': 16, 'Gi': 24, 'Ve': 32}
    ora += dict_giorno_ora[giorno]  # Calcola l'indice dell'orario effettivo

    # Itera sulle righe del CSV per trovare i docenti che hanno lezione nell'ora specificata
    for i in range(len(righecsv)):
        if righecsv[i][ora].strip(' ') != '' and righecsv[i][ora].strip(' ') != 'R':
            docs_giorno_ora.append(righecsv[i][0].strip(' '))

    ora -= dict_giorno_ora[giorno] # Resetta il valore di ora

    return docs_giorno_ora, ora  # Restituisce i docenti che hanno lezione e l'ora effettiva

