## Canvas-Exporter

An ongoing project to automate grading stuff in Canvas using Python3

#### Usage

You must add a config file (canvas.conf) in the same directory as exporter.py,
and it must be of the format:

{

    "URL": "https://lmsproxy.uits.iu.edu/lmspx-prd/canvas/",
    "token": [Kyle's Token],
    "course_id": [Course ID]
}

For help: 

`python3 grade.py -h`

`python3 grade.py quizzes -h`