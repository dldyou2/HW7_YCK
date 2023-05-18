import numpy as np
import pandas as pd

def solve():
    csv = pd.read_csv("./gender2.csv", encoding='cp949', index_col=0)
    data = csv[['2022년_계_총인구수', '2022년_남_총인구수', '2022년_여_총인구수']]
    df = pd.DataFrame(data, columns=['2022년_계_총인구수', '2022년_남_총인구수', '2022년_여_총인구수'])
    df.rename(columns={
        '2022년_계_총인구수':'Total',
        '2022년_남_총인구수':'Male',
        '2022년_여_총인구수':'Female',
    }, inplace=True)
    print(df)
        
def main():
    solve()
if __name__ =="__main__":
    main()