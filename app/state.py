from typing import List, Dict, Any
from pydantic import BaseModel

class GraphState(BaseModel):
    user_query: str
    intent: str | None = None
    filters: Dict[str, Any] = {}
    retrieved_items: List[Dict] = []
    ranked_items: List[Dict] = []
    response: Any = None
