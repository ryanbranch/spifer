import os
from pathlib import Path
import math
import random


"""
_________________________________________________
#TODO
_________________________________________________
 - PLACEHOLDER
     - place
         - holder
     - PLACE holder
     - PLACE holder
 - Placeholder
"""


# G L O B A L      C O N S T A N T S
# ________________________________
# GENERAL VARIABLES
# Path at which to save any outputs
OUTPUT_PATH = "saved\\output-path-test"
# Default file extension to use when saving outputs
OUTPUT_DEFAULT_EXTENSION = ".png"


# Container class for holding all variables and functions related to manipulation of images
class ServerSpider:

    def __init__(self):
        # MEMBER VARIABLES UPON INITIALIZATION
        # The X value of the current pixel being edited
        # Suffix to apply to the filename of the current file being held for output
        self.currentFileIndex = 1
        # List of file paths of all saved files
        self.outputFileList = []
        # Internal variable used to track error incidences during debugging
        self.errorCount = 0

        self.prepareDirectories()

    # Ensures that the directory specified for the output image(s) exists to avoid errors
    @staticmethod
    def prepareDirectories():
        print("PREPARING DIRECTORIES...")
        output_directory = os.path.dirname(OUTPUT_PATH)
        os.makedirs(output_directory, exist_ok=True)
        print("ALL DIRECTORIES PREPARED SUCCESSFULLY.\n")

    # Crawls around
    def crawl(self):
        print("the itsy bitsy spider...")


def main():
    # Initializes the random number generator
    random.seed("333   333   333")
    spider = ServerSpider()
    spider.crawl()
    return 0


main()