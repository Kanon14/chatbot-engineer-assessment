import os
from utils.outlet_store import create_outlet_db
from utils.product_store import create_product_vector_store_pinecone

if __name__ == "__main__":
    # Paths
    outlet_csv = "data/zus_outlets.csv"
    outlet_db = "data/outlets.db"
    product_yaml = "data/zus_trial.yaml"
    pinecone_index = "zus-products"

    # Ensure folders exist
    os.makedirs("data", exist_ok=True)

    # Run: SQLite for outlet DB
    create_outlet_db(outlet_csv, outlet_db)

    # Run: Pinecone vector store for products
    create_product_vector_store_pinecone(product_yaml, index_name=pinecone_index)
