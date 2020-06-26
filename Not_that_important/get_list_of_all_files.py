import os
def get_list(dir_name):
    list_of_file=os.listdir(dir_name)
    all_files=list()

    for entry in list_of_file:
        full_path=os.path.join(dir_name,entry)
        if os.path.isdir(full_path):
            all_files=all_files+get_list(full_path)
        else:
            all_files.append(full_path)

    return all_files

dir_name=r"../.."
list_of_files=get_list(dir_name)
print("\n".join(list_of_files))
