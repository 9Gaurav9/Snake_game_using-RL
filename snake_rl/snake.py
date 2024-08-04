# import pygame
# import random

# class SnakeGame:
#     def __init__(self):
#         pygame.init()
#         self.display = pygame.display.set_mode((500, 500))
#         pygame.display.set_caption('Snake Game')
#         self.clock = pygame.time.Clock()
#         self.reset()

#     def reset(self):
#         self.game_over = False
#         self.snake = [[250, 250], [240, 250], [230, 250]]
#         self.food = self._place_food()
#         self.direction = 'RIGHT'
#         self.score = 0
#         return self._get_state()

#     def step(self, action):
#         self._move(action)
#         if self.snake[0] == self.food:
#             self.score += 1
#             self.food = self._place_food()
#             reward = 10
#         else:
#             self.snake.pop()
#             reward = -1
        
#         if self._is_collision():
#             self.game_over = True
#             reward = -10
        
#         self._update_ui()
#         self.clock.tick(30)
#         return self._get_state(), reward, self.game_over, self.score

#     def _get_state(self):
#         head = self.snake[0]
#         return [head[0], head[1], self.food[0], self.food[1]]

#     def _move(self, action):
#         directions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
#         self.direction = directions[action]

#         if self.direction == 'UP':
#             self.snake.insert(0, [self.snake[0][0], self.snake[0][1] - 10])
#         elif self.direction == 'DOWN':
#             self.snake.insert(0, [self.snake[0][0], self.snake[0][1] + 10])
#         elif self.direction == 'LEFT':
#             self.snake.insert(0, [self.snake[0][0] - 10, self.snake[0][1]])
#         elif self.direction == 'RIGHT':
#             self.snake.insert(0, [self.snake[0][0] + 10, self.snake[0][1]])

#     def _place_food(self):
#         return [random.randint(0, 49) * 10, random.randint(0, 49) * 10]

#     def _is_collision(self):
#         head = self.snake[0]
#         if head[0] < 0 or head[0] >= 500 or head[1] < 0 or head[1] >= 500:
#             return True
#         if head in self.snake[1:]:
#             return True
#         return False

#     def _update_ui(self):
#         self.display.fill((0, 0, 0))
#         for part in self.snake:
#             pygame.draw.rect(self.display, (0, 255, 0), pygame.Rect(part[0], part[1], 10, 10))
#         pygame.draw.rect(self.display, (255, 0, 0), pygame.Rect(self.food[0], self.food[1], 10, 10))
#         pygame.display.flip()

#     def run(self):
#         while not self.game_over:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     self.game_over = True
#                     break

#             keys = pygame.key.get_pressed()
#             if keys[pygame.K_UP]:
#                 self.step(0)
#             if keys[pygame.K_DOWN]:
#                 self.step(1)
#             if keys[pygame.K_LEFT]:
#                 self.step(2)
#             if keys[pygame.K_RIGHT]:
#                 self.step(3)
