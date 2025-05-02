class Environment:
    def __init__(self, location_A='Dirty', location_B='Dirty'):
        self.location_A = location_A
        self.location_B = location_B
        self.vacuum_location = 'A'
        self.score = 0

    def __str__(self):
        return f"Location A: {self.location_A}, Location B: {self.location_B}, Vacuum at: {self.vacuum_location}"

class ReflexVacuumAgent:
    def __init__(self, env):
        self.env = env

    def perceive_and_act(self):
        if self.env.vacuum_location == 'A':
            if self.env.location_A == 'Dirty':
                self.env.location_A = 'Clean'
                self.env.score += 1  # Suck
                print("Sucked dirt at A")
            else:
                self.env.vacuum_location = 'B'
                print("Moved to B")
        elif self.env.vacuum_location == 'B':
            if self.env.location_B == 'Dirty':
                self.env.location_B = 'Clean'
                self.env.score += 1  # Suck
                print("Sucked dirt at B")
            else:
                self.env.vacuum_location = 'A'
                print("Moved to A")

# Running the environment
env = Environment(location_A='Dirty', location_B='Dirty')
agent = ReflexVacuumAgent(env)

# Simulate the agent's actions
for _ in range(4):  # run a few steps
    print(env)
    agent.perceive_and_act()

print("\nFinal State:")
print(env)
print("Performance Score:", env.score)
