import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

FAISS_INDEX_PATH = "app/vectorstore/products_index.faiss"
ID_MAP_PATH = "app/vectorstore/id_map.npy"

_model = None
_index = None
_id_map = None


def load_faiss():
    global _model, _index, _id_map

    if _index is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")
        _index = faiss.read_index(FAISS_INDEX_PATH)
        _id_map = np.load(ID_MAP_PATH)

    return _model, _index, _id_map


def semantic_search(query: str, top_k: int = 10):
    model, index, id_map = load_faiss()

    query_vector = model.encode(
        [query], normalize_embeddings=True
    )

    scores, indices = index.search(query_vector, top_k)

    return [int(id_map[i]) for i in indices[0]]
