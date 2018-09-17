import argparse
import json
import os
import csv
from datetime import datetime
from canvas import Canvas
from string_matcher import StringMatcher
import PDF as pdf

commands = ['quizzes', 'autograder', 'merge', 'split']

# TODO : Fix implementation
def quizzes(args):
    """
    This function blah ...

    Args:
        assignmentId (str|int): Unique Canvas ID for the assignment to grade.
        files (list of str):    List of the files containing the quizzes
        usernames (str):        Path to text document containing usernames of students.
    
    Returns:
        blah

    Blah:
        blah
    """

    canvas_conf = loadConfig(args.canvas_config)
    c = Canvas(canvas_conf["token"], canvas_conf["course_id"], canvas_conf["URL"])
    students = c.getStudents()

    files = []
    with open(args.usernames) as f:

        grades = {}
        lines = [line.strip() for line in f.readlines()]
        for line in lines:
            student = line
            grades[student] = line

        files = [args.solution]
        for student in students:
            student_id = student["id"]
            username = student["login_id"]
            fname = "%s%s.pdf" % (args.folder, username)

            if not os.path.isfile(fname):
                print("File %s does not exist. " % fname)
                grade = 0
            else:
                grade = grades[username]
                files.append(c.uploadFileToSubmission(fname, args.assignment_id, student_id))

            print(c.gradeAssignmentAndComment(student_id, args.assignment_id, grade, files=files))

def autograder(args):

    due_date = datetime.strptime(args.due_date, "%Y-%m-%d")

    with open(args.file, 'rt', encoding='utf8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        reader.__next__() # skip the first line, which is the headers

        for row in reader:
            username = row[0].split('@')[0]
            submission_date = datetime.strptime(row[1].split('T')[0], "%Y-%m-%d")
            score = int(row[2])
            print(str(username) + ' ' + str(submission_date) + ' ' + str(score))

def split(args):
    pdf.split(args.fname, args.names, args.folder, int(args.pages))

def merge(args):
    pdf.merge(args.pdfs, args.output)

def quizzes_parser(parser):
    parser.add_argument("assignment_id", help="Unique Canvas ID for the assignment to grade")
    parser.add_argument("folder", help="Path to folder containing all of the quizzes. End with a \"/\".")
    parser.add_argument("usernames", help="Path to text document containing usernames of students,  with their corresponding grade next to their usernames seperated by a space.")
    parser.add_argument("canvas_config", help="Path to configuration file containing token and canvas URL")
    parser.add_argument("solution", nargs="?", help="Optional solution file to attach to each comment")
    parser.add_argument("comment", nargs="?", help="Optional comment to comment on each submission")
    parser.add_argument('-f', nargs = '*', dest = 'files', help = 'List of files contained within the given folder parameter to scan and grade', default = None)

def autograder_parser(parser):
    parser.add_argument("assignment_id", help="Unique Canvas ID for the assignment to grade")
    parser.add_argument("file", help="Path to CSV file exported from the autograder containing the grades to the assignment.")
    parser.add_argument("due_date", help="Due date for the assignment in the format yyyy-mm-dd")
    parser.add_argument("config", help="Path to configuration file containing token and canvas URL")

def merge_parser(parser):
    parser.add_argument("output", help="File to output merged pdfs to")
    parser.add_argument("pdfs", nargs='+', help='PDFs to merge')

def split_parser(parser):
    parser.add_argument("fname", help="Name/path to file to split")
    parser.add_argument("names", help="text document with names, in order, to split the document by")
    parser.add_argument("folder", help="folder to save all new pdfs in")
    parser.add_argument("pages", nargs="?", help="How many pages per document", default=1)

"""
 HELPER FUNCTIONS: 
"""
def loadConfig(config):
    """
    This function loads a config file into a JSON for use with our program.

    Args:
        config (str): Path to config file including JSON
    
    Returns:
        JSON containing our configuration data    
    """
    with open(config) as conf:
        return json.load(conf)

def main():
    __globals__ = globals()
    descr = "Use to automate grading for Canvas"
    parser = argparse.ArgumentParser(description=descr)
    subparsers = parser.add_subparsers()
    for cmd in commands:
        cmdf = __globals__[cmd]
        subp = subparsers.add_parser(cmd, help=cmdf.__doc__)
        __globals__[cmd + '_parser'](subp)
        subp.set_defaults(func=cmdf)
    args = parser.parse_args()

    if 'func' in args:
        args.func(args)
    else:
        parser.error("Please speecify at least one command")


if __name__ == "__main__":
    main()