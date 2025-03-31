import random
import os

def get_user_agent():
    path = os.path.join(
        os.path.join(os.path.dirname(__file__)),
        "..",
        "..",
        "..",
        "data",
        "useragents.txt",
    )
    user_agents = open(path).read().splitlines()
    user_agent = random.choice(user_agents)