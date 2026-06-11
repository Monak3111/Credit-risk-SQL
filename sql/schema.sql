create database credit_risk_db;
use credit_risk_db;
CREATE TABLE customer_profiles (
    customer_id INT PRIMARY KEY,
    gender VARCHAR(10),
    age INT,
    income DECIMAL(15,2),
    occupation VARCHAR(100),
    family_size INT
);

CREATE TABLE loan_applications (
    application_id INT PRIMARY KEY,
    customer_id INT,
    loan_amount DECIMAL(15,2),
    loan_type VARCHAR(50),
    interest_rate DECIMAL(5,2),
    loan_term INT,
    target INT,
    FOREIGN KEY (customer_id)
    REFERENCES customer_profiles(customer_id)
);


create table credit_history (
history_id int primary key auto_increment,
customer_id int,
credit_score int,
total_credit decimal (15,2),
utilized_credit decimal(15,2),
defaults_count int,
    FOREIGN KEY(customer_id)
    REFERENCES customer_profiles(customer_id)
);

CREATE TABLE payment_records (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    payment_date DATE,
    payment_amount DECIMAL(15,2),
    days_late INT,
    
    FOREIGN KEY (customer_id)
        REFERENCES customer_profiles(customer_id)
);

CREATE TABLE customer_features (
    customer_id INT PRIMARY KEY,
    debt_income_ratio FLOAT,
    annuity_income_ratio FLOAT,
    credit_goods_ratio FLOAT,
    default_flag INT
);











