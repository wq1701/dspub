import time
from tqdm import tqdm
from tqdm import trange

for i in tqdm(range(100)):
    time.sleep(0.1)

# in some consoles, it will print a new line for every step. like below
# 1% |
# 2% ||
# 3% |||
# fix

for i in tqdm(range(100), leave=True, position=0):
    time.sleep(0.1)


for i in tqdm(range(100), desc="Training", unit="epoch"):
    time.sleep(0.1)

for i in trange(100, desc="Training", unit="epoch"):
    time.sleep(0.1)

# %% rich
from rich.progress import track

for i in track(range(100), description="Processing..."):
    # Simulate some processing time
    time.sleep(0.1)
