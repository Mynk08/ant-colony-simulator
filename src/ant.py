"""Ant agent implementation for colony simulation."""
import random
import math

class Ant:
    def __init__(self, x, y, colony):
        self.x = x
        self.y = y
        self.colony = colony
        self.has_food = False
        self.pheromone_strength = 100

    def move(self, pheromone_map):
        """Move based on pheromone trails and random exploration."""
        directions = self._get_possible_directions()

        if self.has_food:
            # Return to colony
            direction = self._get_direction_to_colony()
        elif self._detect_pheromones(pheromone_map):
            # Follow pheromone trail
            direction = self._follow_pheromones(pheromone_map)
        else:
            # Random exploration
            direction = random.choice(directions)

        self.x += direction[0]
        self.y += direction[1]

    def _get_possible_directions(self):
        return [(0,1), (1,0), (0,-1), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]

    def _get_direction_to_colony(self):
        dx = self.colony.x - self.x
        dy = self.colony.y - self.y
        magnitude = math.sqrt(dx**2 + dy**2)
        if magnitude == 0:
            return (0, 0)
        return (int(dx/magnitude), int(dy/magnitude))

    def _detect_pheromones(self, pheromone_map):
        return pheromone_map.get((self.x, self.y), 0) > 0

    def _follow_pheromones(self, pheromone_map):
        best_dir = (0, 0)
        max_pheromone = 0
        for direction in self._get_possible_directions():
            new_x = self.x + direction[0]
            new_y = self.y + direction[1]
            pheromone = pheromone_map.get((new_x, new_y), 0)
            if pheromone > max_pheromone:
                max_pheromone = pheromone
                best_dir = direction
        return best_dir
