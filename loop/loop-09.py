"""


months = ["Jan","Feb","Mar","Apr","May","June","July","August","September","October","November","December"]


for i in months:
    if(i == "Janu"):
        break
    
else:
    print("Janu not and it does break my loop found")  
    
    
""" 

print("------------------------------------------------------------------------------------------------------------------------------")

"""

months = ["Jan","Feb","Mar","Apr","May","June","July","August","September","October","November","December"]


for i in months:
    if(i == "Apr"):
        break
    
else:
    print("Apr found because that loop did not run complety so it will come inside the else condition here and this print will never be executed")
    
    
    """
    
    
    
    
    
    
    
    
    
months = ["Jan","Feb","Mar","Apr","May","June","July","August","September","October","November","December"]


for i in months:
    if(i == "Apr" or i == "Jan" or i == "June"):
        continue
    
else:
    print("this will run because loop run without break")    