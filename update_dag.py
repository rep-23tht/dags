import os

def update_image_tag(dag_file_paths, image_name, new_tag):
    for dag_file_path in dag_file_paths:
        with open(dag_file_path, 'r') as file:
            lines = file.readlines()

        with open(dag_file_path, 'w') as file:
            for line in lines:
                if 'image=' in line:
                    line = line.split('image="')[0] + f'image="{image_name}:{new_tag}",\n'
                file.write(line)

if __name__ == "__main__":
    dag_files = os.getenv('DAG_FILES').split(',')
    image_name = os.getenv('IMAGE_NAME')
    new_tag = os.getenv('NEW_TAG')
    update_image_tag(dag_files, image_name, new_tag)
