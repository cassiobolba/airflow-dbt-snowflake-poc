from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def my_callable(*args, **kwargs):
    print("Hello from PythonOperator")

with DAG('my_dag', start_date=datetime(2021, 1, 1), schedule_interval='@once' ) as dag:
    python_task = PythonOperator(
        task_id='my_python_task',
        python_callable=my_callable
    )