## Canvas-Exporter

An ongoing project to automate grading stuff in Canvas using Python3

#### Usage

You must add a config file (canvas.conf) of the format:

{

    "URL": "https://lmsproxy.uits.iu.edu/lmspx-prd/canvas/",
    "token": [Kyle's Token],
    "course_id": [Course ID]
}

For help: 

`python3 exporter.py -h`

`python3 exporter.py quizzes -h`