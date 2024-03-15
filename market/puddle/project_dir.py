import os

def print_project_structure(directory, indent=''):
    """
    Print the directory structure of a given directory recursively.
    """
    # Print the current directory name
    print(indent + os.path.basename(directory) + '/')
    
    # Get the list of all files and directories in the current directory
    items = os.listdir(directory)
    
    # Iterate over each item
    for item in sorted(items):
        # Construct the full path of the item
        item_path = os.path.join(directory, item)
        
        # If the item is a directory, recursively print its structure
        if os.path.isdir(item_path):
            print_project_structure(item_path, indent + '    ')
        # If the item is a file, print its name
        else:
            print(indent + '    ' + item)

# Replace 'path_to_your_project_directory' with the path to your Django project directory
project_directory = 'market'

# Print the project structure starting from the project directory
print_project_structure(project_directory)
