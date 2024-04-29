import multiprocessing
import time
import random
import datetime

def process_function():
    
    wait_time = random.random()
    
    time.sleep(wait_time)
    
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current time: {current_time}")
    
    print("Exiting process.")

if __name__ == "__main__":
    
    processes = []
    for _ in range(3):
        p = multiprocessing.Process(target=process_function)
        processes.append(p)
        p.start()

    
    for p in processes:
        p.join()

    print("All processes have finished.")