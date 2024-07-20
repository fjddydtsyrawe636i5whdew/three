import os
import shutil
import random
import time
from git import Repo

# List of some random GitHub repositories
repositories = [
    "https://github.com/psf/requests.git",
    "https://github.com/django/django.git",
    "https://github.com/pallets/flask.git",
    "https://github.com/tensorflow/tensorflow.git",
    "https://github.com/numpy/numpy.git"
]

# Interval in seconds
clone_interval = 60  # 60 seconds for cloning
delete_interval = 60  # 60 seconds for deleting
file_create_interval = 10  # 10 seconds for creating files
file_delete_interval = 5  # 5 seconds for deleting files
end_time = time.time() + 5 * 60 * 60  # 5 hours from now

def clone_and_delete_repo():
    while time.time() < end_time:
        # Choose a random repository
        repo_url = random.choice(repositories)
        repo_name = repo_url.split('/')[-1].replace('.git', '')

        # Clone the repository
        Repo.clone_from(repo_url, repo_name)
        print(f"Cloned repository {repo_name}")

        # Wait for the clone interval
        time.sleep(clone_interval)

        # Delete the cloned repository
        shutil.rmtree(repo_name)
        print(f"Deleted repository {repo_name}")

        # Wait for the delete interval before the next iteration
        time.sleep(delete_interval)

def create_and_delete_files():
    for i in range(1, 101):
        # Create a text file
        file_name = f"{i}.txt"
        with open(file_name, 'w') as f:
            f.write(f"This is file {file_name}")
        print(f"Created file {file_name}")

        # Wait for the file delete interval
        time.sleep(file_delete_interval)

        # Delete the text file
        os.remove(file_name)
        print(f"Deleted file {file_name}")

        # Wait for the file create interval before the next iteration
        time.sleep(file_create_interval - file_delete_interval)

# Run both functions concurrently
import threading
repo_thread = threading.Thread(target=clone_and_delete_repo)
file_thread = threading.Thread(target=create_and_delete_files)

repo_thread.start()
file_thread.start()

repo_thread.join()
file_thread.join()
