import random
import os


def getRandomUserAgent():
    path = os.path.join(
        os.path.join(os.path.dirname(__file__)),
        "..",
        "..",
        "..",
        "data",
        "useragents.txt",
    )
    userAgents = open(path).read().splitlines()
    userAgent = random.choice(userAgents)