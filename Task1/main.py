# import libraries
import pandas as pd

def calculate_average_age(file_path):
    try:
        # Read the CSV file with pandas
        df = pd.read_csv(file_path)

        # Check if the required columns are present
        required_columns = ['Name', 'Age']
        if not set(required_columns).issubset(df.columns):
            raise ValueError(f"CSV file must have columns: {', '.join(required_columns)}.")

        # Check for null values in the 'Age' column
        if df['Age'].isnull().any():
            raise ValueError("Null values found in the 'Age' column. Please handle or clean the data.")

        # Check for valid numerical values in the 'Age' column
        if not pd.to_numeric(df['Age'], errors='coerce').notna().all():
            raise ValueError("Invalid values found in the 'Age' column.")

        # Calculate the average age
        average_age = df['Age'].mean()
        return average_age

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except pd.errors.EmptyDataError:
        print("Error: Empty CSV file.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

result = calculate_average_age('Task1/data.csv')
print(f"Average age: {result}")
