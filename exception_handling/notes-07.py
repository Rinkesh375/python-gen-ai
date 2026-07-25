file = open("sample.txt","w")

try:
    file.write("This is sample text file which is being written in notes-07")
except Exception as error:
    print(error)
finally:
    file.close()        
    
    
try:
    file = open("student.txt", "w")
    file.write("Name : Rinkesh\n")
    file.write("Course : Python\n")
    file.write("City : Faridabad\n")

except Exception as error:
    print(error)

finally:
    file.close()    
    
    
try:
    file = open("student.txt", "r")

    data = file.read()

    print(data)

except FileNotFoundError:
    print("File not found.")

finally:
    file.close()    
    
    
    
try:

    file = open("student.txt", "a")

    file.write("Country : India\n")

except Exception as error:
    print(error)

finally:
    file.close()    
    
    
    
try:

    file = open("unknown.txt", "r")

    print(file.read())

except FileNotFoundError as error:

    print(error)

finally:

    print("Program Finished")    
    
    
    
try:

    file = open("student.txt", "r")

    print(file.readline())
    print(file.readline())

except Exception as error:

    print(error)

finally:

    file.close()    
    
    
    
try:

    source = open("student.txt", "r")

    destination = open("backup.txt", "w")

    destination.write(source.read())

except Exception as error:

    print(error)

finally:

    source.close()
    destination.close()    
    
    
    
import os

try:

    os.remove("backup.txt")

    print("File deleted.")

except FileNotFoundError:

    print("File already deleted.")

except PermissionError:

    print("Permission denied.")   
    
    
    

try:

    with open("notes.txt", "w") as file:

        file.write("Learning Python File Handling")

except Exception as error:

    print(error)    