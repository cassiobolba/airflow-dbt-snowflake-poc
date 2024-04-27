from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def my_callable(*args, **kwargs):
    import pandas as pd

    # File path to the CSV file
    file_path = '/data_src/account-statement_2024-04-01_2024-04-30_pt_62a9ca.csv'

    # Read the CSV file
    df = pd.read_csv(file_path)

    # Display the first 5 rows of the DataFrame
    print(df.head())

with DAG('my_dag', start_date=datetime(2021, 1, 1), schedule_interval='@once' ) as dag:
    python_task = PythonOperator(
        task_id='my_python_task',
        python_callable=my_callable
    )