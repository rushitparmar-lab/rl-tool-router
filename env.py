# env.py
from tools import search_web, calculate_math, execute_python_code, fetch_url, read_file, save_to_file

class RLEnvironment:
    def __init__(self, config):
        self.config = config
        self.current_step = 0
        self.max_steps = config.get("max_steps", 10)
        self.state = None

    def reset(self, prompt=""):
        """Resets the environment for a new episode."""
        self.current_step = 0
        self.state = {"prompt": prompt, "history": []}
        return self.state

    def step(self, action: dict):
        """
        Executes a single step in the environment.
        Expected action format: {"tool": "search_web", "args": "python tutorial"}
        """
        self.current_step += 1
        
        # TODO: Implement actual tool dispatching logic here
        observation = "Tool execution result stub"
        
        # Append to history so get_reward can evaluate the trajectory
        self.state["history"].append((action, observation))
        
        done = self.current_step >= self.max_steps
        
        # Only return the final reward if the episode is done
        reward = self.get_reward() if done else 0.0
        info = {}
        
        return observation, reward, done, info

    def get_reward(self):
        """Evaluates the state history to provide a score for GRPO."""
        # TODO: Implement reward logic (e.g., checking if the final answer is correct)
        return 0.5
