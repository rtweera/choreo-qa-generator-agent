from pydantic import BaseModel
from typing import List

class TopicList(BaseModel):
    topics: List[str]
