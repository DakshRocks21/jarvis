import os


# Find all __pycache__ directories and delete them
def clean_pycache():
    # print("Deleting the following dirs: ")
    for root, dirs, files in os.walk(os.getcwd()):
        for d in dirs:
            if d == "__pycache__":
                # print("-", os.path.join(root, d))
                os.system(f"rm -rf {os.path.join(root, d)}")


clean_pycache()