import os
from datetime import datetime

from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import PostgresUserPasswordProfileMapping


# Define your PostgreSQL profile mapping
postgres_profile_mapping = PostgresUserPasswordProfileMapping(
    user='postgres',
    password='admin',
    host='localhost',
    port='1234',  # Typically 5432 for PostgreSQL
    database='AssessmentDB'
)
# Define your project configuration

project_config = ProjectConfig(
    project_dir='./../../data_pipeline_assessment/',  # The directory where your dbt project is located
    profiles_dir='./../../data_pipeline_assessment/dbt-dag/.dbt/',  # The directory where your dbt profile is defined
    project_name='data_pipeline_assessment'
)
# Define your profile configuration
profile_config = ProfileConfig(
    profile_name='postgres',  # Must match the name used in your dbt profile
    profile_mapping=postgres_profile_mapping
)
# Define your execution configuration
execution_config = ExecutionConfig(
    run_timestamp=datetime.utcnow(),  # Use UTC timestamp for consistent scheduling
    environment='staging'  # Typically 'dev', 'staging', or 'production'
)
# Initialize the DbtDag with your configurations
dbt_dag = DbtDag(
    project_config=project_config,
    profile_config=profile_config,
    execution_config=execution_config,
    operator_args={"install_deps": True},  # This will install dependencies before running dbt commands
    schedule_interval="@daily",  # DAG will run daily
    start_date=datetime(2024, 4, 25),  # Starting date for the DAG to run
    catchup=False,  # Whether or not to perform catch-up runs
    dag_id="dbt_postgres_dag"  # Unique identifier for the DAG
)