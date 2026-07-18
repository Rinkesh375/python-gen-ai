def authorization(fn):
    def wrapper(name,user_role="user",):
        if (user_role == "admin"):
            fn(name)
        else:
            return "You can not run the application function you are not admin!"    
    return wrapper
    
    


@authorization
def admin_fn(name):
    print(f"Successfully run the {name}")


print(admin_fn("Rinkesh",""))  