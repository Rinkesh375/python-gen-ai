from multiprocessing import Process
import time


def brew_tea():
    
    count = 0
    for i in range(100000000):
        count += 1
    
    
if __name__ == "__main__":
    processOne = Process(target=brew_tea)  
    processTwo = Process(target=brew_tea)  


    start = time.time()
    processOne.start()
    processTwo.start()

    processOne.join()
    processTwo.join()
    end = time.time()

    print(f"{end-start}")