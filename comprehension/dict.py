employeesSalaryUSD = {
    "Rinkesh":500,
    "Abhishek":2000,
    "Shubham":1300,
    "Lokesh":800
} 

employeesSalaryInr = {
  key:value*96 for key,value in employeesSalaryUSD.items()
}


print(employeesSalaryInr)