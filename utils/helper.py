from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
import yaml


# Load product docs from a YAML file
def load_yaml_file(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
    return data


# Convert product entries into readable strings for vector embedding
def convert_yaml_to_documents(yaml_data: list) -> list:
    documents = []
    for entry in yaml_data:
        text = f"Product Name: {entry.get('product', '')}\n"
        text += f"Category: {entry.get('category', '')}\n"
        text += f"Price: {entry.get('price', '')}\n"
        text += f"Status: {entry.get('status', '')}\n"
        text += f"Features: {', '.join(entry.get('features', []))}\n"
        if 'colors' in entry:
            text += f"Colors: {', '.join(entry['colors'])}\n"
        if 'product_specs' in entry:
            specs = ', '.join([f"{k}: {v}" for k, v in entry['product_specs'].items()])
            text += f"Specifications: {specs}\n"
        if 'warranty' in entry:
            text += f"Warranty: {entry['warranty']}\n"
        if 'url' in entry:
            text += f"URL: {entry['url']}\n"
        documents.append(text.strip())
    return documents


# Split the YAML texts into manageable chunks (if needed)
def text_split_from_strings(texts: list):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    return text_splitter.create_documents(texts)


# Download the embedding model from HuggingFace
def download_hf_embeddings():
    return HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
