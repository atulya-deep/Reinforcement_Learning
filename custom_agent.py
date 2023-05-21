class Agent:
    def _init_(self, env):
        self.env = env
        self.state = self.env.reset()
        self.gamma = 0.9
        self.Q = defaultdict(lambda: [0, 0, 0, 0])

    def update_Q(self, state, action, reward, next_state):
        self.Q[state][action] = self.Q[state][action] + 0.1 * (reward + self.gamma * max(self.Q[next_state]) - self.Q[state][action])

    def get_action(self):
        if np.random.uniform(0, 1) < 0.1:
            return np.random.choice(self.env.num_actions)
        return np.argmax(self.Q[self.state])

    def train(self):
        for i in range(100):
            total_reward = 0
            state = self.env.reset()
            while True:
                action = self.get_action()
                next_state, reward = self.env.move(action)
                total_reward += reward
                self.update_Q(state, action, reward, next_state)
                if next_state == state:
                    break
                state = next_state
            print(total)
