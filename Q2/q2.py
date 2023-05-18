import numpy as np

def solve():
    Docs = np.array([[1, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0], [1, 1, 0, 1, 0, 0]])
    Query = np.array([1, 1, 0, 0, 1, 0])
    QueryNorm = np.linalg.norm(Query)
    for i, doc in enumerate(Docs):
        docNorm = np.linalg.norm(doc)
        res = np.dot(doc, Query) / (docNorm * QueryNorm)
        print(f"doc{i + 1}={res:.2f}")
        
def main():
    solve()
if __name__ =="__main__":
    main()