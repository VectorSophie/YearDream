pip.main(['install', "pygame"]) 
pip.main(['install', "sys"]) 

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Time Loop Bullet Hell")

font = pygame.font.SysFont("timesnewroman", 30)

score = 0
corruption = 0  # 0 to 20

running = True
while running:
    screen.fill((0, 0, 0)) 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (20, 20))
    
    corruption_text = font.render(f"Corruption: {corruption}/20", True, (255, 255, 255))
    screen.blit(corruption_text, (20, 60))
    
    if corruption >= 10:
        if pygame.time.get_ticks() % 500 < 250:
            corruption_text = font.render("Corruption: ???", True, (255, 0, 0))
            screen.blit(corruption_text, (20, 60))
    
    pygame.display.flip()
    
pygame.quit()
sys.exit()
