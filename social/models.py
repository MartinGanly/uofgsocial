# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

class University(models.Model):
	name = models.CharField(max_length=255)
	logo = models.ImageField(upload_to='university_images', blank=True)
	colour = models.CharField(max_length=6)
	email_domain = models.CharField(max_length=255)
	slug = models.SlugField(default='', unique=True)

	def save(self, *args, **kwargs):
                self.slug = slugify(self.name)
                super(University, self).save(*args, **kwargs)

	class Meta:
                verbose_name_plural = 'Universities'

	def __str__(self):
		return self.name

class College(models.Model):
	name = models.CharField(max_length=255, default='College of Science and Engineering')
	university = models.ForeignKey(University, on_delete=models.CASCADE)

	def __str__(self):
		return self.name + " (" + self.university.name + ")"

class Subject(models.Model):
	name = models.CharField(max_length=255, default='Computing Science')
	college = models.ForeignKey(College, on_delete=models.CASCADE)

	def __str__(self):
		return self.name + " (" + self.college.university.name + ")"

class Module(models.Model):
	name = models.CharField(max_length=255, default='Computing Science 1P')
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

	def __str__(self):
		return self.name + " (" + self.subject.name + " - " + self.subject.college.university.name + ")"

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	picture = models.ImageField(upload_to='profile_images', blank=True)
	location = models.CharField(blank=True, max_length=255)
	bio = models.TextField(blank=True)
	dob = models.DateField(blank=True)
	# The register page, has 'languages' as a thing to input when registering, should i be worried?
	university = models.ForeignKey(University, blank=True, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.user.first_name + " " + self.user.last_name + " (" + str(self.university) + ")"

class Follow(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	module = models.ForeignKey(Module, on_delete=models.CASCADE)
	
	class Meta:
                verbose_name_plural = 'Followers'

	def __str__(self):
		return self.user.first_name + " " + self.user.last_name + " follows " + str(self.module)

class Post(models.Model):
	content = models.TextField()
	image = models.ImageField(upload_to='post_images', blank=True)
	video = models.URLField(blank=True)
	likes = models.IntegerField(default=0)
	module = models.ForeignKey(Module, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "Post by " + self.user.first_name + " " + self.user.last_name + " on " + str(self.created)

class Comment(models.Model):
	content = models.TextField()
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)


class Notification(models.Model):
	content = models.TextField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	link = models.URLField()
	read = models.BooleanField()
