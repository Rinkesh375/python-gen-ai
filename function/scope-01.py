def outer_name():
    name="Rinkesh"
    def inner_name():
        nonlocal name
        name="Rinkesh Kumar"
        print(name)
    
    print(name)
    inner_name()
    print(name)    
    
    
outer_name()    