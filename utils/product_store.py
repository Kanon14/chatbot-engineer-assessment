import os
import yaml
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec

# Load .env for Pinecone API
load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

def load_yaml(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def convert_to_text_chunks(products):
    docs = []
    for item in products:
        text = f"Product Name: {item.get('product')}\n"
        text += f"Category: {item.get('category')}\n"
        text += f"Price: {item.get('price')}\n"
        text += f"Discount: {item.get('discount')}\n"
        text += f"Status: {item.get('status')}\n"
        text += f"Colors: {item.get('colors')}\n"
        text += f"Product Specs: {item.get('prod_specs')}\n"
        text += f"Features: {item.get('features')}\n"
        text += f"Warranty: {item.get('warranty')}\n"
        text += f"URL: {item.get('url')}\n"
        docs.append(text.strip())
    splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=20)
    return splitter.create_documents(docs)

def create_product_vector_store_pinecone(yaml_path, index_name): 
    product_data = load_yaml(yaml_path)
    text_chunks = convert_to_text_chunks(product_data)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    pc = Pinecone(api_key=PINECONE_API_KEY)

    if index_name not in [i.name for i in pc.list_indexes()]:
        pc.create_index(
            name=index_name,
            dimension=384,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1")
        )

    vectorstore = PineconeVectorStore.from_documents(
        documents=text_chunks,
        embedding=embeddings,
        index_name=index_name,
    )
    print(f"[✓] Pinecone vector store created under index: {index_name}")
