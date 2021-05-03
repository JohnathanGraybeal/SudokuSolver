import os
from bs4 import BeautifulSoup as bs
import tkinter.filedialog


class FileParser:

    def __init__(self, file):
        """By default only sets the private property file to none when extract_metadata is called by the object instance it will have a value """
        self._file = None

    @property
    def file(self):
        """Returns the name of the file """
        return self._file

    @file.setter
    def file(self, user_file):
        """Validates the user selected file 
            it it's a valid file split into name and extension
            if it's not an xml extension set acceptable file to false and raise type exception
            then open file dialog so user can choose a valid file  """
        if os.path.isfile(user_file):
            self._file = user_file
            self._filename, self._file_extension = os.path.splitext(user_file)
            try:
                if self._file_extension != '.xml':
                    self.acceptable_file = False
                    raise TypeError('File must be a .xml file  ')
                else:
                    self.acceptable_file = True
            except TypeError:
                file_to_open = tkinter.filedialog.askopenfilename(
                    filetypes=[("XML", "*.xml")])
                self._file = file_to_open

        else:
            file_to_open = tkinter.filedialog.askopenfilename(
                filetypes=[("XML", "*.xml")])
            self._file = file_to_open

    @property
    def rows(self):
        """Returns number of rows in each subgrid  """
        name = self._filename + self._file_extension
        with open(name, 'r') as file:
            content = file.readlines()  # extract rows per box
            content = "".join(content)
            bs_content = bs(content, 'xml')
            self.rows_per_box = int(
                bs_content.find("rows_per_box").get_text())
            if self.rows_per_box < 0:
                self.rows_per_box = 3
        return self.rows_per_box

    @property
    def cols(self):
        """Returns number of cols """
        name = self._filename + self._file_extension
        with open(name, 'r') as file:
            content = file.readlines()  # extract rows per box
            content = "".join(content)
            bs_content = bs(content, 'xml')
            self.cols_per_box = int(
                bs_content.find("cols_per_box").get_text())
            if self.cols_per_box < 0:
                self.cols_per_box = 3
        return self.cols_per_box

    @property
    def value_range(self):
        """Returns the range of valid values as a tuple """
        if self.rows == 0 and self.cols == 0:  # handle 0x0
            self.range = {1}
        elif self.rows >= 1 and self.cols == 0:  # hand nx0
            self.range = {1, self.rows}
        elif self.rows == 0 and self.cols >= 1:  # handle 0xn
            self.range = {1, self.cols}
        else:
            range_val = self.rows * self.cols
            self.range = {1, range_val}
        return self.range

    @property
    def start_state(self):
        """returns a dict of the start state or puzzle hints """
        name = self._filename + self._file_extension
        with open(name, 'r') as file:
            content = file.readlines()
            content = "".join(content)
            bs_content = bs(content, 'xml')
            self.state = str(bs_content.find("start_state"))
        if "<start_state/>" in self.state:
            self.state = {}

        elif "<start_state/>" not in self.state:
            if " " in self.state:
                self.state = self.state.replace(" ", "",)
            if "\n" in self.state:
                self.state = self.state.replace("\n", "",)
            if "\\" in self.state:
                self.state = self.state.replace("\\", "",)
                self.state = self.state.replace(
                    "<start_state>", "", 1)
                self.state = self.state.replace(
                    "</start_state>", "", 1)
                self.state = eval(self.state)
        else:
            self.state = {}

        return self.state

    @property
    def well_formed(self):
        "returns the value of the well formed property from the xml file"
        name = self._filename + self._file_extension
        with open(name, 'r') as file:
            content = file.readlines()
            content = "".join(content)
            bs_content = bs(content, 'xml')
            self.formed = str(
                bs_content.find("well_formed").get_text())
        return self.formed

    @property
    def solvable(self):
        """ returns T/F if the puzzle is able to be solved"""
        name = self._filename + self._file_extension
        with open(name, 'r') as file:
            content = file.readlines()
            content = "".join(content)
            bs_content = bs(content, 'xml')
            self.can_solve = str(bs_content.find("solvable").get_text())
        return self.can_solve

    @property
    def unique_solution(self):
        """returns T/F if the puzzle only has one unique solutions """
        name = self._filename + self._file_extension
        with open(name, 'r') as file:
            content = file.readlines()
            content = "".join(content)
            bs_content = bs(content, 'xml')
            self.solution = str(
                bs_content.find("unique_solution").get_text())
        return self.solution

    @property
    def pigeonhole(self):
        """returns T/F if the puzzle is pigeonhole decidable """
        name = self._filename + self._file_extension
        with open(name, 'r') as file:
            content = file.readlines()
            content = "".join(content)
            bs_content = bs(content, 'xml')
            self.pigeonhole_decidable = str(bs_content.find(
                "pigeonhole_decidable").get_text())
        return self.pigeonhole_decidable

    def extract_data(self, file):
        """Calls all the properties to extract all of the data from a given file """
        self.file = file
        self.rows
        self.cols
        self.value_range
        self.start_state
        self.well_formed
        self.solvable
        self.unique_solution
        self.pigeonhole

    def display_attributes(self):
        """Displays the attributes of the file """
        print(f"File Name: {self.file}")
        print(f"Size: {self.rows} x {self.cols}")
        print(f"Well Formed: {self.well_formed}")
        print(f"Solvable: {self.solvable}")
        print(f"Unique Solution: {self.unique_solution}")
        print(f"Pigeon Hole Decideable: {self.pigeonhole}")
        print(f"Value Range: {self.value_range}")
        print("-"*56)
