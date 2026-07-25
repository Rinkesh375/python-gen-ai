import threading
import time


def brew_tea():
    print(f"{threading.current_thread().name} started brewing...")
    count = 0
    for i in range(100000000):
        count += 1
    print(f"{threading.current_thread().name} finished brewing...")
    
threadOne = threading.Thread(target=brew_tea,name="BaristaOne")  
threadTwo = threading.Thread(target=brew_tea,name="BaristaTwo")  


start = time.time()
threadOne.start()
threadTwo.start()

threadOne.join()
threadTwo.join()
end = time.time()

print(f"{end-start}")
 
        