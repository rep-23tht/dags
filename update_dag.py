import os
import sys

def update_image_tag(dag_file_path, image_name, new_tag):
    with open(dag_file_path, 'r') as file:
        lines = file.readlines()

    with open(dag_file_path, 'w') as file:
        for line in lines:
            if f'image="{image_name}:' in line:
                line = line.split('image="')[0] + f'image="{image_name}:{new_tag}",\n'
            file.write(line)

if __name__ == "__main__":
    dag_file_path = os.getenv('DAG_FILE_PATH')
    image_name = os.getenv('IMAGE_NAME')
    new_tag = os.getenv('NEW_TAG')
    update_image_tag(dag_file_path, image_name, new_tag)
