import os
from tkinter.filedialog import askopenfilename
from bs4 import BeautifulSoup as bs


class FileParser:
    def __init__(self):
        """
        On initialization opens a file picker dialog that should be an xml file and matches the correct fille pattern otherwise
        raises an error
        """
        self.acceptable_file = True
        self.file_name = askopenfilename()
        self.filename, self.file_extension = os.path.splitext(self.file_name)
        if self.file_extension != '.xml':
            # TODO make this a dialog
            raise TypeError('Select an xml file to parse ')

    def extract_metadata(self):
        """Extracts the meta data from the xml file in order to create the puzzle using BeautifulSoup"""
        if self.acceptable_file:
            with open(self.file_name, 'r') as file:
                content = file.readlines() # extract rows per box 
                content = "".join(content)
                bs_content = bs(content, 'xml')
                self.rows_per_box = int(bs_content.find("rows_per_box").get_text())

                self.cols_per_box = int(bs_content.find("cols_per_box").get_text())

                self.value_range = range(1,(self.rows_per_box * self.cols_per_box) +1) 

                #TODO extract start state into a dictionary 

                self.start_state = dict(bs_content.find("start_state").get_text())

                self.well_formed = bool(bs_content.find("well_formed").get_text())

                self.solvable = bool(bs_content.find("solvable").get_text())

                self.unique_solution = bool(bs_content.find("unique_solution").get_text())

                self.pigeonhole = bool(bs_content.find("pigeonhole_decidable").get_text())

                print(self.start_state)

               


                


file = FileParser()
file.extract_metadata()
