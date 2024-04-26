# Use the official Airflow image as a parent image
FROM quay.io/astronomer/astro-runtime:11.1.0

WORKDIR "/usr/local/airflow"
COPY requirements.txt .
COPY dags-airflow ./dags
COPY data_pipeline_assessment /usr/local/airflow/data_pipeline_assessment
RUN python -m venv dbt_venv && source dbt_venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt && deactivate

#RUN export AIRFLOW_HOME=~/airflow
# install from pypi using pippip install apache-airflow
# initialize the database
RUN airflow db init

RUN airflow users  create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin

EXPOSE 9900

ENTRYPOINT ["airflow", "webserver", "--port", "9900"]