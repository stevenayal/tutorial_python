# -*- coding: utf-8 -*-#
import random
print('---------------------------------')
print('   JUEGO DE ADIVINA EL NUMERO')
print('---------------------------------')
print()

the_number = random.randint(0, 100)
guess = -1
name = input('Jugador Cual es tu nombre?')

while guess != the_number:
    guess_text = input('Adivina el numero entre 0 and 100: ')
    guess = int(guess_text)

    if guess < the_number:
        # print('Your guess of ' + guess + ' was too LOW.')
        print('Sorry {}, tu eleccion de {} fue muy BAJA.'.format(name, guess))
    elif guess > the_number:
        print('Sorry {}, tu eleccion de {} fue muy ALTA.'.format(name, guess))
    else:
        print('Excelente trabajo {}, Tu ganas, era el {}!'.format(name, guess))

print('Fin.')