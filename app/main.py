from fastapi import FastAPI
from pydantic import BaseModel
from app.graph import shopping_graph

app = FastAPI(title="AI Shopping Assistant")

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
def query_products(req: QueryRequest):
    result = shopping_graph.invoke(
        {"user_query": req.query}
    )
    return result["response"]
