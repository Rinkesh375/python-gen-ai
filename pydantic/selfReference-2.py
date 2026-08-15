from typing import List
from pydantic import BaseModel, Field


class Comment(BaseModel):
    id: int
    content: str
    replies: List["Comment"] = Field(default_factory=list)


Comment.model_rebuild()

comment = Comment(
    id=1,
    content="First comment",
    replies=[
        Comment(id=2, content="Reply 1"),
        Comment(
            id=3,
            content="Reply 2",
            replies=[
                Comment(id=4, content="Nested reply")
            ]
        ),
    ],
)

print(comment)