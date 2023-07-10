from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
import os


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020,8,1),
    'retries': 0
}

with DAG('library_dimensional', default_args=default_args, schedule_interval='@once') as dag:
    task_1 = BashOperator(
        task_id='library_dimensional',
        bash_command='cd /dbt && dbt run --models library_dimensional --profiles-dir .',
        env={
            'dbt_user': '{{ var.value.dbt_user }}',
            'dbt_password': '{{ var.value.dbt_password }}',
            **os.environ
        },
        dag=dag
    )