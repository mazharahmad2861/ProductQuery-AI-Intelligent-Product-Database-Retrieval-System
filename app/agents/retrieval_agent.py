import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from app.db.database import fetch_products_by_ids

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index("app/vectorstore/products_index.faiss")
id_map = np.load("app/vectorstore/id_map.npy")

def retrieval_agent(state):
    query_embedding = model.encode(
        [state.user_query], normalize_embeddings=True
    )

    scores, indices = index.search(query_embedding, k=10)
    product_ids = [int(id_map[i]) for i in indices[0]]

    rows = fetch_products_by_ids(product_ids)

    products = []
    for r in rows:
        products.append({
            "id": r[0],
            "name": r[1],
            "brand": r[2],
            "category": r[3],
            "price": r[4],
            "rating": r[5],
            "description": r[6],
            "stock": r[7],
        })

    state.retrieved_items = products
    return state
