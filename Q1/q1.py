import numpy as np

def solve():
    arr = np.array([[1, 2], [3, 4]])
    vec1 = np.array([1, 2, 3])
    vec2 = np.array([4, 5, 6])
    w, v = np.linalg.eig(arr)
    print("Eigenvalues: ", end="") 
    print(w)
    print("Eigenvectors: ", end="")
    print(v)
    print("Determinant: ", end="")
    print(np.linalg.det(arr))
    print("Cross product: ", end="")
    print(np.cross(vec1, vec2))
    A = np.array([[1, 2, -2], [2, 1, -5], [1, -4, 1]])
    b = np.array([-15, -21, 18])
    print("Solution: ", end="")
    print(np.linalg.solve(A, b))
    
def main():
    solve()
if __name__ =="__main__":
    main()