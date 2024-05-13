# ORARIO ITIS GUGLIELMO MARCONI

## Autori: Justin Plaku | Fasolo Mattia ##


## Descrizione del progetto
- Programma sviluppato in **`Python`** che utilizza un file di tipo **CSV** *(comma-separeted values)* per **creare/gestire** dei file in base alle **richieste dell'utente**

- Il programma adotta principalmente **liste** come `strutture dati` e mostra grande utilizzo di **metodi di gestione dei `file`**

- Infine il programma presenta un **modulo personalizzato** compreso di **metodi personalizzati** per permettere al programma di `compiere determinate azioni`


## Requisiti minimi del progetto
- Ecco un **elenco di passaggi `fondamentali`** per il funzionamento corretto dell'*intero progetto*:

1. Assicurati che il file `OrarioTabellaGlobale.csv` sia all'interno della **project directory.**

2. Assicurati di utilizzare una **versione superiore a** `Python3`

## Spiegazione delle Funzioni
### File main.py
```py
# -*- coding: utf-8 -*-

import os
import funzioni.Funzioni as Funzioni
PERCORSOCSV = 'OrarioTabellaGlobale.csv'  # Percorso del file CSV dell'orario globale
PERCORSODIR = 'FileCreati'  # Directory in cui verranno creati i file di output
SCELTAMESSAGGIO = 'Operazione da eseguire: '  # Messaggio per richiedere l'operazione da eseguire
ERROREMESSAGGIO = 'Operazione non prevista.'   # Messaggio di errore per input non valido
FILENOTFOUND = 'File CSV non trovato!'  # Messaggio di errore per file CSV non trovato
SCELTE_VALIDE = ('0', '1', '2', '3', '4')  # Tuple delle scelte valide per il menu

# Pulisce la console per una visualizzazione più pulita
os.system('CLS')


uscita = False
while (not(uscita)):
    # Verifica se la directory specificata esiste, altrimenti la crea
    if (os.path.exists(PERCORSODIR)):
        pass
    else:
        os.system('md ' + PERCORSODIR)
    
    print('-' * 80)
    Funzioni.vociMenu()  # Stampa le voci del menu chiamando la funzione da Funzioni.py
    print('-' * 80)

    scelta = input(SCELTAMESSAGGIO)  # Richiede all'utente di inserire una scelta
    while (scelta not in SCELTE_VALIDE):  # Continua a richiedere finché l'input non è valido
        print(ERROREMESSAGGIO)
        scelta = input(SCELTAMESSAGGIO)
    
    if scelta == SCELTE_VALIDE[0]:  # Se la scelta è '0', esci dal ciclo
        uscita = True

    elif scelta == SCELTE_VALIDE[1]:  # Se la scelta è '1', esegui la prima operazione
        if not(os.path.exists(PERCORSOCSV)):
            print(FILENOTFOUND)  # Se il file non esiste, stampa un messaggio di errore
            break
        else:
            filecsv = open(PERCORSOCSV, 'r')  # Apre il file CSV in modalità lettura

        righecsv = []
        classi = set()

        # Legge ogni riga del file CSV e costruisce un insieme delle classi presenti
        rigacsv = filecsv.readline().rstrip().split(',')
        while rigacsv != ['']:
            righecsv.append(rigacsv)
            rigacsv = filecsv.readline().rstrip().split(',')

        for i in range(len(righecsv)):
            for j in range(len(righecsv[i])):
                if (len(righecsv[i][j].strip(" ")) == 3 and righecsv[i][j] != ''):
                    classi.add(righecsv[i][j])
        
        classi = list(classi)

        # Richiede all'utente di inserire la classe da controllare e la converte in maiuscolo
        classe = input('Inserisci la classe da controllare: ').upper()
        while (classe not in classi):
            print(ERROREMESSAGGIO)
            classe = input('Inserisci la classe da controllare: ').upper()

        PERCORSOTXT = PERCORSODIR + '\\' + classe + '.txt'  # Percorso del file di output per la classe
        filetxt = open(PERCORSOTXT, 'a')  # Apre il file di output in modalità append
        filetxt.close()
        filetxt = open(PERCORSOTXT, 'w')  # Apre il file di output in modalità scrittura

        docenti_classe = Funzioni.elencoDocentiClasse(righecsv, classe)  # Ottiene gli insegnanti per la classe

        for i in docenti_classe:
            filetxt.write(i + '\n')  # Scrive ciascun insegnante nel file di output
        
        filecsv.close()  # Chiude il file CSV
        filetxt.close()  # Chiude il file di output

# termine codice per lo svolgimento della prima scelta

    elif scelta == SCELTE_VALIDE[2]:  # Se la scelta è '2', esegui la seconda operazione
        if not(os.path.exists(PERCORSOCSV)):
            print(FILENOTFOUND)  # Se il file non esiste, stampa un messaggio di errore
            break
        else:
            filecsv = open(PERCORSOCSV, 'r')  # Apre il file CSV in modalità lettura

        righecsv = []
        docenti = []

        # Legge ogni riga del file CSV e costruisce una lista dei docenti presenti
        rigacsv = filecsv.readline().rstrip().split(',')
        while rigacsv != ['']:
            righecsv.append(rigacsv)
            rigacsv = filecsv.readline().rstrip().split(',')

        for i in range(len(righecsv)):
            docenti.append(righecsv[i][0].strip(' '))
        
        docenti.remove(docenti[0])
        docenti.remove(docenti[0])

        # Richiede all'utente di inserire il docente da controllare e lo converte in maiuscolo
        docente = input('Inserisci il docente da controllare: ').upper()
        while (docente not in docenti):
            print(ERROREMESSAGGIO)
            docente = input('Inserisci il docente da controllare: ').upper()

        PERCORSOTXT = PERCORSODIR + '\\' + docente + '.txt'  # Percorso del file di output per il docente
        filetxt = open(PERCORSOTXT, 'a')  # Apre il file di output in modalità append
        filetxt.close()
        filetxt = open(PERCORSOTXT, 'w')  # Apre il file di output in modalità scrittura

        orario_docente = Funzioni.orarioDocente(righecsv, docente)  # Ottiene l'orario del docente

        for i in righecsv[0]:
            filetxt.write(i + ', ')  # Scrive l'intestazione nel file di output
        filetxt.write('\n')
        
        for i in righecsv[1]:
            filetxt.write(i + ', ')  # Scrive l'orario del docente nel file di output
        filetxt.write('\n\n')

        ore_settimanali = 0
        for i in range(len(orario_docente)):
            filetxt.write(orario_docente[i] + ', ')  # Scrive l'orario del docente nel file di output
            if (orario_docente[i].strip() != ''):
                ore_settimanali += 1

        filetxt.write('\nNumero di ore settimanali: ' + str(ore_settimanali - 1))
        
        filecsv.close()  # Chiude il file CSV
        filetxt.close()  # Chiude il file di output

# codice per la terza scelta

    elif scelta == SCELTE_VALIDE[3]:  # Se la scelta è '3', esegui la terza operazione
        if not(os.path.exists(PERCORSOCSV)):
            print(FILENOTFOUND)  # Se il file non esiste, stampa un messaggio di errore
            break
        else:
            filecsv = open(PERCORSOCSV, 'r')  # Apre il file CSV in modalità lettura

        righecsv = []
        docenti = []

        # Legge ogni riga del file CSV e costruisce una lista dei docenti presenti
        rigacsv = filecsv.readline().rstrip().split(',')
        while rigacsv != ['']:
            righecsv.append(rigacsv)
            rigacsv = filecsv.readline().rstrip().split(',')

        for i in range(len(righecsv)):
            docenti.append(righecsv[i][0].strip(' '))
        
        docenti.remove(docenti[0])
        docenti.remove(docenti[0])

        # Richiede all'utente di inserire il docente da controllare e lo converte in maiuscolo
        docente = input('Inserisci il docente da controllare (D): ').upper()
        while (docente not in docenti):
            print(ERROREMESSAGGIO)
            docente = input('Inserisci il docente da controllare (D): ').upper()

        PERCORSOTXT = PERCORSODIR + '\\' + docente + ' (D)' + '.txt'  # Percorso del file di output per il docente
        filetxt = open(PERCORSOTXT, 'a')  # Apre il file di output in modalità append
        filetxt.close()
        filetxt = open(PERCORSOTXT, 'w')  # Apre il file di output in modalità scrittura

        ore_disponibili = Funzioni.oreDispDocente(righecsv, docente)  # Ottiene le ore disponibili del docente
        filetxt.write('Numero di ore disponibili di ' + docente + ': ' + str(ore_disponibili))

        filecsv.close()  # Chiude il file CSV
        filetxt.close()  # Chiude il file di output

    elif scelta == SCELTE_VALIDE[4]:  # Se la scelta dell'utente è quella di cercare docenti in base all'ora e al giorno
        if not(os.path.exists(PERCORSOCSV)):  # Se il file CSV non esiste
            print(FILENOTFOUND)  # Stampa un messaggio di file non trovato
            break  # Esce dal loop
        else:
            filecsv = open(PERCORSOCSV, 'r')  # Apre il file CSV in modalità lettura

        righecsv = []  # Lista vuota per memorizzare le righe del CSV
        giorni = []  # Lista per memorizzare i giorni presenti nel CSV
        ore = list(range(1, 8))  # Lista delle ore valide

        # Legge la prima riga del CSV e la splitta per ottenere una lista di intestazioni
        rigacsv = filecsv.readline().rstrip().split(',')
        while rigacsv != ['']:  # Continua fino a quando non raggiunge una riga vuota
            righecsv.append(rigacsv)  # Aggiunge la riga alla lista righecsv
            rigacsv = filecsv.readline().rstrip().split(',')  # Legge la riga successiva

        # Itera sulle intestazioni per estrarre i giorni e li aggiunge all'insieme 'giorni'
        for i in range(len(righecsv[0])):
            if (righecsv[0][i].strip() != '' and righecsv[0][i].strip() != 'Docente'):
                if (righecsv[0][i].strip() in giorni):
                    pass
                else:
                    giorni.append(righecsv[0][i].strip())

        giorni = list(giorni)  # Converte l'insieme in lista
        giorno = input(f'Inserisci il giorno da controllare {giorni}: ').capitalize()  # Chiede all'utente di inserire il giorno
        while (len(giorno) > 2 or giorno not in giorni):  # Verifica che il giorno inserito sia valido
            print(ERROREMESSAGGIO)  # Stampa un messaggio di errore
            giorno = input(f'Inserisci il giorno da controllare {giorni}: ').capitalize()  # Richiede il giorno

        ora = input(f'Inserisci l\'ora di {giorno} da controllare {ore}:')  # Chiede all'utente di inserire l'ora
        while (len(ora) > 1 or int(ora) not in ore):  # Verifica che l'ora inserita sia valida
            print(ERROREMESSAGGIO)  # Stampa un messaggio di errore
            ora = input(f'Inserisci l\'ora di {giorno} da controllare {ore}:')  # Richiede l'ora

        ora = int(ora)  # Converte l'ora in intero

        # Ottiene i dati dei docenti per il giorno e l'ora specificati
        dati = Funzioni.docentiGiornoOra(righecsv, giorno, ora)
        docenti_giorno_ora = dati[0]  # Lista dei docenti per il giorno e l'ora specificati
        ora = dati[1]  # Ora effettiva ottenuta dalla funzione

        # Crea il percorso del file di output per i docenti
        PERCORSOTXT = f'{PERCORSODIR}\\DOCENTI ({giorno}, {ora}a ora).txt'
        # Apre il file di output in modalità append
        filetxt = open(PERCORSOTXT, 'a')
        filetxt.close()  # Chiude il file
        # Apre il file di output in modalità scrittura
        filetxt = open(PERCORSOTXT, 'w')

        filetxt.write(f'Docenti con lezioni alla {ora}a ora di {giorno}\n')  # Scrive l'intestazione nel file di output

        # Itera sui docenti e li scrive nel file di output
        for i in docenti_giorno_ora:
            filetxt.write(i + '\n')

        filecsv.close()  # Chiude il file CSV
        filetxt.close()  # Chiude il file di output
```
- Il **Main File** è sviluppato con dei metodi importate dal modulo `Funzioni` e con un ciclo "condizionato" dalle **scelte selezionate tramite input**

- Il file genera una cartella `FileCreati` dove andranno situati i **file creati**

- Il menu viene **generato all'inizio del file** e successivamente il programma sta in ascolto di una **stringa** da impostare su `scelta`, la quale se **non presente tra i valori di `SCELTE_VALIDE`** restituisce un errore.

- In base alla scelta inserita il programma **svolge delle specifiche funzioni**, tra cui l'ottenimento dei **parametri** dei metodi personalizzati di `Funzioni`

### Creazione del menu interattivo
```py
STARTMESSAGGIO = 'Digita '
MIDMESSAGGIO = ' per '
VOCI_MENU = (   
                'terminare', 
                'ottenere l\'elenco dei docenti di una classe',
                'ottenere l\'orario di un determinato docente', 
                'ottenere le ore a disposizione di un docente', 
                'ottenere l\'elenco dei docenti che hanno lezione in un determinato giorno e ora'
            )

def vociMenu():
    for i in range(len(VOCI_MENU)):
        print(STARTMESSAGGIO + str(i) + MIDMESSAGGIO + VOCI_MENU[i])
```
- La funzione è ideata per mostrare sul **terminale** il `menu interattivo` che l'utente può utilizzare per eseguire le **successive funzioni**

- Le costanti `STARTMESSAGGIO, MIDMESSAGGIO E VOCI_MENU` sono utilizzate dalla funzione `vociMenu` per stampare un elenco di **stringhe concatenate** tramite la scansione di `VOCI_MENU`

### Elenco dei docenti in una classe
```py
def elencoDocentiClasse(righecsv, classe):
    docs = []
    for i in range(len(righecsv)):
        for j in range(len(righecsv[i])):
            if (righecsv[i][j].strip() == classe):
                docs.append(righecsv[i][0].strip())
                break
    
    return docs
```
- La funzione utilizza la **matrice** `righecsv` creata tramite il file *CSV* e una **stringa** `classe` ottenuta tramite *input* per accedere al **cognome** e al **nome** del `docente corrispondente` alla classe, per poi aggiungerlo ad una **seconda lista** di stringhe che successivamente verrà **riscritta su un file in secondo luogo**

### Orario di un docente
```py
def orarioDocente(righecsv, docente):
    for i in range(len(righecsv)):
        if (righecsv[i][0].strip() == docente):
            return righecsv[i]
```
- La funzione gestisce la **medesima matrice** per accedere tramite una stringa `docente` alla riga corrispondente che mostra le ore della settimana che successivamente verrà **riscritta su un file in secondo luogo** assieme alle **ore settimanali**

### Ore disponibili di un docente
```py
def oreDispDocente(righecsv, docente):
    ore_d = 0
    for i in range(len(righecsv)):
        if (righecsv[i][0].strip() == docente):
            for j in range(len(righecsv[i])):
                if (righecsv[i][j].strip() == 'D'):
                    ore_d += 1
        
    return ore_d
```
- La funzione calcola le **ore contrassegnate da `'D'`** all'interno del file *CSV* data una stringa `docente` (cognome e nome del docente), il quale totale delle ore verrà **riscritto su un file in secondo luogo** assieme al `docente` precedentemente ottenuto

### Elenco dei docenti dati giorno e ora
```py
def docentiGiornoOra(righecsv, giorno, ora):

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
```
- la funzione restituisce l'elenco dei docenti dati come parametri un giorno della settimana e un'ora di quel giorno.

