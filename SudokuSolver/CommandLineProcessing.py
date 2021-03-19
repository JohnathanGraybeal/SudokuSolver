from FileParser import FileParser
import argparse
import os


class CommandLineProcessing:

    def __init__(self):
        """sets default values for instance variables and calls the procesing method  """
        self.file = None  # Set default values
        self.solve_on_startup = False
        self.time_delay = 0
        self.solution_name = None
        self.exit = None
        self.launch_file_picker_on_startup = False
        self.processing()

    def processing(self):
        """Does the command line prosessing possible args: -f,--File,-s,--Solve,-t,--Time,-n,--Name,-e,--Exit
        all values that it sets are optional so everything is intialized to none
        instance variables are: 
        file: the file path the user inputs set with -f,--File
        solve_on_start_up determines if program automatically starts solving set by -s,--Solve
        """
        cmd = argparse.ArgumentParser()

        cmd.add_argument("--h", default="Optional arguments: --f[File](Name of puzzle file), --s[Solve](Solve on startup?),\
         --t[Time](time delay),--n[Name](name of file to save current state of puzzle to),--e[Exit](exit after solving?)")

        cmd.add_argument("--f", default=None, help="The puzzle File")
        cmd.add_argument("--s", default=False,
                         help="Solve on startup?: y/n ignored if --f is None")
        cmd.add_argument(
            "--t", default=0, help="Float amount for time delay ignored if --f or --s is None")
        cmd.add_argument(
            "--n", default=None, help="Name of the file to save puzzle state to ignored ignored if --f or --s is None")
        cmd.add_argument("--e", default=False,
                         help="Exit on solve? y/n ignored if --n or --s is None")

        args = cmd.parse_args()

        # default to prevent access before asssignment error
        parser = FileParser("")
        if args.h:
            print(args.h)
        if args.f != None:  # if not default value then check if file exists if it does assign to instance variable
            try:
                if os.path.isfile(args.f):
                    self.file = args.f
                    parser = FileParser(self.file)

            except FileNotFoundError as ex:
                print(ex)
        if parser.filename == None:  # if no filename skip otherwise if --s is set then set solve_on_startup accordingly
            pass
        elif args.s != False:
            if args.s == "y".lower() or args.s == "True":
                self.solve_on_startup = True
            elif args.s == "n".lower() or args.s == "False":
                self.solve_on_startup = False
            else:
                pass
        else:
            pass
        if int(args.t) != 0 and int(args.t) > 0:  # if not the default and a non negative
            if parser.filename == None or self.solve_on_startup == None:
                pass
            else:
                try:
                    self.time_delay = float(args.t)
                except ValueError as error:
                    print(error)
        if args.n != None:  # if not default value set instance variable
            self.solve_on_startup = args.n
        if args.e != False:  # if not default value and select values exist then set exit to true
            if self.solve_on_startup == None or parser.filename == None:
                pass
            else:
                if args.e == "y".lower() or args.e == "true".lower():
                    self.exit = True
                else:
                    pass


cmd = CommandLineProcessing()
