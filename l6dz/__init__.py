from statistics import mean

import queen_task

import time
start_time = time.time()
for i, res in enumerate(queen_task.generate_all(), start=1):
    print(f"{i}: {res}")
print("--- %s seconds ---" % (time.time() - start_time))