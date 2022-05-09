# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : test_jenkins.py
# Time       ：2022-05-09 22:59
# Author     ：author name
# version    ：python 3.7-32bit
# Description：
"""

from datetime import datetime, timedelta
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from jenkins import Jenkins


def jenkins_rename(**context):

    stock = context.get("stock")
    print(f"stock===={stock}")
    jen = Jenkins(url=r"http://www.weridolin.cn:8080/",
                  username="werido", password="359066432")
    print(jen.jobs_count())

    try:
        jen.rename_job("devops_test1", "devops_test2")
        return "devops_test2"
    except Exception:
        jen.rename_job("devops_test2", "devops_test1")
        return "devops_test1"


def get_jen_name(*args, **context):
    # 变量传输
    jen_name = context["ti"].xcom_pull(task_ids="jenkins_rename")
    print(f"jen_name==={jen_name}")
    return jen_name


def task1(**context):
    jen_name = context["ti"].xcom_pull(task_ids="get_jen_name")
    print("aaaa")
    return jen_name+"aaaa"


def task2(**context):
    jen_name = context["ti"].xcom_pull(task_ids="get_jen_name")
    print("bbbb")
    return jen_name+"bbbb"


with DAG(
    dag_id='jenkins_rename',
    default_args={
        'depends_on_past': False,
        'email': ['airflow@example.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
    },
    # [END default_args]
    description='A simple jenkins_rename DAG',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
    catchup=False,
    tags=['example'],
) as dag:

    dag.doc_md = """
    This is a documentation placed anywhere
    """  # otherwise, type it like this
    download_task = PythonOperator(
        task_id="jenkins_rename",
        python_callable=jenkins_rename,
        provide_context=True

    )

    get_jen_name_task = PythonOperator(
        task_id="get_jen_name",
        python_callable=get_jen_name,
        provide_context=True

    )

    demo1_task = PythonOperator(
        task_id="task1",
        python_callable=task1,
        provide_context=True

    )

    demo2_task = PythonOperator(
        task_id="task2",
        python_callable=task2,
        provide_context=True

    )
    download_task >> get_jen_name_task >> [demo1_task, demo2_task]

    # [END documentation]


# docker run -d --name mysql  -e MYSQL_ROOT_PASSWORD=123456 -p 3310:3306 mysql
# mysql+mysqldb://root:123456@119.91.151.142:3306/airflow_db
# docker run --name postgres -v dv_pgdata:/var/lib/postgresql/data -e POSTGRES_PASSWORD=123456 -p 5432:5432 -d postgres
# postgresql+psycopg2://postgres:123456@119.91.151.142/airflow_db

# jenkins_rename()
