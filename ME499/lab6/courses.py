#!usr\bin\env python 3
# -*-coding: utf-8 -*-


"""
****************************
    ME 499 Spring 2018
        Lab_6 courses.py
        20 May 2018
    Samuel J. Stumbo
****************************
"""

"""
References used:
*****************************
1. Dr. Smart's scraper.py and cash.py
2. https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe
3. http://docs.python-guide.org/en/latest/scenarios/scrape/
4. https://www.youtube.com/watch?v=ng2o98k983k
5. https://stackoverflow.com/questions/36709165/beautifulsoup-object-of-type-response-has-no-len
6. https://www.digitalocean.com/community/tutorials/how-to-scrape-web-pages-with-beautiful-soup-and-python-3
*****************************
"""
import requests
from bs4 import BeautifulSoup
import html5lib


class Course:
    def __init__(self, department, course_number, term, course_description, turms, crns, instructors, days, times):
        self.department = department
        self.course_number = course_number
        self.term = term
        self.turms = turms
        self.crns = crns
        self.instructors = instructors
        self.days = days
        self.times = times
        self.description = course_description
        self.crns = crns

    def __str__(self):
        return 'Class:                   {0} {7}: {1} \n'\
               'Term:                    {2}  \n'\
               'CRN:                     {3}  \n'\
               'Instructor:              {4} \n'\
               'Days:                    {5} \n'\
               'Times:                   {6}'.format(self.department, self.description, self.term, self.crns,
                                                          self.instructors, self. days, self.times, self.course_number)


def scrape_course(department, course_number, term):
    """
    This function scrapes an OSU course catalog page based on any college of engineering class input.
    """
    # This first part extracts the user input to build the url string that will be processed in the scraper.


    year = term[1:3]
    season = term[0]
    if season == 'F':
        term_num = '01'
        year = str(int(year) + 1)
    if season == 'W':
        term_num = '02'
    if season == 'S':
        term_num = '03'

    url = 'http://catalog.oregonstate.edu/CourseDetail.aspx?Columns=afghijklmnopqrstuvwyz'\
            '{&SubjectCode=' + department + '&CourseNumber=' + str(course_number) + '&Term=20' + year + term_num

    # This part scrapes the website
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html5lib")
    trs = soup.find_all('tr')
    headers = []

    # This takes care of the headers for the table
    for tr in trs:
        for header in tr.find_all('b'):
            stripped_header = header.text
            headers.append(stripped_header)

    # This part takes care of the body of the table
    locater = []
    j = 0
    table_data = []
    for tr in trs:
        for td in tr.find_all('td'):
            stripped_td = td.text
            for element in td.find_all('font'):
                if element.text == term:
                    locater.append(j)
                j += 1
                table_data.append(element.text)

    # This takes care of the course description
    course_description = soup.find('h3').text
    course_description = course_description.replace('.', '').replace('(4)','').replace('\n', ' ').replace('   ', '')\
        .replace(department+ ' ' + str(course_number), "")



    # This part pulls specific items from our table
    turms = []
    crns = []
    instructors = []
    calendars = []
    for element in locater:
        turm = table_data[element]
        crn = table_data[element + 1]
        section = table_data[element + 2]
        Cr = table_data[element + 3]
        pass_no = table_data[element + 4]
        instructor = table_data[element + 5]
        day_time_date = table_data[element + 6]
        day_time_date = day_time_date.replace('\n', '')
        day_time_date = day_time_date.replace(' ', '')
        location = table_data[element + 7]
        #print(turm, crn, instructor, day_time_date)
        turms.append(turm)
        crns.append(crn)
        instructors.append(instructor)
        calendars.append(day_time_date)
    days = []
    times = []

    if len(calendars) > 1:
        for i in range(len(calendars)):
            days.append(calendars[i][0:2])
            times.append(calendars[i][2:11])
    else:
        calendars = str(calendars)
        days = calendars[1:4].replace("'", '')
        times = calendars[4:13]
    table_headings = headers[0], headers[1], headers[5], headers[6]
    class_table = [list(zip(turms, crns, instructors, calendars))]
    formatted_table = [table_headings, class_table]



    description = 'Place holder'
    c = Course(department, course_number, term, course_description, turms, crns, instructors, days, times)

    return c

if __name__ == "__main__":

    c = scrape_course('ME', 451, 'F18')

    print(c)

