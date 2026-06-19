# Retail-ETL-Pipeline-using-Python-PostgreSQL
#  Retail ETL Pipeline using Python & PostgreSQL

An end-to-end ETL (Extract, Transform, Load) pipeline built using Python, Pandas, and PostgreSQL to process retail sales data. The pipeline extracts data from multiple CSV files, transforms the data into structured fact and dimension tables, and loads it into a PostgreSQL database for analytical reporting.

---

##  Project Overview

This project demonstrates a complete ETL workflow commonly used in data engineering and data warehousing projects.

The pipeline:

- Extracts retail sales, store, and feature datasets from CSV files
- Cleans and transforms raw data using Pandas
- Creates fact and dimension tables following a Star Schema approach
- Loads transformed data into PostgreSQL
- Uses a modular architecture separating Extract, Transform, and Load layers

---

##  Architecture

```text
CSV Files
(Features, Sales, Stores)
           │
           ▼
 ┌──────────────────┐
 │  Extract Layer   │
 │ Pandas read_csv  │
 └────────┬─────────┘
          │
          ▼
 ┌──────────────────┐
 │ Transform Layer  │
 │ Data Cleaning    │
 │ Date Conversion  │
 │ Feature Creation │
 │ Star Schema      │
 └────────┬─────────┘
          │
          ▼
 ┌──────────────────┐
 │    Load Layer    │
 │ SQLAlchemy       │
 │ PostgreSQL       │
 └────────┬─────────┘
          │
          ▼
 ┌──────────────────┐
 │ PostgreSQL DB    │
 │ fact_sales       │
 │ dim_store        │
 │ dim_date         │
 │ dim_feature      │
 └──────────────────┘
```

---

##  Technologies Used

- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- Psycopg2
- CSV Files

---

##  Project Structure

```text
Retail_ETL_Pipeline/
│
├── main.py
│
├── Data/
│   ├── Features_dataset.csv
│   ├── sales_dataset.csv
│   └── stores_dataset.csv
│
└── etl/
    ├── extract.py
    ├── transform.py
    └── load.py
```

---

##  ETL Workflow

### 1. Extract

Loads data from:

- Features Dataset
- Sales Dataset
- Stores Dataset

Using Pandas:

```python
pd.read_csv()
```

---

### 2. Transform

The transformation layer performs:

#### Data Cleaning

- Converts date columns to datetime format
- Removes unnecessary columns
- Standardizes column names
- Removes duplicate records

#### Feature Engineering

Creates:

- Year
- Month
- Week Number

#### Data Modeling

Creates:

##### Fact Table

- fact_sales

##### Dimension Tables

- dim_store
- dim_date
- dim_feature

This structure follows a simple Star Schema design for analytical reporting.

---

### 3. Load

The load layer:

- Connects to PostgreSQL using SQLAlchemy
- Creates database tables automatically
- Loads transformed data into PostgreSQL



##  Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Retail_ETL_Pipeline.git

cd Retail_ETL_Pipeline
```

### Install Dependencies

```bash
pip install pandas sqlalchemy psycopg2-binary
```

---

##  Configure PostgreSQL

Update database credentials inside:

```python
etl/load.py
```

Example:

```python
db_name = "retail_project"
db_host = "localhost"
db_port = 5432
db_user = "postgres"
db_pass = "your_password"
```

---

##  Run the Pipeline

Execute:

```bash
python main.py
```

Successful execution:

```text
Pipeline Started

Data Extracted Successfully
Data Transformed Successfully
Data Loaded Successfully

Pipeline Completed
```

---

##  Key Features

- Modular ETL Architecture
- Data Extraction from Multiple Sources
- Data Cleaning and Transformation
- Star Schema Design
- Date Feature Engineering
- PostgreSQL Integration
- Reusable Pipeline Components
- Automated Database Loading

---

## Skills Demonstrated

- Data Engineering
- ETL Pipeline Development
- Python Programming
- Pandas
- SQL
- PostgreSQL
- SQLAlchemy
- Data Warehousing
- Data Transformation
- Database Management

---

##  Learning Outcomes

Through this project, I gained practical experience in:

- Designing ETL pipelines
- Data cleaning and preprocessing
- Building fact and dimension tables
- Working with PostgreSQL databases
- Data warehousing concepts
- Writing modular and maintainable Python code


##  Author

**Nadeesha**

Computer Science Undergraduate (AI Specialization)

Passionate about Data Engineering, Data Science, and Analytics.

⭐ If you found this project useful, consider giving it a star.
