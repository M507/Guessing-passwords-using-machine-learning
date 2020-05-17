import subprocess
import os.path


"""
Stylish input()
"""
def s_input(string):
    return input(string+">").strip("\n")


"""
Execute command locally
"""
def execute_command(command):
    if len(command) > 0:
        print(command)
        proc = subprocess.Popen(command.split(" "), stdout=subprocess.PIPE, cwd="/tmp")
        return proc

"""
Get all subdirectories of a directory.
"""
def getSubs(dirname):
    dirs = [d for d in os.listdir(dirname) if os.path.isdir(os.path.join(dirname, d))]
    # subdirectories = [dirname + "/" + subDirName for subDirName in subdirectories]
    subdirectories = []
    for dir in dirs:
        subdirectories.append(dirname + '/' + dir)
    return subdirectories


"""
Rocket science
"""
def answer(string):
    a = input(string)
    if a == "Y" or a == 'y' or a == 'Yes' or a == 'yes':
        return True
    else:
        return False
