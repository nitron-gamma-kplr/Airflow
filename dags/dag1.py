from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta


def greetings(message):
    print("#############################################")
    print(f"  {message}, AIRFLOW!")
    print((datetime.now() + timedelta(hours=2)).strftime("%y-%m-%d %H:%M:%S"))
    print("#############################################")


# Define the DAG
dag = DAG(
    "hello_world_dag",
    description="A simple DAG that prints Hello, World!",
    start_date=datetime(2023, 5, 1),
    schedule_interval="@once",
)

# Define the task
hello_task = PythonOperator(task_id="hello_task", python_callable=greetings, dag=dag, op_kwargs={'message': 'hello'})

# Define the task
hello_task2 = PythonOperator(
    task_id="hello_task2", python_callable=greetings, dag=dag
)

# Define the task
goodby_task = PythonOperator(task_id="goodby_task", python_callable=greetings, dag=dag, op_kwargs={'message': 'goodby'})

# Set the task dependencies
[hello_task, hello_task2] >> goodby_task
