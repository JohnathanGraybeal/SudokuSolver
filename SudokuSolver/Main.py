from FileParser import FileParser
import sys

file = FileParser()
file.extract_metadata()

print(file.file_name)

