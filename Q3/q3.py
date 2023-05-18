import numpy as np
import pandas as pd

def solve():
    arr = np.array([[1000, 25], [280, 120], [900, 30]])
    df = pd.DataFrame(arr, index=['store1', 'store2' ,'store3'], columns=['unit price', 'number'])
    print(df)
    df['total price'] = df['unit price'] * df['number']
    print(df)
    df = df.sort_values(by='total price', ascending=False)
    print(df[:2])
        
def main():
    solve()
if __name__ =="__main__":
    main()