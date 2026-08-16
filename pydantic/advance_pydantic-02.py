from pydantic import BaseModel

class TextContent(BaseModel):
    type: str = "text"
    content: str
    
   
   
   
text = TextContent(
    content="Hello World"
)    
    
    
    
print(text)    
    