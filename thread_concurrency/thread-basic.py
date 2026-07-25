import threading
import time

def take_order():
    for i in range(1,5):
        print(f"Taking order no:{i}")
        time.sleep(1)
        
        
def brew_order():
    for i in range(1,5):
        print(f"Brew order no:{i}")
        time.sleep(2)
        
    
    
    
order =  threading.Thread(target=take_order)
brewOrder = threading.Thread(target=brew_order)

order.start()
brewOrder.start()


order.join()
brewOrder.join()

    
                