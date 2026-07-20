import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient

load_dotenv()

client = QdrantClient(
    url=os.environ["QDRANT_URL"],
    api_key=os.environ["QDRANT_API_KEY"],
    timeout=30,
)

def main():
    print("Hello from rag-papeer-project!")
    

    # 1. Can we list collections at all?
    try:
        print("Collections:", client.get_collections())
    except Exception as e:
        print("FAILED to list collections:", e)

    # 2. Try creating a throwaway test collection
    from qdrant_client.models import Distance, VectorParams
    try:
        client.create_collection(
            collection_name="test_permission_check",
            vectors_config=VectorParams(size=768, distance=Distance.COSINE),
        )
        print("Successfully created test collection")
        client.delete_collection("test_permission_check")
        print("Successfully deleted test collection")
    except Exception as e:
        print("FAILED to create/delete:", e)
        


if __name__ == "__main__":
    main()
