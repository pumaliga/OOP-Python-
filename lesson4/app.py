import models
import sys
import traceback
from datetime import datetime
time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")


def main():
    programmer = models.Programmer('Alex', 'sasha@gmail.com', 100)
    candidate_one = models.Candidate('Artur Morgan', 'rdr2@gmail.com', 'Wild West', 'shooting', 'senior')
    return f'{programmer}', f'{candidate_one}'


logs = open("logs.py", 'a')
try:
    models.candidate_one
except Exception:
    exc_type, value, exc_traceback = sys.exc_info()
    logs.write(f"date: time: {time}, exception type: {exc_type.__name__},"
               f"full traceback: {repr(traceback.format_tb(exc_traceback))}, end= \n")

logs.close()


