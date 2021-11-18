import os
import subprocess
import sys
import traceback 
import unittest

# DICTIONARY
VERSION = "1.0.0" # Version of the agent
DEBUG   = False   # Flag for debug operation
VERBOSE = False   # Flag for verbose operation
FIRST   = 0       # first element in a list
LAST    = -1      # last element in a list

class Command:
    """ Command() --> Command Object """

    def __init__(self, command):
        """ Creates an instance of an object of type Command. """
        self.command    = str(command).strip()    # The command to execute
        self._stdout    = subprocess.PIPE         # Standard Output PIPE
        self._stderr    = subprocess.PIPE         # Standard Error PIPE
        self.output     = "Command not executed"  # Output from command
        self.error      = "Command not executed"  # Error from command
        self.returnCode = None                    # Default return code from command

    def run(self):
        """ Executes the command in the specified shell. """
        try:
            results = subprocess.Popen(self.command        ,
                                       stdout=self._stdout ,
                                       stderr=self._stderr ,
                                       shell=True          ,
                                       encoding='utf-8'    )  # Execute the command

            self.output, self.error = results.communicate()  # Get output and error
            self.returnCode = results.returncode  # Get Return Code
        except Exception as e:
            self.output = str(e)
            self.error = f"Unable to execute: {self.command}\n{e}\n"
            if DEBUG: self.error += f"{traceback.print_exc()}" # optionally print the stack trace  
            self.returnCode = 113

    def show_results(self):
        """ Prints original command and resutls to stdout. """
        print(f"COMMAND     : {self.command}")
        print(f"OUTPUT      : {self.output.strip()}")
        print(f"ERROR       : {self.error.strip()}")
        print(f"RETURN CODE : {self.returnCode}")

    def return_results(self):
        """ Returns a dictionary containing the original command  and results. """
        results = {"command"     : self.command.strip(),
                   "output"      : self.output.strip(),
                   "error"       : self.error.strip(),
                   "return_code" : self.returnCode}
        return results

class Unit_Tests(unittest.TestCase):

   def test_unexecuted_command(self):
      """ An unexecuted command should indicate the command has not been executed """
      c=Command("dir")
      self.assertEqual(c.return_results()["output"], "Command not executed")
      self.assertEqual(c.return_results()["error"], "Command not executed") 
      self.assertEqual(c.return_results()["return_code"], None) 
      c.show_results()

   def test_known_good_command(self):
       """ Test a known good os command """
       c=Command("dir")
       c.run()
       self.assertEqual(c.return_results()["return_code"], 0)  
       c.show_results()   

   def test_known_bad_command(self):
      """ Test a known bad os command """ 
      c=Command("qwert")
      c.run()
      self.assertGreater(c.return_results()["return_code"], 0)     
      c.show_results()

if __name__ == "__main__":

   unittest.main()
   sys.exit(0)