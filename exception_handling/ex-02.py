def loading_state(state):
    try:
        if isinstance(state,bool):
            print(f"{"LOADING..." if state else "NOT LOADING..."}")
        else:
            raise ValueError(f"{state} is not boolean.")  
    except ValueError as e:
        print(e)
    finally:
        print("Pass Next stage please")    
              
            
           
loading_state(1)  
loading_state("")
loading_state("Rinkesh")
loading_state([])
loading_state({})
loading_state(True)              
            