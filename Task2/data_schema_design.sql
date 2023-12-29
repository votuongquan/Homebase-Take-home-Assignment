CREATE TABLE ProductInformation (
    ProductID INT PRIMARY KEY,
    Name VARCHAR(255),
    Description TEXT,
    Price DECIMAL(10, 2),
    QuantityInStock INT,
    ProductType VARCHAR(50)
);

CREATE TABLE OrderManagement (
    OrderID INT PRIMARY KEY,
    OrderDate DATE,
    CustomerName VARCHAR(255),
    CustomerAddress TEXT,
    CustomerPhoneNumber VARCHAR(20),
    OrderStatus VARCHAR(50)
);

CREATE TABLE OrderDetails (
    OrderDetailID INT PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    QuantityPurchased INT,
    FOREIGN KEY (OrderID) REFERENCES OrderManagement(OrderID),
    FOREIGN KEY (ProductID) REFERENCES ProductInformation(ProductID)
);

CREATE TABLE InventoryTracking (
    TransactionID INT PRIMARY KEY,
    ProductID INT,
    TransactionDate DATE,
    QuantityIn INT,
    QuantityOut INT,
    FOREIGN KEY (ProductID) REFERENCES ProductInformation(ProductID)
);