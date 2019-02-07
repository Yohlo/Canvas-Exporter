import json
import os
from canvas import Canvas

#############
# Constants #
#############
QUIZZES_DIR = 'quizzes/'
CONF_FNAME = 'canvas.conf'

#########################
# Get the assignment id #
#########################
while(True):
    assignment_id = input('Please enter the id for this assignment on canvas:')
    assignment_id = int(assignment_id)
    correct = input('Is ' + str(assignment_id) + ' the correct assignment id? (Y/N):')
    if correct == 'y' or correct == 'Y':
        break
    print('Incorrect Assignment ID')

#####################################
# Get usernames and scores filename #
#####################################
while(True):
    grades_fname = input('Please type the name of the file containing usernames and grades (.csv of form username,grade):')
    if not os.path.isfile(grades_fname):
        print('File ' + grades_fname + ' does not exist.')
    else:
        break

#######################################
# Create dict of usernames and grades #
#######################################
print('Processing grading file...')
usernames_and_grades = {}
with open(grades_fname) as grade_file:
    lines = [line.split(',') for line in grade_file.readlines()]
    for line in lines:
        usernames_and_grades[line[0]] = line[1]

############################################
# Load Canvas details and construct object #
############################################
with open(CONF_FNAME) as conf:
    canvas_conf = json.load(conf)
    c = Canvas(canvas_conf["token"], canvas_conf["course_id"], canvas_conf["URL"])

#################################################
# Get students and their user names from Canvas #
#################################################
students = c.getStudents()

canvas_usernames = set()
for student in students:
    canvas_usernames.add(student['login_id'])

################################################################
# Get user names that occur both in Canvas and the grades file #
################################################################
good_usernames = canvas_usernames.intersection(set(usernames_and_grades.keys()))

#####################################
# Main Quiz Uploading/Grading Steps #
#####################################
skipped_usernames = set()
files = []
pdf_number = 1
for student in students:
    student_id = student['id']
    username = student['login_id']

    # Make sure the username is in the grade file
    if username not in good_usernames:
        # Skip to the next person
        skipped_usernames.add(username)
        continue

    # Grab the pdf filename
    fname = QUIZZES_DIR + str(pdf_number) + '.pdf'
    grade = usernames_and_grades[username]

    # Upload the files
    files.append(c.uploadFileToSubmission(fname, assignment_id, student_id))

    # Grade the assignments
    print(c.gradeAssignmentAndComment(student_id, assignment_id, grade, files=files))

    # Increment the pdf number
    pdf_number += 1

################
# Report stats #
################
print('Total number of users graded: ' + str(len(good_usernames)))
print('Total number of users on Canvas: ' + str(len(canvas_usernames)))
print('Usernames not graded (' + str(len(skipped_usernames)) + '):')
for username in skipped_usernames:
    print(username)

print('*** NOTE ***')
print('Skipped user names are in Canvas, but were not in the grading file...')


