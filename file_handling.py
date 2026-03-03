import csv
#read csv
def read_csv(filename):
    data=[]
    with open(filename,'r') as f:
        reader=csv.DictReader(f)
        for row in reader:
            data.append(row)   
    return data

#loading titanic dataset
data=read_csv('titanic.csv')

#printing basic info
print(f"Total passengers: {len(data)}")

#printing survivors
survivors = [row for row in data if row["Survived"] == "1"]
died = [row for row in data if row["Survived"] == "0"]
print(f"Survived: {len(survivors)}")
print(f"Died: {len(died)}")
print(f"Survival rate: {len(survivors)/len(data)*100:.1f}%")

#gender count
males=[row for row in data if row['Sex']=='male']
females=[row for row in data if row['Sex']=='female']
print(f"Male passengers: {len(males)}")
print(f"Female passengers: {len(females)}")

print()
#writing summary to a text file
with open('summary.txt','w') as f:
    f.write(f"Total passengers: {len(data)}\n")
    f.write(f"Survived: {len(survivors)}\n")
    f.write(f"Died: {len(died)}\n")
    f.write(f"Survival rate: {len(survivors)/len(data)*100:.1f}%\n")
print("Summary written to summary.txt")