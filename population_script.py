# Population script for WAD2 project 2018 by Euan McGrevey and Sam Griffin

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
					  'uofgconnect.settings')

import random

import django
django.setup()
from social.models import University, College, Subject, Module, UserProfile, Follow, Post, Comment, Notification
from django.contrib.auth.models import User

from datetime import date

def populate():

	userdata = [
		{
			"fname": "John",
			"sname": "Doe",
			"matric": "1234567"
		},
		{
			"fname": "Jane",
			"sname": "Doe",
			"matric": "2234567"
		},
		{
			"fname": "John",
			"sname": "Lennon",
			"matric": "3234567"
		},
		{
			"fname": "Terence",
			"sname": "Stephens",
			"matric": "4234567"
		},
		{
			"fname": "Sally",
			"sname": "Jones",
			"matric": "5234567"
		},
		{
			"fname": "Gary",
			"sname": "Jones",
			"matric": "6234567"
		},
		{
			"fname": "Sam",
			"sname": "Griffin",
			"matric": "2327827"
		},
		{
			"fname": "Euan",
			"sname": "McGrevey",
			"matric": "2255355"
		},
		{
			"fname": "Martin",
			"sname": "Ganly",
			"matric": "2325580"
		},
		{
			"fname": "Chak",
			"sname": "Ho",
			"matric": "2268750"
		}
	]

	data = {
		"University of Glasgow": { # University
			"logo": None,
			"colour": "003865",
			"email_domain": "student.gla.ac.uk",
			"colleges": { # Colleges
				"College of Science and Engineering": {
					"Computing Science": [ # Subject
						"Computer Systems 2", # Module
						"Java Programming 2",
						"Object Oriented Software Engineering",
						"Algorithms and Data Structures"
					],
					"Physics": [
						"Programming C under Linux",
						"Forces"
					],
					"Chemistry": [
						"Acids"
					]
				},
				"College of Arts": {
					"Music": [
						"Music Theory",
						"Music History"
					]
				}
			}
		},
		"University of Sussex": { # University
			"logo": None,
			"colour": "003B49",
			"email_domain": "sussex.ac.uk",
			"colleges": { # Colleges
				"College of Science and Engineering": {
					"Computer Science and Artificial Intelligence": [ # Subject
						"Introduction to Programming", # Module
						"Mathematical Concepts",
						"Programming Concepts",
						"Computer Vision",
						"Intelligence in Animals and Machines"
					]
				}
			}
		}
	}


	for uni, uni_data in data.items():
		u = add_uni(uni, uni_data['colour'], uni_data['email_domain'])

		uni_users = []

		for x in range(random.randint(1, len(userdata))): # Will create at least one user at each university
			udata = random.choice(userdata); # Chooses data at random

			# Note: deliberately able to have 2 users with the same name, like the real world
			print("Creating user: " + udata['fname'] + " " + udata['sname'])
			user = User.objects.create_user(udata['matric'] + str(x) + uni_data['email_domain'], udata['matric'] + "@" + uni_data['email_domain'], "password")
			user.first_name = udata['fname']
			user.last_name = udata['sname']
			user.save()

			up = UserProfile.objects.get_or_create(user=user, university=u, dob=date(random.randint(1990,2018), random.randint(1,12), random.randint(1,28)))[0]
			up.save()

			uni_users.append(user)

		for college, subjects in uni_data['colleges'].items():
			c = add_col(college, u)

			for subject, modules in subjects.items():
				s = add_sub(subject, c)

				for module in modules:
					m = add_module(module, s)

					num_followers = random.randint(1, len(uni_users))
					print("Adding " + str(num_followers) + " follower(s) for " + m.name)
					for x in range(num_followers):
						f = Follow.objects.get_or_create(user=random.choice(uni_users), module=m)[0]
						f.save()


	# Now to create some dummy people and posts

	# users = None

def add_module(name, sub):
	print("Creating module: " + name)
	m = Module.objects.get_or_create(subject=sub, name=name)[0]
	m.save()
	return m

def add_sub(name, college):
	print("Creating subject: " + name)
	s = Subject.objects.get_or_create(name=name, college=college)[0]
	s.save()
	return s

def add_col(name, uni):
	print("Creating college: " + name)
	c = College.objects.get_or_create(name=name, university=uni)[0]
	c.save()
	return c

def add_uni(name, colour, domain, logo=None):
	print("Creating university: " + name)
	u = University.objects.get_or_create(name=name, colour=colour, email_domain=domain, logo=logo)[0]
	u.save()
	return u




# Execution
if __name__ == '__main__':
	print("Starting population script...")
	populate()
	print("Population script complete")
