import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from app.db.database import fetch_all_products

model = SentenceTransformer("all-MiniLM-L6-v2")

products = fetch_all_products()

texts = []
id_map = []

for p in products:
    product_id, name, brand, category, price, rating, desc, stock = p
    texts.append(f"{name} {desc}")
    id_map.append(product_id)

embeddings = model.encode(texts, normalize_embeddings=True)

index = faiss.IndexFlatIP(embeddings.shape[1])
index.add(embeddings)

faiss.write_index(index, "app/vectorstore/products_index.faiss")
np.save("app/vectorstore/id_map.npy", np.array(id_map))

print("FAISS index built successfully")
