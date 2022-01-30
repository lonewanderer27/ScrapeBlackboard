import os

from prettytable import PrettyTable

from courses import Courses
from login import Login

login = Login()
login.bb_login(user_id=os.environ['bb_username'], password=os.environ['bb_password'])
# b is the currently active webdriver object that has BB logged in! so we fetch that to fetch whatever want.
courses = Courses(login.b)
subjects_list = []
for course in courses.courses_view():
    # print(course.text)
    if course.text != "":
        subjects_list.append(course.text)


table = PrettyTable()
table.add_column("2nd Sem Subjects", subjects_list)
table.align = "c"
print(table)







# driver.close()