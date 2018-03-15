# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from social.models import University, College, Subject, Module, UserProfile, Follow, Post, Comment, Notification



class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

    
# Register your models here.
admin.site.register(University)
admin.site.register(College)
admin.site.register(Subject)
admin.site.register(Module)
admin.site.register(UserProfile)
admin.site.register(Follow)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Notification)
