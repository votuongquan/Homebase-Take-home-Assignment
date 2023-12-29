# Task 1: Python Programming

## Description

Task 1 involves processing data from a CSV file using a Python script.

## File Structure

The workspace contains the following files:

- `data.csv`: This is the data file that the Python script will process.
- `main.py`: This is the main Python script that processes the data.

## Requirements

- Python 3.x
- pandas library (for handling CSV data)

## Instructions

1. Ensure that Python 3.x is installed on your system.
2. Install the pandas library using pip: `pip install pandas`
3. Run the `main.py` script: `python main.py`

The script will read the data from `data.csv`, process it, and output the results.

# Task 2 Data Structures: E-commerce Inventory Schema

## Description

Task 2 involves designing a database schema for an e-commerce inventory system. The schema is defined in SQL and includes tables for product information, order management, order details, and inventory tracking.

## File Structure

The workspace contains the following files:

- `data_schema_design.sql`: This file contains the SQL commands to create the database schema.
- `E_commerce_inventory.bak`: This is a backup file for the database.

## Requirements

- SQL Server or any SQL database system
- SQL client software (like SQL Server Management Studio, DBeaver, etc.)

## Instructions

1. Open your SQL client software and connect to your SQL Server.
2. Open the `data_schema_design.sql` file in your SQL client software.
3. Execute the SQL commands in the `data_schema_design.sql` file to create the database schema.

The schema includes the following tables:

- `ProductInformation`: Contains information about the products.
- `OrderManagement`: Contains information about the orders.
- `OrderDetails`: Contains details about the orders, such as the products in each order.
- `InventoryTracking`: Tracks the inventory transactions for each product.

# Task 3:  Web Scraping - Real Estate Data from Batdongsan.com

## Description
Task 3 involves web scraping data from a real estate website and processing it using Python. The data is then stored in an Excel file and a SQLite database.

## File Structure 
The workspace contains the following files:
  - `real_estate_cache.sqlite`: This is the SQLite database where the scraped data is cached.
  - `main.py`: This is the main Python script that scrapes the data and processes it
  - `databds.xlsx`: This is the Excel file where the scraped data is stored

## Requirements
  - Python 3.x
  - numpy library (for handling data)
  - pandas library (for handling data)
  - BeautifulSoup library (for web scraping)
  - requests library (for making HTTP requests)
  - requests_cache library (for caching HTTP requests)
  - selenium library (for automating web browser interaction)

## File Instructions

Ensure that Python 3.x is installed on your system.
Install the required Python libraries using pip:
  - `pip install pandas`
  - `pip install beautifulsoup4`
  - `pip install requests`
  - `pip install requests-cache`
  - `pip install selenium`

Run the main.py script: python main.py

The script will scrape data from the real estate website, process it, and store it in data.xlsx and real_estate_cache.sqlite.

# Task 4:Nested Set Model Implementation

## Description
Task 4 involves Python programming. More details are needed to provide a complete description.

## File Structure
The workspace contains the following file:
  - `main.py`: This is the main script where the Node and NestedSetModel classes are defined and used.

### Classes
  - `Node`: This class represents a node in the tree. Each node has an id, children, left, and right attributes. The id is a unique identifier for the node, children is a list of child nodes, and left and right are used for the Nested Set Model representation.

  - `NestedSetModel`: This class is used to convert a tree of Node objects into a Nested Set Model. It also provides methods to retrieve parent-child relationships and print the Nested Set Model.

## Instructions 
To use this script, you need to create a tree of Node objects and pass the root node to the NestedSetModel class.
I gave an crystal clear example in the script


# Task 5: Database and SQL - Stored Procedure Creation

## Description

Task 5 involves creating a stored procedure in SQL to manage blog posts. The stored procedure includes functionalities for adding new posts, retrieving post details, updating posts, and deleting posts. It also manages user interactions like adding comments to posts and deleting comments.

## File Structure

The workspace contains the following file:

- `stored_procedure.sql`: This file contains the SQL commands to create the stored procedure.

## Requirements

- SQL Server or any SQL database system
- SQL client software (like SQL Server Management Studio, DBeaver, etc.)

## Instructions

1. Open your SQL client software and connect to your SQL Server.
2. Open the `stored_procedure.sql` file in your SQL client software.
3. Execute the SQL commands in the `stored_procedure.sql` file to create the stored procedure.

The stored procedure `ManageBlogPost` performs the following operations:

- `add_post`: Adds a new post to the `BlogPosts` table.
- `get_post`: Retrieves details of a post from the `BlogPosts` table.
- `update_post`: Updates a post in the `BlogPosts` table.
- `delete_post`: Deletes a post from the `BlogPosts` table.
- `add_comment`: Adds a comment to the `Comments` table.
- `delete_comment`: Deletes a comment from the `Comments` table.
- `fetch_post_data`: Fetch all related data to the post

