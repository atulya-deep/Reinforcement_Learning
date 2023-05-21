class Environment:
    def _init_(self):
        self.grid = np.array([[0, 0, 0],
                              [0, 0, 0],
                              [0, 0, 0]])
        self.rewards = defaultdict(int)
        self.rewards[3,1] = 100
        self.rewards[3,2] = -100
        self.rewards[2,2] = -100
        self.rewards[1,2] = -100
        self.rewards[0,2] = 100
        self.rewards[2,1] = -100
        self.rewards[1,1] = 100
        self.rewards[0,1] = -100
        self.rewards[2,0] = 100
        self.rewards[1,0] = -100
        self.rewards[0,0] = 100
        self.possible_actions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        self.num_actions = len(self.possible_actions)

    def move(self, action):
        x, y = self.state
        new_x, new_y = x + self.possible_actions[action][0], y + self.possible_actions[action][1]
        if new_x < 0 or new_y < 0 or new_x > 2 or new_y > 2:
            return x, y, -1
        return new_x, new_y, self.rewards[new_x, new_y]

    def reset(self):
        self.state
