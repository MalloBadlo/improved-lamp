import pygame, sys
import numpy as np

# Initializes pygame
pygame.init()

# --------
# Costants
# --------

score_X = 0
score_Y = 0

GAME_WIDTH = 600	
GAME_HEIGHT = 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COL = 3
CIRCLE_RADIUS = 30
CIRCLE_WIDTH = 10
CROSS_WIDTH = 15
SQUARE_SIZE = 250
SPACE_X = 180
SPACE_Y = 220

#RGB: red, green, blue
BG_COLOR = (160, 160, 160)
LINE_COLOR = (96, 96, 96)
CIRCLE_COLOR = (255, 255, 153)
CROSS_COLOR = (0, 153, 153)
GREEN_LIGHT = (178, 255, 102)
GREEN_LIGHTER = (204, 255, 153)
WHITE = (255,255,255)
RED = (204,0,0)
RED_LIGHTER = (255, 51, 51)
# ------
# Screen
# ------
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
icon = pygame.image.load('tris.png')
pygame.display.set_icon(icon)
screen.fill(BG_COLOR)

# ----------
# Game board
# ----------
board = np.zeros((BOARD_COL, BOARD_ROWS))

# ---------
# Functions
# ---------
def draw_lines():
	# horizontal 1
	pygame.draw.line(screen, LINE_COLOR, (150, SQUARE_SIZE), (450, SQUARE_SIZE), LINE_WIDTH)
	# horizontal 2
	pygame.draw.line(screen, LINE_COLOR, (150, SQUARE_SIZE + 100), (450, SQUARE_SIZE + 100), LINE_WIDTH)

	#vertical 1
	pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 150), (SQUARE_SIZE, 450), LINE_WIDTH)
	#vertical 2
	pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE + 100, 150), (SQUARE_SIZE + 100, 450), LINE_WIDTH)


def draw_figures():
	
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COL):
			if board[row][col] == 1:
				pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * 100 + 200), int(row * 100 + 200)), CIRCLE_RADIUS, CIRCLE_WIDTH )

			elif board[row][col] == 2:
				pygame.draw.line(screen, CROSS_COLOR, (col * 100 + SPACE_X, row * 100 + SPACE_X), (col * 100 + SPACE_Y , row * 100 + SPACE_Y), CROSS_WIDTH)
				pygame.draw.line(screen, CROSS_COLOR, (col * 100 + SPACE_Y, row * 100 + SPACE_X), (col * 100 + SPACE_X, row * 100 + SPACE_Y), CROSS_WIDTH)



def avaible_square(row, col):
	return board[row][col] == 0

def mark_square(row, col, player):
	board[row][col] = player

def is_board_full():
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COL):
			if board[row][col] == 0:
				return False

	return True


def check_win(player):
	# vertical win
	for col in range(BOARD_COL):
		if board[0][col] == player and board[1][col] == player and board[2][col] == player:
			draw_vertical_winning(col,player)
			return True

	# horizontal win
	for row in range(BOARD_ROWS):
		if board[row][0] == player and board[row][1] == player and board[row][2] == player:
			draw_horizontal_winning(row,player)
			return True

	# asc diagonal win
	if board[2][0] == player and board[1][1] == player and board[0][2] == player:
		draw_asc_diagonal_winning(player)
		return True

	# desc diagonal win
	if board[0][0] == player and board[1][1] == player and board[2][2] == player:
		draw_desc_diagonal_winning(player)
		return True

	return False



def draw_vertical_winning(col, player):
	posX = col * 100 + 200

	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line(screen, color, (posX,150),(posX,450),10)

def draw_horizontal_winning(row, player):
	posY = row * 100 + 200

	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line(screen, color , (150,posY),(450,posY),10)


def draw_asc_diagonal_winning(player):
	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line(screen, color, (150, 450), (450,150),10)


def draw_desc_diagonal_winning(player):
	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line(screen, color , (150,150), (450,450), 10)

def show_score():
	font = pygame.font.SysFont('bellgrassetto', 25)
	scoreX = font.render('X - ' + str(score_X), False, WHITE).convert()
	scoreY = font.render('O - ' + str(score_Y), False, WHITE).convert()
	screen.blit(scoreX, ((10,10)))
	screen.blit(scoreY,((8,40)))
	

def restart():
	screen.fill( BG_COLOR )
	draw_lines()
	show_score()
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COL):
			board[row][col] = 0

# ---------
# Variables
# ---------
player = 2
game_over = False


draw_lines()
show_score()




		

# Game loop
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

			mouseX = event.pos[0]
			mouseY = event.pos[1]

			clicked_row = -1
			clicked_column = -1

			if 150 <= mouseX < SQUARE_SIZE and 150 <= mouseY < SQUARE_SIZE:
				clicked_row = 0
				clicked_column = 0

			elif SQUARE_SIZE <= mouseX < SQUARE_SIZE + 100 and 150 <= mouseY < SQUARE_SIZE:
				clicked_row = 0
				clicked_column = 1

			elif SQUARE_SIZE + 100 <= mouseX < SQUARE_SIZE + 200 and 150 <= mouseY < SQUARE_SIZE:
				clicked_row = 0
				clicked_column = 2



			elif 150 <= mouseX < SQUARE_SIZE and 260 <= mouseY < SQUARE_SIZE + 100:
				clicked_row = 1
				clicked_column = 0

			elif SQUARE_SIZE <= mouseX < SQUARE_SIZE + 100 and 260 <= mouseY < SQUARE_SIZE + 100:
				clicked_row = 1
				clicked_column = 1

			elif SQUARE_SIZE + 100 <= mouseX < SQUARE_SIZE + 200  and 260 <= mouseY < SQUARE_SIZE + 100:
				clicked_row = 1
				clicked_column = 2



			elif 150 <= mouseX < SQUARE_SIZE and 360 <= mouseY < SQUARE_SIZE + 200:
				clicked_row = 2
				clicked_column = 0

			elif SQUARE_SIZE <= mouseX < SQUARE_SIZE + 100 and 360 <= mouseY < SQUARE_SIZE + 200:
				clicked_row = 2
				clicked_column = 1

			elif SQUARE_SIZE + 100 <= mouseX < SQUARE_SIZE + 200 and 360 <= mouseY < SQUARE_SIZE + 200:
				clicked_row = 2
				clicked_column = 2



			if clicked_column != -1 and clicked_row != -1:
				if avaible_square(clicked_row, clicked_column):
					mark_square(clicked_row, clicked_column, player)
					if check_win(player):
						if player == 2:
							score_X += 1
						else: score_Y += 1
						game_over = True

					if is_board_full():
						game_over = True
					
					
					player = player % 2 + 1
					

					draw_figures()

		if game_over:
			mouse = pygame.mouse.get_pos()
			font1 = pygame.font.SysFont('lucidasansdemigrassetto', 25)
			font2 = pygame.font.SysFont('lucidasansdemigrassetto', 20)
			play_again = font1.render('Play again', False, WHITE).convert()
			quit = font2.render('Quit', False ,WHITE).convert()

			if 220 <= mouse[0] <= 505 and 480 <= mouse[1] <= 530:
				pygame.draw.rect(screen, GREEN_LIGHTER, (220,480,150,50))

			else: 
				pygame.draw.rect(screen, GREEN_LIGHT, (220,480,150,50))


			if  240 <= mouse[0] <= 340 and 550 <= mouse[1] <= 580:
				pygame.draw.rect(screen, RED_LIGHTER, (245, 550,100,30))

			else:
				pygame.draw.rect(screen, RED, (245, 550,100,30))

			screen.blit(play_again, (230,480))
			screen.blit(quit, (275,550))


			if event.type == pygame.MOUSEBUTTONDOWN:
				if 220 <= mouse[0] <= 505 and 480 <= mouse[1] <= 530:
					restart()
					player = 2
					game_over = False

				elif 240 <= mouse[0] <= 340 and 550 <= mouse[1] <= 580:
					sys.exit()





	pygame.display.update()

