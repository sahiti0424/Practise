import pandas as pd

titanic = pd.read_csv("titanic.csv")
titanic["Age"] = titanic["Age"].fillna(titanic["Age"].mean())


# 1. Print first 10 rows
print(titanic.head(10))

# 2. Print shape
print(titanic.shape)

# 3. Print all column names
print(titanic.columns.tolist())

# 4. Print total missing values
print( titanic.isnull().sum())

# 5. Select only Name and Age columns
print(titanic[["Name", "Age"]].head())

# 6. How many passengers were in class 1
print(len(titanic[titanic["Pclass"] == 1]))

# 7. How many passengers survived
print(titanic["Survived"].sum())

# 8. Average fare paid
print(titanic["Fare"].mean())

# 9. Oldest passenger
print(titanic["Age"].max())

# 10. Youngest passenger
print( titanic["Age"].min())

# 11. How many females survived
female_survivors = titanic[(titanic["Sex"] == "female") & (titanic["Survived"] == 1)]
print(len(female_survivors))

# 12. Survival rate of males vs females
print(titanic.groupby("Sex")["Survived"].mean())

# 13. Average age of survivors vs non survivors
print( titanic.groupby("Survived")["Age"].mean())

# 14. Count passengers by class
print(titanic["Pclass"].value_counts())

# 15. Add column FareCategory — cheap if Fare < 50, expensive if >= 50
titanic["FareCategory"] = titanic["Fare"].apply(
    lambda x: "Cheap" if x < 50 else "Expensive"
)
print(titanic["FareCategory"].value_counts())

# 16. Sort by Fare descending — who paid most?
print(titanic.sort_values("Fare", ascending=False)[["Name", "Fare"]].head())

# 17. How many passengers embarked from each port
print(titanic["Embarked"].value_counts())

# 18. Average fare by passenger class
print(titanic.groupby("Pclass")["Fare"].mean())

# 19. Drop Name, Ticket, Cabin columns
titanic_clean = titanic.drop(columns=["Name", "Ticket", "Cabin"], errors="ignore")
print(titanic_clean.columns.tolist())
