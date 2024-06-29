"""
Query to the GitHub REST API for various endpoint
events
"""
from airflow import DAG
from airflow.models import BaseOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.decorators import apply_defaults
from airflow.models import Variable
from datetime import datetime, timedelta, timezone
from airflow.utils.trigger_rule import TriggerRule
from airflow.operators.bash_operator import (
    BashOperator
)

from airflow.operators.python import (
    BranchPythonOperator
)
from airflow.operators.dummy import (
    DummyOperator
)
from airflow.operators.trigger_dagrun import (
    TriggerDagRunOperator
)
from utils.process_gh_repo_requests import generate_concurrent_requests

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
    "catchup": False,
    "max_active_runs": 1
}
dag = DAG(
    'gh_rest_issues_api',
    default_args=default_args,
    description="Task queries GitHub REST API endpoint - issues",
    schedule_interval="@hourly",
    start_date=datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0),
    tags=["dev"]
)


run_date = "{{ dag_run.conf['execution_date'] if dag_run and dag_run.conf and 'execution_date' in dag_run.conf else ds_nodash }}"


fetch_issues = PythonOperator(
    task_id="fetch_issues",
    python_callable=generate_concurrent_requests,
    op_args=["issues"],
    dag=dag
)

trigger_spark_issues_transfer = TriggerDagRunOperator(
    task_id="trigger_spark_issues_transfer",
    trigger_dag_id="publish_pg_raw_issues_to_iceberg",
    dag=dag
)

fetch_issues >> trigger_spark_issues_transfer