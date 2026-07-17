"""
==========================================================
Topic: yield from (Delegating to Another Generator)
==========================================================
"""

def python_playlist():
    yield "Python Variables"
    yield "Python Loops"
    yield "Python Functions"


def javascript_playlist():
    yield "JavaScript Variables"
    yield "JavaScript Arrays"


def full_course():

    yield "Welcome to the Course"
    
    """
    for video in python_playlist():

        yield video
    """
    
    yield from python_playlist()

    yield "Take a Short Break ☕"

    yield from javascript_playlist()

    yield "Congratulations! Course Completed 🎉"


for video in full_course():
    print(video)