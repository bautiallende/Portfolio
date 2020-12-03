from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)
import csv
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

