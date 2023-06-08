import os, json

def clear_outputs(notebook_name_and_path):
    original_file = open(notebook_name_and_path, 'r')
    notebook_contents = json.load(original_file)
    original_file.close()
    for cell in notebook_contents['cells']:
        if cell['cell_type']=='code':
            cell['outputs'] = []
            cell['execution_count'] = None
    with open(notebook_name_and_path, 'w') as notebook_file:
        json.dump(notebook_contents, notebook_file)

for root, dirs, files in os.walk("."):
    for filename in files:
        if filename.endswith('.ipynb'):
            notebook_name = filename[:-6]
            notebook_name_and_path = os.path.join(root, filename)
            notebook_file = open(notebook_name_and_path)
            notebook_contents = json.load(notebook_file)
            for cell in notebook_contents['cells']:
                if cell['cell_type']=='code':
                    outputs = cell['outputs']
                    if len(outputs) > 0:
                        notebook_file.close()