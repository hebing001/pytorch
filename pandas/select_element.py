import pandas as pd
import numpy as np

data = np.arange(-12, 12).reshape((6, 4))
print("numpy:\n", data)
df = pd.DataFrame(
    data,
    index=list("abcdef"),
    columns=list("ABCD"))
print("\ndf:\n", df)

# print("numpy:\n", data[2:3, 1:3])
# print("\ndf:\n", df.iloc[2:3, 1:3])
#
#
# print("numpy:\n", data[[3,1], :])
# print("\ndf:\n", df.loc[["d", "b"], :])
#
# row_labels = df.index[2:4]
# print("row_labels:\n", row_labels)
# print("\ndf:\n", df.loc[row_labels, ["A", "C"]])


print(df["A"]<3)


var = ~(df.iloc[0] < -10)
print(var)
print(type(var))
print(var.values)
print(type(var.values))

print(df.iloc[:, ~((df.iloc[0] < -10)).values])
print(df.loc[:, ~((df.iloc[0] < -10))])