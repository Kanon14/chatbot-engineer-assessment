from utils.helper import (
    load_yaml_file,
    convert_yaml_to_documents,
    text_split_from_strings,
    download_hf_embeddings
)
from langchain.vectorstores import FAISS

# Load and process
yaml_data = load_yaml_file("data/zus_products.yaml")
documents = convert_yaml_to_documents(yaml_data)
chunks = text_split_from_strings(documents)
embeddings = download_hf_embeddings()

# Build FAISS vector store
vectorstore = FAISS.from_documents(chunks, embeddings)
vectorstore.save_local("vectorstore/products_faiss")
