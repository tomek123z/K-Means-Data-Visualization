import pygame

pygame.init()

screen = pygame.display.set_mode((1200,700))

pygame.display.set_caption("kmeans visualization")

running = True
	
clock = pygame.time.Clock()

BACKGROUND = (214, 214, 214)
BLACK = (0,0,0)
BACKGROUND_PANEL = (249, 255, 230)
WHITE = (255,255,255)

font = pygame.font.SysFont('sans', 40)
font_small = pygame.font.SysFont('sans', 20)
text_plus = font.render('+', True, WHITE)
text_minus = font.render('-', True, WHITE)
text_run = font.render("Run", True, WHITE)
text_random = font.render("Random", True, WHITE)
text_algorithm = font.render("Algorithm", True, WHITE)
text_reset = font.render("Reset", True, WHITE)

K = 0
error = 0
points = []

while running:
	clock.tick(60)
	screen.fill(BACKGROUND)
	mouse_x, mouse_y = pygame.mouse.get_pos()

	# Draw interface
	# Draw panel
	pygame.draw.rect(screen, BLACK, (50,50,700,500))
	pygame.draw.rect(screen, BACKGROUND_PANEL, (55,55,690,490))

	# K button + 
	pygame.draw.rect(screen, BLACK, (850,50,50,50))
	screen.blit(text_plus, (860,50))

	# K button -
	pygame.draw.rect(screen, BLACK, (950,50,50,50))
	screen.blit(text_minus, (960,50))

	# K value
	text_k = font.render("K = " + str(K), True, BLACK)
	screen.blit(text_k, (1050,50))

	# run button
	pygame.draw.rect(screen, BLACK, (850,150,150,50))
	screen.blit(text_run, (900,150))

	# random button
	pygame.draw.rect(screen, BLACK, (850,250,150,50))
	screen.blit(text_random, (850,250))

	# Reset button
	pygame.draw.rect(screen, BLACK, (850,550,150,50))
	screen.blit(text_reset, (850,550))	

	# Algorithm button
	pygame.draw.rect(screen, BLACK, (850,450,150,50))
	screen.blit(text_algorithm, (850,450))	

	# Error text
	text_error = font.render("Error = " + str(error), True, BLACK)
	screen.blit(text_error, (850,350))

	# Draw mouse position when mouse is in panel
	if 50 < mouse_x < 750 and 50 < mouse_y < 550:
		text_mouse = font_small.render("(" + str(mouse_x - 50) + "," + str(mouse_y - 50) + ")",True, BLACK)
		screen.blit(text_mouse, (mouse_x + 10, mouse_y))

	# End draw interface

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			# Create point on panel
			if 50 < mouse_x < 750 and 50 < mouse_y < 550:
				point = [mouse_x -50, mouse_y-50]
				points.append(point)
				print(points)

			# Change K button +
			if 850 < mouse_x < 900 and 50 < mouse_y < 100:
				K = K+1
				print("Press K +")
			
			# Change K button -
			if 950 < mouse_x < 1000 and 50 < mouse_y < 100:
				if K > 0:
					K -= 1
				print("Press K -")

			# Run button
			if 850 < mouse_x < 1000 and 150 < mouse_y < 200:
				print("run pressed")

			# Random button
			if 850 < mouse_x < 1000 and 250 < mouse_y < 300:
				print("random pressed")

			# Reset button
			if 850 < mouse_x < 1000 and 550 < mouse_y < 600:
				print("reset button pressed")

			# Algorithm 
			if 850 < mouse_x < 1000 and 450 < mouse_y < 500:
				print("Algorithm button pressed")

	# Draw point
	for i in range(len(points)):	
		pygame.draw.circle(screen,BLACK, (points[i][0] + 50, points[i][1] + 50), 6)
		pygame.draw.circle(screen,WHITE, (points[i][0] + 50, points[i][1] + 50), 5)

	pygame.display.flip()

pygame.quit()