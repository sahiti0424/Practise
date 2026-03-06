import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

titanic = pd.read_csv("titanic.csv")
titanic["Age"] = titanic["Age"].fillna(titanic["Age"].mean())

#setting style
sns.set_style("whitegrid")

#Survival Rate by Gender
plt.figure(figsize=(8, 5))
sns.barplot(data=titanic, x="Sex", y="Survived", palette="Set2")
plt.title("Survival Rate by Gender")
plt.xlabel("Gender")
plt.ylabel("Survival Rate")
plt.savefig("insight1_gender_survival.png")
plt.show()