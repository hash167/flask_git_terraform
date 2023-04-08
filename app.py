import os
import threading
from flask import Flask, request, jsonify, Response
from python_terraform import Terraform

app = Flask(__name__)
terraform_lock = threading.Lock()

def run_terraform():
    data = request.get_json()
    name = data.get('name')
    branch = data.get('branch')

    if not name or not branch:
        yield jsonify({"error": "Missing 'name' or 'branch' parameters."})

    yield "Waiting for the lock...\n"
    with terraform_lock:
        try:
            # Clone the repository
            os.system(f'git clone -b {branch} https://github.com/hash167/flask_git_terraform data')

            # Change directory to the specified folder
            os.chdir(os.path.join(os.getcwd(), 'data', name))

            # Initialize and configure Terraform
            tf = Terraform(working_dir=os.getcwd(), stdout_callback=lambda x: print(x), stderr_callback=lambda x: print(x))

            # Initialize Terraform
            return_code, stdout, stderr = tf.init()
            yield stdout
            yield stderr

            # Apply Terraform configuration
            return_code, stdout, stderr = tf.apply(auto_approve=True)
            yield stdout
            yield stderr

        except Exception as e:
            yield jsonify({"error": str(e)})

@app.route('/deploy', methods=['POST'])
def deploy():
    return Response(run_terraform(), content_type='text/plain')

if __name__ == '__main__':
    app.run(debug=True)
