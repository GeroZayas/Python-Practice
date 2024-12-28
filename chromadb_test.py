from icecream import ic 
import chromadb

# chroma_client = chromadb.Client()
chroma_client = chromadb.PersistentClient(path="./chroma_persistence")

# collection = chroma_client.create_collection("my_collection")
collection = chroma_client.get_collection("my_collection")

collection.add(
    documents=[
        "Python is a versatile and high-level programming language known for its readability and simplicity. It supports multiple programming paradigms, including object-oriented, functional, and procedural approaches, making it suitable for various applications such as web development, data science, machine learning, automation, and scientific computing. Python emphasizes clean code and offers features like dynamic typing and extensive libraries, which facilitate quick development and debugging.",
        "Programming involves creating instructions that guide computers to perform specific tasks. It encompasses core concepts such as variables for data storage, control structures for managing program flow, and logical constructs like conditional statements and loops. Programmers leverage these building blocks to solve complex problems and develop applications, transforming ideas into functional software systems across various technological domains.",
    ],
    ids=[
        "id1",
        "id2",
    ]
)

results = collection.query(
    query_texts=[
        "apps",
    ],
    n_results=1,
)


ic(results)
