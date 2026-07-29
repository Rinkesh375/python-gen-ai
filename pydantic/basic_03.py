from pydantic import BaseModel
from typing import List, Dict, Optional

class CartItem(BaseModel):
    id:int
    items:List[str]
    qtyItems:Dict[str,int]
    couponCode:Optional[str] = None
    


cart1 = CartItem(id=1,items=["Keyboard","Mouse","Earphone"],qtyItems={"Keyboard":1,"Mouse":5})    
print(cart1)