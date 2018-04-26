import os
import subprocess


def get_resize(source_dir, result_dir, converter):

    dir_files = os.listdir(source_dir)
    for file in dir_files:
        process = subprocess.Popen([converter, os.path.join(source_dir, file), "-resize", "200", os.path.join(result_dir, file)])


def main():
    directory = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(os.path.join(directory, "Result"))

    converter = os.path.join(directory, "convert")
    source_dir = os.path.join(directory, 'Source')
    result_dir = os.path.join(directory, "Result")

    get_resize(source_dir, result_dir, converter)
main()
