import os
from tkinter.filedialog import askopenfilename
from bs4 import BeautifulSoup as bs


class FileParser:

    def __init__(self, file):
        """
        takes a file as a argument splits it into a filename and extension,then checks if the extension is xml 
        if extension is xml parses the file to extract puzzle attributes 
        """
        self.rows_per_box = 3
        self.cols_per_box = 3
        self.start_state = {(): [1, self.rows_per_box * self.cols_per_box]}

        self.open_file(file)
        self.extract_metadata()

    def open_file(self, file):
        """Tries to open the user inputed file splits the file name into name and extension
        checks if the file has an xml extension if it doesn't raise a type error
        defines these instance variables:
        filename: the name of the file
        file_extension:the file extension
        acceptable_file: boolean if the file is an acceptable format to parse """

        if os.path.isfile(file):
            self.filename, self.file_extension = os.path.splitext(file)
            if self.file_extension != '.xml':
                self.acceptable_file = False
                raise TypeError('Select an xml file to parse ')
            else:
                self.acceptable_file = True
        else:
            self.acceptable_file = False
            self.filename = None
            self.file_extension = None

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
            name = self.filename + self.file_extension
            with open(name, 'r') as file:
                content = file.readlines()  # extract rows per box
                content = "".join(content)
                bs_content = bs(content, 'xml')

                self.rows_per_box = int(
                    bs_content.find("rows_per_box").get_text())
                if self.rows_per_box < 0:
                    self.rows_per_box = 3

                self.cols_per_box = int(
                    bs_content.find("cols_per_box").get_text())
                if self.cols_per_box < 0:
                    self.cols_per_box = 3

                self.value_range = range(
                    1, (self.rows_per_box * self.cols_per_box) + 1)

                self.start_state = str(bs_content.find("start_state"))

                if "<start_state/>" in self.start_state:
                    self.start_state = {
                        (): [1, self.rows_per_box * self.cols_per_box]}

                elif "<start_state/>" not in self.start_state:
                    self.start_state = self.start_state.replace(
                        "<start_state>", "", 1)
                    self.start_state = self.start_state.replace(
                        "</start_state>", "", 1)
                    self.start_state = eval(self.start_state)
                else:
                    self.start_state = {
                        (): [1, self.rows_per_box * self.cols_per_box]}

                self.well_formed = str(
                    bs_content.find("well_formed").get_text())

                self.solvable = str(bs_content.find("solvable").get_text())

                self.unique_solution = str(
                    bs_content.find("unique_solution").get_text())

                self.pigeonhole = str(bs_content.find(
                    "pigeonhole_decidable").get_text())
