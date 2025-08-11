from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()

from LS import linkedin_summarizer


app = Flask(__name__)


'''@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    summary_and_facts, interests, ice_breakers, profile_pic_url = ice_break_with(
        name=name
    )
    return jsonify(
        {
            "summary_and_facts": summary_and_facts.to_dict(),
            "interests": interests.to_dict(),
            "ice_breakers": ice_breakers.to_dict(),
            "picture_url": profile_pic_url,
        }
    )
'''
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    person_info,profile_pic_url=linkedin_summarizer(name=name)

    return jsonify(
        {
            "summary":person_info.summary,
            "facts": person_info.facts,
            "facts":person_info.facts,
            "Educational_Background":person_info.Educational_Background,
            "Skills":person_info.Skills,
            "Work_Experience":person_info.Work_Experience,
            "areer_Progression":person_info.Career_Progression,
            "Key_Achievements":person_info.Key_Achievements,
            "Cultural_Fit_Indicators":person_info.Cultural_Fit_Indicators,
            "picture_url": profile_pic_url,
        }
    )

if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)
