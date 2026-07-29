from pydantic import BaseModel
from typing import Any, Dict, List

class ApiResponse(BaseModel):
    data: Dict[str, Any]

response = ApiResponse(
    data={
        "user": {
            "id": 1,
            "name": "Rinkesh",
            "verified": True
        },
        "orders": [
            {
                "id": 101,
                "amount": 999
            },
            {
                "id": 102,
                "amount": 1499
            }
        ],
        "totalOrders": 2,
        "success": True
    }
)

print(response)