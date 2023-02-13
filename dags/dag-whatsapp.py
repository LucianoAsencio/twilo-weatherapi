from datetime import timedelta, datetime

from airflow import DAG

from airflow.operators.python import PythonOperator

# Un diccionario que despues será pasado como parámetro en la creación del DAG

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def envio_mensaje():
    with open('../app/script.py', 'r') as f:
        exec(f.read())

with DAG(
    'Envío mensaje',
    default_args = default_args,
    description = 'Envía un mensaje por whatsapp con la info del clima de Mar del Plata',
    schedule_interval = timedelta(days=1),
    start_date = datetime(2023, 2, 13, 15, 50),
    tags = ['mensaje','Twilo','WeatherAPI'],
) as dag:
    envio_mensaje_task = PythonOperator(task_id="envio_mensaje", python_callable=envio_mensaje)


    envio_mensaje_task