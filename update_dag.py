import os

def update_image_tag(dag_file_path, new_tag):
    with open(dag_file_path, 'r') as file:
        lines = file.readlines()

    with open(dag_file_path, 'w') as file:
        for line in lines:
            if 'image=' in line:
                line = line.split('image="')[0] + f'image="busybox:{new_tag}",\n'
            file.write(line)

if __name__ == "__main__":
    dag_file_path = os.getenv('DAG_FILE_PATH')
    new_tag = os.getenv('NEW_TAG')
    update_image_tag(dag_file_path, new_tag)
