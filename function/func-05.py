def multiple_values():
    name ="Rinkesh"
    age=25
    city = "FBD"
    country="India"
    return name,age,city,country
    
user = multiple_values()
name,city,age,country= multiple_values() 
#order should be the  same

print(user)   

print(f"name={name},city={city},age={age},country={country}")