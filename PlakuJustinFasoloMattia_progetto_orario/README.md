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
import Funzioni
PERCORSOCSV = 'OrarioTabellaGlobale.csv'
PERCORSODIR = 'FileCreati'
SCELTAMESSAGGIO = 'Operazione da eseguire: '
ERROREMESSAGGIO = 'Operazione non prevista.' 
FILENOTFOUND = 'File CSV non trovato!'
SCELTE_VALIDE = ('0', '1', '2', '3', '4')


os.system('CLS')
if (os.path.exists(PERCORSODIR)):
    pass
else:
    os.system('md ' + PERCORSODIR)

uscita = False
while (not(uscita)):
    print('-' * 80)
    Funzioni.vociMenu()
    print('-' * 80)

    scelta = input(SCELTAMESSAGGIO)
    while (scelta not in SCELTE_VALIDE):
        print(ERROREMESSAGGIO)
        scelta = input(SCELTAMESSAGGIO)
    
    if scelta == SCELTE_VALIDE[0]:
        uscita = True


    
    
    elif scelta == SCELTE_VALIDE[1]:
        if not(os.path.exists(PERCORSOCSV)):
            print(FILENOTFOUND)
            break
        else:
            filecsv = open(PERCORSOCSV, 'r')

        righecsv = []
        classi = set()

        rigacsv = filecsv.readline().rstrip().split(',')
        while rigacsv != ['']:
            righecsv.append(rigacsv)
            rigacsv = filecsv.readline().rstrip().split(',')

        for i in range(len(righecsv)):
            for j in range(len(righecsv[i])):
                if (len(righecsv[i][j].strip(" ")) == 3 and righecsv[i][j] != ''):
                    classi.add(righecsv[i][j])
        
        classi = list(classi)

        classe = input('Inserisci la classe da controllare: ').upper()
        while (classe not in classi):
            print(ERROREMESSAGGIO)
            classe = input('Inserisci la classe da controllare: ').upper()

        PERCORSOTXT = PERCORSODIR + '\\' + classe + '.txt'
        filetxt = open(PERCORSOTXT, 'a')
        filetxt.close()
        filetxt = open(PERCORSOTXT, 'w')

        docenti_classe = Funzioni.elencoDocentiClasse(righecsv, classe)

        for i in docenti_classe:
            filetxt.write(i + '\n')
        
        filecsv.close()
        filetxt.close()

    elif scelta == SCELTE_VALIDE[2]:
        if not(os.path.exists(PERCORSOCSV)):
            print(FILENOTFOUND)
            break
        else:
            filecsv = open(PERCORSOCSV, 'r')

        righecsv = []
        docenti = []

        rigacsv = filecsv.readline().rstrip().split(',')
        while rigacsv != ['']:
            righecsv.append(rigacsv)
            rigacsv = filecsv.readline().rstrip().split(',')

        for i in range(len(righecsv)):
            docenti.append(righecsv[i][0].strip(' '))
        
        docenti.remove(docenti[0])
        docenti.remove(docenti[0])

        docente = input('Inserisci il docente da controllare: ').upper()
        while (docente not in docenti):
            print(ERROREMESSAGGIO)
            docente = input('Inserisci il docente da controllare: ').upper()

        PERCORSOTXT = PERCORSODIR + '\\' + docente + '.txt'
        filetxt = open(PERCORSOTXT, 'a')
        filetxt.close()
        filetxt = open(PERCORSOTXT, 'w')

        orario_docente = Funzioni.orarioDocente(righecsv, docente)

        for i in righecsv[0]:
            filetxt.write(i + ', ')
        filetxt.write('\n')
        
        for i in righecsv[1]:
            filetxt.write(i + ', ')
        filetxt.write('\n\n')

        ore_settimanali = 0
        for i in range(len(orario_docente)):
            filetxt.write(orario_docente[i] + ', ')
            if (orario_docente[i].strip() != ''):
                ore_settimanali += 1

        filetxt.write('\nNumero di ore settimanali: ' + str(ore_settimanali - 1))
        
        filecsv.close()
        filetxt.close()

    elif scelta == SCELTE_VALIDE[3]:
        if not(os.path.exists(PERCORSOCSV)):
            print(FILENOTFOUND)
            break
        else:
            filecsv = open(PERCORSOCSV, 'r')

        righecsv = []
        docenti = []

        rigacsv = filecsv.readline().rstrip().split(',')
        while rigacsv != ['']:
            righecsv.append(rigacsv)
            rigacsv = filecsv.readline().rstrip().split(',')

        for i in range(len(righecsv)):
            docenti.append(righecsv[i][0].strip(' '))
        
        docenti.remove(docenti[0])
        docenti.remove(docenti[0])

        docente = input('Inserisci il docente da controllare (D): ').upper()
        while (docente not in docenti):
            print(ERROREMESSAGGIO)
            docente = input('Inserisci il docente da controllare (D): ').upper()

        PERCORSOTXT = PERCORSODIR + '\\' + docente + ' (D)' + '.txt'
        filetxt = open(PERCORSOTXT, 'a')
        filetxt.close()
        filetxt = open(PERCORSOTXT, 'w')

        ore_disponibili = Funzioni.oreDispDocente(righecsv, docente)
        filetxt.write('Numero di ore disponibili di ' + docente + ': ' + str(ore_disponibili))

        filecsv.close()
        filetxt.close()




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

- **N.B: *La funzione `n.5` non è attualmente disponibile nel progetto, la sua aggiunta è pianificata il prima possibile***

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


