import os
import json
from flask import Flask

PORT = 5000
HOST = "127.0.0.1"
DEBUG = True

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, static_folder=ROOT_DIR + "/static/")
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

comm_file_name = os.path.join(app.static_folder, "js", "committees.json")
comm_file = open(comm_file_name)
committees = json.load(comm_file)

member_file_name = os.path.join(app.static_folder, "js", "secratariat.json")
member_file = open(member_file_name)
members = json.load(member_file)

member_file_name = os.path.join(app.static_folder, "js", "executive_board.json")
eb_member_file = open(member_file_name)
eb_members = json.load(eb_member_file)

tech_file_name = os.path.join(ROOT_DIR, "static", "js", "tech-team.json")
tech_file = open(tech_file_name)
tech_members = json.load(tech_file)

@app.context_processor
def utility_functions():
    def print_in_console(message):
        print(str(message))
    return dict(mdebug=print_in_console)