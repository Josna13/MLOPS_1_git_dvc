import pandas as pd

data = pd.read_csv("EMP.csv")

data["Salary"] = data["Salary"] * 1.10


data.to_csv("EMP.csv", index=False)

print("Salary increased by 10% successfully.\n")


print(data)