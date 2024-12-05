import pandas as pd

# Load the uploaded CSV file to examine its contents
file_path = 'gym_members_exercise_tracking_synthetic_data.csv'
data = pd.read_csv(file_path)

data.head()

# Strip leading and trailing whitespaces, tabs, and newline characters from the Workout_Type column
data['Workout_Type'] = data['Workout_Type'].str.strip().replace(r'\\[n|t]', '', regex=True)

# Remove rows where Workout_Type is null or blank after cleaning
data = data[data['Workout_Type'].notna()]
data = data[data['Workout_Type'] != '']
data.reset_index(drop=True, inplace=True)

# Check the unique values in the cleaned Workout_Type column
print(data['Workout_Type'].unique())

# Save the cleaned data to a new CSV file
cleaned_file_path = 'cleaned_gym_members_data.csv'
data.to_csv(cleaned_file_path, index=False)
