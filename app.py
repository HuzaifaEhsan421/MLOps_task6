import pandas as pd

# Load the data from CSV
data = pd.read_csv('data.csv')

# Define a simple function to categorize age groups
def categorize_age(age):
    if age < 30:
        return 'Youth'
    else:
        return 'Adult'

# Apply the function to the 'Age' column
data['AgeGroup'] = data['Age'].apply(categorize_age)

# Save the processed data to a new CSV file
data.to_csv('new_data.csv', index=False)
