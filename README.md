# nxtgen-assessment - Building a Data Pipeline from Scratch

## Overview
This project involves data extraction, transformation, and loading (ETL) tasks to process data from two sources and transform it into a structured format for analysis and reporting purposes.

## Data Extraction:
Data is fetched from two sources.
#### Sources:

    CSV File: The project extracts data from a CSV file containing customers data.
    REST Endpoint: Additionally, data is fetched from a REST endpoint to enrich the dataset with products information. 
    Data is cleaned and stored in a PostgreSQL database hosted locally using PgAdmin. The database is named AssessmentDB.

## Data Transformation:
Data is transformation using dbt (Data Build Tool), which helps in creating data models, staging, and marts.
#### Transformation Process:
    Data Models: Data models are created to define the structure of the transformed data.
    Staging and Marts: Staging tables are used to temporarily store the extracted data in views before transformation, while mart tables contain the transformed data ready for analysis.
    Execution: Transformation tasks are executed using dbt run and debugged using dbt debug commands.

## Data Loading:
    Utilized Astronomer Cosmos to build and deploy Apache Airflow within Docker containers.

 ## Instructions for running with docker:
 **Assuming docker is installed on the system, if not you can install [here](https://docs.docker.com/desktop/install/mac-install/)**  
 Build Docker Image:  
 `docker build -t <image-name> .`  
 Run Docker Container:    
 `docker run -p 9900:9900 <image-name>`     
 Using Docker Compose for Postgres Connection:    
 `docker-compose up`    
Access the Airflow UI by navigating to `localhost:9900`     
Credentials for Airflow:     
user: admin     
pswd: admin      
