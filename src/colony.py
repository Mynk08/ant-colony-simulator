"""Colony management and simulation."""
from ant import Ant

class Colony:
    def __init__(self, x, y, num_ants=50):
        self.x = x
        self.y = y
        self.ants = [Ant(x, y, self) for _ in range(num_ants)]
        self.pheromone_map = {}
        self.food_collected = 0

    def update(self):
        """Update all ants and pheromones."""
        for ant in self.ants:
            ant.move(self.pheromone_map)
        self._evaporate_pheromones()

    def _evaporate_pheromones(self, rate=0.95):
        for pos in list(self.pheromone_map.keys()):
            self.pheromone_map[pos] *= rate
            if self.pheromone_map[pos] < 1:
                del self.pheromone_map[pos]
