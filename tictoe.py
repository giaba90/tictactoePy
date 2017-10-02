#!/usr/bin/env python
# -*- coding: utf-8 -*-

welcome = """
*****************************************
*       Benvenuti nel gioco TicToe      *
*           versione DOS                *
*                                       *
*                                       *
* Istruzioni:                           *
*                                       *
* scegli il numerino corrispondente     *
* alla posizione dove mettere il segno  *
*****************************************
"""

#Print a field game
def print_matrix(m_input):
	print ''
	for row in m_input:
		for col in row:
			print '| '+str(col),
		print '|'

#Draw tic or toe
def draw_tictoe(pos,m,t):
	if pos == '1':
		if m[0][0]!= 'x' and m[0][0]!= 'o':
			m[0][0] = t
			return True
		else:
			print '\nLa posizione ' + str(pos) +' è occupata\n'
			print_matrix(matrix_input)
			return False
	if pos == '2':
		if m[0][1]!= 'x' and m[0][1]!= 'o':
			m[0][1] = t
			return True
		else:
			print '\nLa posizione ' + str(pos) +' è occupata\n'
			print_matrix(matrix_input)
			return False
	if pos == '3':
		if m[0][2]!= 'x' and m[0][2]!= 'o':
			m[0][2] = t
			return True
		else:
			print '\nLa posizione ' + str(pos) +' è occupata\n'
			print_matrix(matrix_input)
			return False
	if pos == '4':
		if m[1][0]!= 'x' and m[1][0]!= 'o':
			m[1][0] = t
			return True
		else:
			print '\nLa posizione ' + str(pos) +' è occupata\n'
			print_matrix(matrix_input)
			return False
	if pos == '5':
		if m[1][1]!= 'x' and m[1][1]!= 'o':
			m[1][1] = t
			return True
		else:
			print '\nLa posizione ' + str(pos) +' è occupata\n'
			print_matrix(matrix_input)
			return False
	if pos == '6':
		if m[1][2]!= 'x' and m[1][2]!= 'o':
			m[1][2] = t
			return True
		else:
			print '\nLa posizione ' + str(pos) +' è occupata\n'
			print_matrix(matrix_input)
			return False
	if pos == '7':
		if m[2][0]!= 'x' and m[2][0]!= 'o':
			m[2][0] = t
			return True
		else:
			print '\nLa posizione ' + str(pos) +' è occupata\n'
			print_matrix(matrix_input)
			return False
	if pos == '8':
		if m[2][1]!= 'x' and m[2][1]!= 'o':
			m[2][1] = t
			return True
		else:
			print '\nLa posizione ' + str(pos) +' è occupata\n'
			print_matrix(matrix_input)
			return False
	if pos == '9':
		if m[2][2]!= 'x' and m[2][2]!= 'o':
			m[2][2] = t
			return True
		else:
			print '\nLa posizione ' + str(pos) +' è occupata\n'
			print_matrix(matrix_input)
			return False


#check the winner
def check_result(t,m):
	tris = 3*[t]
	col1 = [m[0][0],m[1][0],m[2][0]]
	col2 = [m[0][1],m[1][1],m[2][1]]
	col3 = [m[0][2],m[1][2],m[2][2]]
	dia1 = [m[0][0],m[1][1],m[2][2]]
	dia2 = [m[0][2],m[1][1],m[2][0]]

	if (tris in m) or (tris == col1) or (tris == col2) or (tris == col3) or (tris == dia1) or (tris == dia2):
		return True
	else:
		return False

#Input matrix
matrix_input =[
	[1,2,3],
	[4,5,6],
	[7,8,9]
]

print welcome
print_matrix(matrix_input)

i=0 #counter. if this is equal to 4, there aren't a winner

#main cycle
while True:
	#player choice 1
	while True:
		p1 = raw_input('\nIn quale posizione vuoi mettere la x : ')
		if draw_tictoe(p1,matrix_input,'x') == True:
			break

	if check_result('x',matrix_input) :
		print_matrix(matrix_input)
		print '\nIl vincitore è il giocatore 1\n'
		break

	print_matrix(matrix_input)

	#player choice 2
	while True:
		p2 = raw_input('\nIn quale posizione vuoi mettere la o : ')
		if draw_tictoe(p2,matrix_input,'o') == True:
			break

	if check_result('o',matrix_input):
		print_matrix(matrix_input)
		print '\nIl vincitore è il giocatore 2\n'
		break

	print_matrix(matrix_input)

	i+=1
	if i == 4:
		print '\nPareggio ! Nessun vincitore\n'
		break
