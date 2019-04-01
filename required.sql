# John VanHouten, 206552
# mysql -h csmidn -u m206552 -p m206552
# Password = 'passwordCookie'

# {1}

CREATE TABLE Users
(
UserID int,
UserName varchar(255),
Name varchar(255),
PRIMARY KEY (UserID)
);

# Still have to edit the data type of content
CREATE TABLE MessageBoard
(
MessageID int AUTO_INCREMENT,
UserID int,
mContent ???,
mTime ???,
PRIMARY KEY (SaleID)
FOREIGN KEY (UserID)
        REFERENCES Users(UserID)
        ON DELETE CASCADE
);

CREATE TABLE SALEITEM
(
SaleID int,
ProductID int,
Quantity int,
PRIMARY KEY (SaleID, ProductID)
);
