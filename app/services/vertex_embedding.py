# services/vertex_embeddings.py
from vertexai.language_models import TextEmbeddingModel

# You must init VertexAI in your main before calling this
model = TextEmbeddingModel.from_pretrained("textembedding-gecko@001")

def chunk_text(text: str, max_chunk_chars: int = 1000):
    # Naive line-based chunker for now (improve later)
    chunks, current = [], []
    count = 0
    for line in text.splitlines():
        if count + len(line) > max_chunk_chars:
            chunks.append("\n".join(current))
            current, count = [], 0
        current.append(line)
        count += len(line)
    if current:
        chunks.append("\n".join(current))
    return chunks

def embed_text_chunks(text: str):
    chunks = chunk_text(text)
    embeddings = [model.get_embeddings([chunk])[0].values for chunk in chunks]
    return embeddings
