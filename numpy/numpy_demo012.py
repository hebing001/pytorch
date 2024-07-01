import numpy as np
t1 = np.arange(12).reshape(3,4).astype(float)
print(t1)
print("-------------------------------")
t1[1,2:] = np.nan
t1[2,1:] = np.nan
print(t1)
print(t1!=t1)
for i in range(t1.shape[1]):
    print("分隔符")
    temp_col = t1[:,i]
    print(temp_col)
    nan_num = np.count_nonzero(temp_col!=temp_col)
    if nan_num != 0:
        # print(temp_col[temp_col==temp_col] )
        # print(np.mean(temp_col[temp_col==temp_col]))
        # temp_col[temp_col!=temp_col] = np.mean(temp_col[temp_col==temp_col])
        print(np.isnan(temp_col))
        print(temp_col[np.isnan(temp_col)])
        temp_col[np.isnan(temp_col)] = np.mean(temp_col[temp_col==temp_col])
print(t1)