import numpy as np
def create_matrix(mc):
    print("\n ARRAY "+str(mc)+" Elements:")
    array_1=map(int,input().split())
    array_1=np.array(list(array_1))
    print("\n ARRAY "+str(mc)+", ROW COLUMN:")
    row,column=map(int,input().split())
    if(len(array_1)!=(row*column)):
        print("\n Row and column size not match with the total size!!Retry")
        return create_matrix(mc)
    array_1=array_1.reshape(row,column)
    print("\n ARRAY "+str(mc))
    print(array_1)
    print("\n Inverse:")
    return array_1
print(np.linalg.inv(create_matrix(1)))
