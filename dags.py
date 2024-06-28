from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from airflow.utils.dates import days_ago
import yaml

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'retries': 1,
}

dag = DAG(
    'eks_job_dag',
    default_args=default_args,
    description='A simple DAG to run a job on EKS',
    schedule_interval='@daily',
)

# Define the job configuration as a multi-line string
job_config_str = """
apiVersion: batch/v1
kind: Job
metadata:
  name: hello-world-job1
spec:
  template:
    spec:
      containers:
      - name: hello-world
        image: busybox
        command: ["echo", "Hello, world!"]
      restartPolicy: Never
"""

# Parse the job configuration from the multi-line string
job_config = yaml.safe_load(job_config_str)

# Define the KubernetesPodOperator
run_eks_job = KubernetesPodOperator(
    namespace='airflow',
    image="yyut.{image_name}:{new_tag}",  # Replace with the actual image if different
    cmds=job_config['spec']['template']['spec']['containers'][0]['command'],
    name=job_config['metadata']['name'],
    task_id="hello_world_job",
    get_logs=True,
    is_delete_operator_pod=False,
    dag=dag,
)

run_eks_job
