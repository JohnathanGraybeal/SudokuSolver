import os
from tkinter.filedialog import askopenfilename


class FileParser:
    def __init__(self):
        """
        On initialization opens a file picker dialog that should be an xml file and matches the correct fille pattern otherwise
        raises an error
        """
        self.acceptable_file = True
        self.file_name = askopenfilename()
        self.filename, self.file_extension = os.path.splitext(self.file_name)
        if self.file_name is not '.xml':
            raise TypeError('Select an xml file to parse ') #TODO make this a dialog 
        file_check = ['ill_formed','solvable','ambiguous','unsolvable','difficult']
        for item in file_check:
            if item not in self.file_name:
                 self.acceptable_file = False
                 raise TypeError(f'Not an acceptable document select a file that contains {[name for name in file_check]}')

        if file_check not in self.file_name:
            self.acceptable_file = False
            raise TypeError(f'Not an acceptable document select a file that contains {file_check}')
    def extract_metadata(self):
        """Extracts the meta data from the xml file in order to create the puzzle"""
        if self.acceptable_file:
            with open (self.file_name,'r') as file:
                

        

file = FileParser()
print(file.file_extension)