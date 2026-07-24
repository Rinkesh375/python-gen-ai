class Employee:
    def __init__(self,name,role):
        self.name= name
        self.role = role
        
    def get_user_info(self):
        return f"name:{self.name} role:{self.role}"    
    
    
    
employeeOne = Employee("Rinkesh","Full Stack Developer")

print(employeeOne.get_user_info())
