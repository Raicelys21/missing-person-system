from django.apps import AppConfig
from flask import Flask, render_template, url_for, request


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'




