
import pygame
import random

# 1. AYARLAR VE RENKLER
WIDTH, HEIGHT = 800, 600
TILE_SIZE = 40
GRAVITY = 0.5

SKY_BLUE = (135, 206, 235)
DIRT_BROWN = (139, 69, 19)
GRASS_GREEN = (34, 139, 34)
STONE_GRAY = (100, 100, 100) # Taş
COAL_BLACK = (20, 20, 20)    # Kömür
PLAYER_RED = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BlockVerse: Maden Operasyonu")
clock = pygame.time.Clock()

# 2. DÜNYA OLUŞTURMA (Madenler Rastgele Dağıtılıyor)
world_data = []
for row in range(HEIGHT // TILE_SIZE):
    r = []
    for col in range(WIDTH // TILE_SIZE):
        if row > 10: # Toprak seviyesi
            sans = random.randint(1, 100)
            if sans < 15:   # %15 şansla TAŞ (2)
                r.append(2)
            elif sans < 5:  # %5 şansla KÖMÜR (3)
                r.append(3)
            else:           # Geri kalanı TOPRAK (1)
                r.append(1)
        else:
            r.append(0) # GÖKYÜZÜ (0)
    world_data.append(r)

# 3. OYUNCU SINIFI
class Player:
    def __init__(self):
        self.rect = pygame.Rect(100, 100, 30, 50)
        self.vel_y = 0
        self.on_ground = False

    def update(self):
        dx, dy = 0, 0
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]: dx -= 5
        if keys[pygame.K_d]: dx += 5
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = -10
            self.on_ground = False

        self.vel_y += GRAVITY
        dy += self.vel_y

        # Yatay hareket ve çarpışma
        self.rect.x += dx
        # Dikey hareket ve yer kontrolü
        self.rect.y += dy
        
        if self.rect.bottom > HEIGHT - 40:
            self.rect.bottom = HEIGHT - 40
            self.on_ground = True
            self.vel_y = 0

    def draw(self):
        pygame.draw.rect(screen, PLAYER_RED, self.rect)

player = Player()

# 4. ANA OYUN DÖNGÜSÜ
run = True
while run:
    screen.fill(SKY_BLUE)
    
    # DÜNYAYI ÇİZ (elif yapısıyla renkleri ayırıyoruz)
    for row_idx, row in enumerate(world_data):
        for col_idx, tile in enumerate(row):
            x = col_idx * TILE_SIZE
            y = row_idx * TILE_SIZE
            
            if tile == 1: # TOPRAK
                pygame.draw.rect(screen, DIRT_BROWN, (x, y, TILE_SIZE, TILE_SIZE))
                pygame.draw.rect(screen, GRASS_GREEN, (x, y, TILE_SIZE, TILE_SIZE), 2)
            elif tile == 2: # TAŞ
                pygame.draw.rect(screen, STONE_GRAY, (x, y, TILE_SIZE, TILE_SIZE))
                pygame.draw.rect(screen, (50, 50, 50), (x, y, TILE_SIZE, TILE_SIZE), 1)
            elif tile == 3: # KÖMÜR
                pygame.draw.rect(screen, COAL_BLACK, (x, y, TILE_SIZE, TILE_SIZE))
                pygame.draw.rect(screen, (255, 255, 255), (x, y, TILE_SIZE, TILE_SIZE), 1)

    # FARE ETKİLEŞİMİ (Kırma ve Koyma)
    mouse_pos = pygame.mouse.get_pos()
    col = mouse_pos[0] // TILE_SIZE
    row = mouse_pos[1] // TILE_SIZE

    if pygame.mouse.get_pressed()[0]: # Sol tık: KIR
        if row < len(world_data) and col < len(world_data[0]):
            world_data[row][col] = 0
            
    if pygame.mouse.get_pressed()[2]: # Sağ tık: KOY (Toprak koyar)
        if row < len(world_data) and col < len(world_data[0]):
            world_data[row][col] = 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    player.update()
    player.draw()
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
