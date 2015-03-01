__author__ = 'chrisshroba'

from flask import *

app = Flask(__name__)


answers = open("answers.txt").readlines()

answers = map(str.strip, answers)
answers = map(str.lower, answers)

answer_dict = {}

for answer in answers:
    answer_dict[answer] = False

teams = ["red", "green", "blue", "yellow"]

@app.route("/submit", methods=["POST"])
def submit_endpoint():
    answer = request.form.get("answer", "").lower()
    team = request.form.get("team", "").lower()
    if answer is "" or team is "" or team not in teams:
        return "Improperly formatted request."
    outcome = answer_dict.get(answer, None)
    if outcome is None:
        return "Failure"
    elif outcome is False:
        answer_dict[answer] = team
        return "Success!"
    else:
        return "Answer already supplied by team %s" % outcome

@app.route("/score")
def score():
    scores = {}
    for team in teams:
        scores[team]=0
    for answer, team in answer_dict.iteritems():
        if team in teams:
            scores[team] += 1
    response_string = ""
    for key in scores:
        response_string += "Team %s:\t %s\n" % (key,scores[key])
    return response_string

app.run(port = 1337,  debug=True)