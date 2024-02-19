import gymnasium as gym

def pacman_play():
    # Load the game environment
    env = gym.make('ALE/MsPacman-v5', render_mode='human')  # Adjust the environment ID if necessary.
    
    episodes = 3  # Number of episodes you want to run
    for episode in range(1, episodes + 1):
        observation = env.reset()  # Reset the environment for a new episode
        done = False
        score = 0
        
        while not done:
            action = compute_action(env)
            observation, reward, done, info, _ = env.step(action)
            score += reward  # Update the score
        
        print(f"Episode: {episode}, Score: {score}")
    
    env.close()  # Close the environment

def compute_action(env):
    action = env.action_space.sample() # Random play, replace with your method
    return action

if __name__ == '__main__':
    pacman_play()
