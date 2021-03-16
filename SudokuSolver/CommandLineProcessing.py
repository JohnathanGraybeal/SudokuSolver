import FileParser
import getopt
import sys
import os


class CommandLineProcessing:
    def __init__(self):
        argList = sys.argv[1:]
        options = "fstne"
        long_options = ["File", "Solve", "Time", "Name", "Exit"]
        self.file = None
        self.solve_on_startup = None
        self.time_delay = None
        self.solution_name = None
        self.exit = None
        
        args, values = getopt.getopt(argList, options, long_options)

        for current_arg, current_val in args:

            if current_arg in ("-f", "--File"):
                try:
                    if os.path.isfile(current_val):
                        self.file = current_val
                except FileNotFoundError as ex:
                    print(ex)
            elif current_arg in ("-s", "--Solve"):
                if Fileparser.file_name == None or FileParser.filename == None:
                     pass
                else:

                    if current_val == "y".lower() or current_val == "True":
                        self.solve_on_startup = True
                    elif current_val == "n".lower() or current_val == "False":
                         self.solve_on_startup = False
                    else:
                         pass

            elif current_val in ("-t", "--Time"):
                if FileParser.file_name == None or FileParser.filename == None or self.solve_on_startup == None:
                    pass
                else:
                     try:

                        self.time_delay = float(current_val)
                     except ValueError as error:
                         print(error)
            elif current_arg in ("-n", "--Name"):
                 self.solve_on_startup = current_val
            elif current_arg in ("-e", "--Exit"):
                if self.solve_on_startup == None or Fileparser.file_name == None or FileParser.filename == None:
                     pass
                else:
                    pass #TODO implement writing puzzle state to a file
        
        
            
             
        
             
     
   
        
        
        
