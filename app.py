import pandas as pd
from pymongo import MongoClient
import warnings

from load_csv_to_mongodb import load_csv_to_mongodb

# Suppress warnings
warnings.filterwarnings("ignore")

# Step 3: Execute MongoDB query and retrieve data
def execute_mongodb_query(query, db_name, collection_name, mongo_uri="mongodb://localhost:27017/"):
    """
    Execute MongoDB query and retrieve data.
    """
    # Connect to MongoDB
    client = MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]
    
    # Execute query
    try:
        result = list(eval(query))  # Convert string query to executable code
        return result
    except Exception as e:
        print(f"Error executing query: {e}")
        return None

# Step 4: Display or save retrieved data
def display_or_save_data(data, save_file=None):
    """
    Display or save retrieved data.
    """
    if data:
        df = pd.DataFrame(data)
        if save_file:
            df.to_csv(save_file, index=False)
            print(f"Data saved to {save_file}.")
        else:
            print(df)
    else:
        print("No data retrieved.")

# Main function
def main():
    # Step 1: Load CSV data into MongoDB
    csv_file = "sample_data.csv"  # Replace with your CSV file
    db_name = "product_db"
    collection_name = "products"
    load_csv_to_mongodb(csv_file, db_name, collection_name)
    
    # Step 2: User interaction
    user_input = input("Enter your query (e.g., 'find products with price greater than 50'): ")
    column_name = input("Enter the column name (e.g., 'Price'): ")
    
    # Generate MongoDB query
    query = generate_mongodb_query(user_input, column_name)
    print(f"Generated Query: {query}")
    
    # Step 3: Execute query and retrieve data
    data = execute_mongodb_query(query, db_name, collection_name)
    
    # Step 4: Display or save data
    save_option = input("Do you want to save the data? (yes/no): ").lower()
    if save_option == "yes":
        save_file = input("Enter the file name to save (e.g., test_case1.csv): ")
        display_or_save_data(data, save_file)
    else:
        display_or_save_data(data)

if __name__ == "__main__":
    main()