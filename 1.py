import pandas as pd

Student = {
    "Roll": [
        101,102,103,104,105,106,107,
        108,109,110,111,112,113,114,
        115,116,117,118,119,120,121,
        122,123,124,125,126,127,128
    ],

    "Name": [
        "Amit","Rohit","Ramesh","Suresh","Mahesh",
        "Rahul","Priya","Sneha","Neha","Akash",
        "Pooja","Karan","Anjali","Vikas",
        "Raj","Simran","Arjun","Kavya","Manish",
        "Isha","Aditya",
        "Varun","Meera","Nikhil","Riya",
        "Sanjay","Deepa","Harsh"
    ],

    "Marks": [
        90,80,70,60,50,85,95,
        88,76,91,84,79,87,73,
        82,94,77,89,68,86,92,
        75,93,81,78,69,88,91
    ]
}

# Create DataFrame
df = pd.DataFrame(Student)

# Save CSV
df.to_csv("Student.csv", index=False)

print("CSV file created successfully.\n")

# Read CSV
data = pd.read_csv("Student.csv")

# Print CSV contents
print(data)