import argparse
import json
import os
from canvas import Canvas

commands = ['quizzes', 'split']

def quizzes(args):
    """
    This function blah ...

    Args:
        assignmentId (str|int): Unique Canvas ID for the assignment to grade.
        folder (str): Path to folder containing all of the quizzes labeled "username.pdf" for each student
        grades (str): Path to text document containing username and grade of students
    
    Returns:
        blah

    Blah:
        blah
    """

    conf = loadConfig(args.config)
    c = Canvas(conf["token"], conf["course_id"], conf["URL"])

    with open(args.grades) as f:

        lines = [line.strip() for line in f.readlines()]
        for line in lines:

            student,grade = line.split(" ")
            student_id = c.getStudentID(student)
            fname = "%s%s.pdf" % (folder, username)

            if not os.path.isfile(fname):
                raise Exception("File %s does not exist. " % fname)

            fid = c.uploadFileToSubmission(fname, args.assignment_id, student_id)
            c.gradeAssignmentAndComment(student_id, args.assignment_id, grade, files=[fid])

def split(args):
    pass

def quizzes_parser(parser):
    parser.add_argument("assignment_id", help="Unique Canvas ID for the assignment to grade")
    parser.add_argument("folder", help="Path to folder containing all of the quizzes labeled \"username.pdf\" for each student")
    parser.add_argument("grades", help="Path to text document containing username and grade of students.")
    parser.add_argument("config", help="Path to configuration file containing token and canvas URL")

def split_parser(parser):
    parser.add_argument("fname", help="Path to PDF document to split")
    parser.add_argument("names", help="Path to txt file containing ordered names of the new files")
    parser.add_argument("folder", help="Folder to save the new documents into")
    parser.add_argument("-p", '--pages', nargs='?', default=1, help="Optional. Number of pages each split document should have")

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