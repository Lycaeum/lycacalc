#!usr/bin/python

# Python Libs

import math
import datetime
import os

# Math functions

# Logo & Menus


def menuPause():
    menuPause = input("\nDigite qualquer tecla para continuar.")
    return(menuPause)


def saudacao():  # Define uma funcão que sauda o usuário conforme a hora do dia
    os.system("clear")
    print("\tLycalc 0.1 Alpha\n\t05/2016\n\tLycasoft(r)")
    currentTime = datetime.datetime.now()
    hournow = currentTime.hour
    minnow = currentTime.minute
    if hournow < 12:
        print('\n\n\n\nBom dia. São %i:%i\n' % (hournow, minnow))
    elif 12 <= hournow < 18:
        print('\n\n\n\nBoa tarde. São %i:%i\n' % (hournow, minnow))
    else:
        print('\n\n\n\nBoa noite. São %i:%i\n' % (hournow, minnow))


def bopMenu():
    menuCond = 0
    while menuCond == 0:
        print("\n1 >>> Adição\n2 >>> Substração\n3 >>> Multiplicação")
        print("4 >>> Divisão & Resto")
        print("0 >>> Sair.\n\n\n\n")
        menuChoice = input("Qual a operação você deseja realizar?:\t>>> ")

        a = input("\nDigite o 1o valor:\t>>> ")
        b = input("\nDigite o 2o valor:\t>>> ")

        if menuChoice == 1:
            resp = a + b
            print("\nA soma dos 2 valores é de %i" % resp)
            menuPause()
        elif menuChoice == 2:
            resp = a - b
            print("\nA substração dos 2 valores é de %i" % resp)
            menuPause()
        elif menuChoice == 3:
            resp = a * b
            print("\nA multiplicação dos 2 valores é de %i" % resp)
            menuPause()
        elif menuChoice == 4:
            resp = a / b
            resp2 = a % b
            print("\nA divisão dos 2 valores é de %i " % resp)
            print("com resto %i" % resp2)
            menuPause()
        elif menuChoice == 0:
            menuCond = 1
        else:
            print("Opção inválida")
            menuPause()


# def main():
saudacao()
bopMenu()
