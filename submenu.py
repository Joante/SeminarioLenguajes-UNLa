import pygame, sys


def dumbmenu(screen, menu, x_pos = 100, y_pos = 100, font = None,
            size = 70, distance = 1.4, fgcolor = (255,255,255),
            cursorcolor = (255,0,0), exitAllowed = True):

	# Draw the Menupoints
	pygame.font.init()
	if font == None:
		myfont = pygame.font.Font(None, size)
	else:
		myfont = pygame.font.SysFont(font, size)
	cursorpos = 0
	renderWithChars = False
	for i in menu:
		if renderWithChars == False:
			text =  myfont.render(str(cursorpos + 1)+".  " + i,
				True, fgcolor)
		else:
			text =  myfont.render(chr(char)+".  " + i,
				True, fgcolor)
			char += 1
		textrect = text.get_rect()
		textrect = textrect.move(x_pos, 
		           (size // distance * cursorpos) + y_pos)
		screen.blit(text, textrect)
		pygame.display.update(textrect)
		cursorpos += 1
		if cursorpos == 9:
			renderWithChars = True
			char = 65

	# Draw the ">", the Cursor
	cursorpos = 0
	cursor = myfont.render(">", True, cursorcolor)
	cursorrect = cursor.get_rect()
	cursorrect = cursorrect.move(x_pos - (size // distance),
	             (size // distance * cursorpos) + y_pos)

	# The whole While-loop takes care to show the Cursor, move the
	# Cursor and getting the Keys (1-9 and A-Z) to work...
	ArrowPressed = True
	exitMenu = False
	clock = pygame.time.Clock()
	filler = pygame.Surface.copy(screen)
	fillerrect = filler.get_rect()
	while True:
		clock.tick(30)
		if ArrowPressed == True:
			screen.blit(filler, fillerrect)
			pygame.display.update(cursorrect)
			cursorrect = cursor.get_rect()
			cursorrect = cursorrect.move(x_pos - (size // distance),
			             (size // distance * cursorpos) + y_pos)
			screen.blit(cursor, cursorrect)
			pygame.display.update(cursorrect)
			ArrowPressed = False
		if exitMenu == True:
			break
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return -1
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE and exitAllowed == True:
					if cursorpos == len(menu) - 1:
						exitMenu = True
					else:
						cursorpos = len(menu) - 1; ArrowPressed = True


				# This Section is huge and ugly, I know... But I don't
				# know a better method for this^^
				if event.key == pygame.K_1:
					cursorpos = 0; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_2 and len(menu) >= 2:
					cursorpos = 1; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_3 and len(menu) >= 3:
					cursorpos = 2; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_4 and len(menu) >= 4:
					cursorpos = 3; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_5 and len(menu) >= 5:
					cursorpos = 4; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_6 and len(menu) >= 6:
					cursorpos = 5; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_7 and len(menu) >= 7:
					cursorpos = 6; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_8 and len(menu) >= 8:
					cursorpos = 7; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_9 and len(menu) >= 9:
					cursorpos = 8; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_a and len(menu) >= 10:
					cursorpos = 9; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_b and len(menu) >= 11:
					cursorpos = 10; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_c and len(menu) >= 12:
					cursorpos = 11; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_d and len(menu) >= 13:
					cursorpos = 12; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_e and len(menu) >= 14:
					cursorpos = 13; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_f and len(menu) >= 15:
					cursorpos = 14; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_g and len(menu) >= 16:
					cursorpos = 15; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_h and len(menu) >= 17:
					cursorpos = 16; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_i and len(menu) >= 18:
					cursorpos = 17; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_j and len(menu) >= 19:
					cursorpos = 18; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_k and len(menu) >= 20:
					cursorpos = 19; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_l and len(menu) >= 21:
					cursorpos = 20; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_m and len(menu) >= 22:
					cursorpos = 21; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_n and len(menu) >= 23:
					cursorpos = 22; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_o and len(menu) >= 24:
					cursorpos = 23; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_p and len(menu) >= 25:
					cursorpos = 24; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_q and len(menu) >= 26:
					cursorpos = 25; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_r and len(menu) >= 27:
					cursorpos = 26; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_s and len(menu) >= 28:
					cursorpos = 27; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_t and len(menu) >= 29:
					cursorpos = 28; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_u and len(menu) >= 30:
					cursorpos = 29; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_v and len(menu) >= 31:
					cursorpos = 30; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_w and len(menu) >= 32:
					cursorpos = 31; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_x and len(menu) >= 33:
					cursorpos = 32; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_y and len(menu) >= 34:
					cursorpos = 33; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_z and len(menu) >= 35:
					cursorpos = 34; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_UP:
					ArrowPressed = True
					if cursorpos == 0:
						cursorpos = len(menu) - 1
					else:
						cursorpos -= 1
				elif event.key == pygame.K_DOWN:
					ArrowPressed = True
					if cursorpos == len(menu) - 1:
						cursorpos = 0
					else:
						cursorpos += 1
				elif event.key == pygame.K_KP_ENTER or \
				     event.key == pygame.K_RETURN:
							exitMenu = True
	
	return cursorpos

if __name__ == '__main__':
	sys.stderr.write("You should import me, not start me...")
	sys.exit()
