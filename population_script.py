# Population script for WAD2 project 2018 by Euan McGrevey

# Might be uofgsocial ? Confusing names >.<
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'uofgconnect.settings')

import django
django.setup()
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
from social.models import University, College, Subject, Module, UserProfile, Follow, Post, Comment, Notification

##### THIS ONE IS WRITTEN TO WORK FOR MODULE MODEL THAT HAS 3 FOREIGN KEYS
def populate():

    # modules
    modules = {"Computer Systems 2": {"university": "University of Glasgow",
                                      "college": "College of Science and Engineering",
                                      "subject": "Computing Science"},
               "Java Progamming 2": {"university": "University of Glasgow",
                                     "college": "College of Science and Engineering",
                                     "subject": "Computing Science"},
               "Algorithmic Foundations 2": {"university": "University of Glasgow",
                                             "college": "College of Science and Engineering",
                                             "subject": "Computing Science"},
               "Maths 2D": {"university": "University of Glasgow",
                            "college": "College of Science and Engineering",
                            "subject": "Mathematics"},
               "Maths 2E": {"university": "University of Glasgow",
                            "college": "College of Science and Engineering",
                            "subject": "Mathematics"},
               "Listening through Analysis": {"university": "University of Glasgow",
                                              "college": "College of Arts",
                                              "subject": "Music"},
               "Jazz and Blues": {"university": "University of Glasgow",
                                  "college": "College of Arts",
                                  "subject": "Music"}
               }

    # subjects
    subjects = ["Computing Science", "Mathematics", "Music"]

    # colleges
    colleges = ["College of Science and Engineering", "College of Arts"]

    # universities
    universities = {"University of Glasgow": {"logo":None,
                                              "colour": "blue",
                                              "email_domain": "@gla.ac.uk"}
                    }

    for uni, uni_data in universities.items():
        u = add_uni(uni, uni_data["logo"], uni_data["colour"], uni_data["email_domain"])

    for col in colleges:
        c = add_col(col)

    for sub in subjects:
        s = add_sub(sub)

    for module, module_data in modules.items():
        m = add_module(module, module_data["university"], module_data["college"], module_data["subject"])



    # Now to create some dummy people and posts

    users = None

def add_module(name, uni, col, sub):
    m = Module.objects.get_or_create(university=uni, college=col, subject=sub, name=name)[0]
    m.save()
    return m

def add_sub(name):
    s = Subject.objects.get_or_create(name=name)
    s.save()
    return s

def add_col(name):
    c = College.objects.get_or_create(name=name)
    c.save()
    return c

def add_uni(name, colour, domain, logo=None):
    u = University.objects.get_or_create(name=name, colour=colour, email_domain=domain, logo=logo)
    u.save()
    return u
    



# Execution
if __name__ == '__main__':
    print("Starting MicroBlog population script...")
    populate()



    
    
"""
#    # Subjects
#    sesubs = {"Computing Science": compsci_modules,
#              "Maths": maths_modules,
#        }
#        
#    msubs = {"Music": music_modules,}
#
#    # Colleges
#    uofgcolleges = {
#        "College of Science and Engineering": sesubs,
#        "College of Arts": msubs,
#        }
#
#    # Universities
#    unis = {
#        "University of Glasgow": uofgcolleges,
#        }
#
#    for uni, uni_data in unis.items():
#        u = add_university(uni, uni_data[""], )
#        for c in uni_data["uofgcolleges"]:
#            add_college(u, c[""], c[""]
#            for sub, sub_data in sesubs.items():
#                s = add_subject(



from uofgconnect import University, College, Subject, Module, UserProfile, Follow, Post, Comment, Notification


def populate():

    # modules
    compsci_modules = [
        {"name": "Computer Systems 2"},
        {"name": "Java Progamming 2"},
        {"name": "Algorithmic Foundations 2"}
        ]

    maths_modules = [
        {"name": "Maths 2D"},
        {"name": "Maths 2E"}
        ]

    music_modules = [
        {"name": "Listening through Analysis"},
        {"name": "Jazz and Blues"}
         ]

    # Subjects
    sesubs = {"Computing Science": compsci_modules,
              "Maths": maths_modules,
        }
        
    msubs = {"Music": music_modules,}

    # Colleges
    uofgcolleges = {
        "College of Science and Engineering": sesubs,
        "College of Arts": msubs,
        }

    # Universities
    unis = {
        "University of Glasgow": uofgcolleges,
        }

    for uni, uni_data in unis.items():
        u = add_university(uni, uni_data[""], )
        for c in uni_data["uofgcolleges"]:
            add_college(u, c[""], c[""]
            for sub, sub_data in sesubs.items():
                s = add_subject(


    # Print out universities
    for u in University.objects.all():
        for c in College.objects.filter(university=u):
            for s in Subject.objects.filter(college=c):
                for m in Module.objects.filter(subject=s):
                    print("- {0} - {1} - {2} - {3}".format(str(u), str(c), str(s), str(m)))

    # Print out users


# Helper functions

# adds a module to a subject
def add_module(sub, name):
    m = Module.objects.get_or_create(subject=sub, name=name)[0]
    m.save()
    return m

# adds a subject to a college
def add_subject(col, name):
    s = Subject.objects.get_or_create(college=col, name=name)[0]
    s.save()
    return s

# adds a college to a university
def add_college(uni, name):
    c = College.objects.get_or_create(university=uni, name=name)[0]
    c.save()
    return c

# adds to the list of univeristies
def add_university(name, colour, domain):
    u = University.objects.get_or_create(name=name)[0]
    u.logo = None
    u.colour = "blue"
    u.email_domain = "gla.ac.uk"
    u.save()
    return u


"""


# Execution
if __name__ == '__main__':
    print("Starting UofGSocial population script...")
    populate()
