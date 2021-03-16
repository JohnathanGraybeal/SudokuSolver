import os
from tkinter.filedialog import askopenfilename
from bs4 import BeautifulSoup as bs
from soup2dict import convert


class FileParser:
    def __init__(self,file):
        """
        On initialization opens a file picker dialog that should be an xml file and matches the correct fille pattern otherwise
        raises an error
        """
        try:
            if os.path.isfile(file):
                self.acceptable_file = True
                self.filename, self.file_extension = os.path.splitext(file)
        except FileNotFoundError as ex:
            print(ex)
            #TODO if exception raised launch the gui then the filepicker 
            self.file_name = askopenfilename()
            if self.file_extension != '.xml':
                raise TypeError('Select an xml file to parse ')  # TODO make this a dialog
            self.filename, self.file_extension = os.path.splitext(self.file_name)
            self.acceptable_file = True
       

    def extract_metadata(self):
        """Extracts the meta data from the xml file in order to create the puzzle using BeautifulSoup
        it creates several class variables:
        rows_per_box:the number of rows per box
        cols_per_box:number of columns per box,
        value_range:the numbers that can be used to fill the boxes
        start_state:initial state of the puzzle,
        well_formed:true false or unknown indicates if start_state keys are in range and that it has a correct value_range,
        solable:indicates if the puzzle is solveable,
        unique_solution:indicates if there is onle one solution,
        pigeonhole:indicates if the puzzle is pigeonhole decideable"""
        if self.acceptable_file:
            with open(self.file_name, 'r') as file:
                content = file.readlines()  # extract rows per box
                content = "".join(content)
                bs_content = bs(content, 'xml')
                self.rows_per_box = int(
                    bs_content.find("rows_per_box").get_text())

                self.cols_per_box = int(
                    bs_content.find("cols_per_box").get_text())

                self.value_range = range(
                    1, (self.rows_per_box * self.cols_per_box) + 1)


                self.start_state = convert(bs_content.find("start_state"))

                self.well_formed = bool(
                    bs_content.find("well_formed").get_text())

                self.solvable = bool(bs_content.find("solvable").get_text())

                self.unique_solution = bool(
                    bs_content.find("unique_solution").get_text())

                self.pigeonhole = bool(bs_content.find(
                    "pigeonhole_decidable").get_text())



