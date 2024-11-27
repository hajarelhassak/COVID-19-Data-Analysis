import tkinter as tk
from tkinter import messagebox

# Fonction pour calculer 
def clc(n1, n2, operation):
    try:
        n1 = float(n1)
        n2 = float(n2)
        if operation == '+':
            return n1 + n2
        elif operation == '-':
            return n1 - n2
        elif operation == '*':
            return n1 * n2
        elif operation == '**':  # puissance
            return n1 ** n2
        elif operation == '/':
            if n2 != 0:
                return n1 / n2
            else:
                return 'Erreur : Division par zéro'
        else:
            return 'Opération invalide'
    except ValueError:
        return 'Erreur : Entrée non valide'

# Fonction pour afficher le résultat
def resultat():
    n1_val = n1.get()
    n2_val = n2.get()
    operation_val = operation.get()
    resultat = clc(n1_val, n2_val, operation_val)
    label_resultat.config(text=f'Le résultat est : {resultat}')

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title('Hajalix - Calculatrice')
fenetre.geometry('400x300')

# Champs pour les entrées
tk.Label(fenetre, text='Entrez votre 1er nombre :').grid(row=0, column=0, padx=10, pady=5)
n1 = tk.Entry(fenetre)
n1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(fenetre, text='Entrez votre 2ème nombre :').grid(row=1, column=0, padx=10, pady=5)
n2 = tk.Entry(fenetre)
n2.grid(row=1, column=1, padx=10, pady=5)

tk.Label(fenetre, text='Entrez l opération souhaitée :').grid(row=2, column=0, padx=10, pady=5)
operation = tk.Entry(fenetre)
operation.grid(row=2, column=1, padx=10, pady=5)

# Bouton pour calculer
bouton_calcul = tk.Button(fenetre, text='Calculer', command= resultat)
bouton_calcul.grid(row=3, column=0, columnspan=2, pady=20)

# Label pour afficher le résultat
label_resultat = tk.Label(fenetre, text='Le résultat est :', bg='lightgray', font=('Arial', 12))
label_resultat.grid(row=4, column=0, columnspan=2, pady=10)

# Boucle principale
fenetre.mainloop()
