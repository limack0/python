from time import time,sleep
import time
from tqdm import tqdm
from alive_progress import *
def progression():
    for i in tqdm(range(100)):
        sleep(0.05)
        
def progression_alive(message):
    with alive_bar(100, title="Décollage", bar='halloween') as bar :
        for i in range(100):
            time.sleep(0.05)
            bar()

progression_alive("voila") # exemple