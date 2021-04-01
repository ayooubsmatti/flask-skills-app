
from flask import Flask, render_template
skills_app = Flask(__name__)
my_skills = [("html", 60), ("css", 80), ("python", 90),
             ("MySql", 45), ("go", 26)]


@skills_app.route('/')
def homepage():
    return render_template("home.html", pagetitle="Home", custom_css="home")


@skills_app.route('/about')
def aboutpage():
    return render_template("about.html", pagetitle="About Us")


@skills_app.route('/add')
def addpage():
    return render_template("add.html", pagetitle="Add Skills", custom_css="add")


@skills_app.route('/skills')
def skillspage():
    return render_template("skills.html",
                           pagetitle="Add Skills",
                           page_head="My skills",
                           description="This is My Skills Page",
                           skills=my_skills,
                           custom_css="skills")


if __name__ == "__main__":
    skills_app.run(debug=True, port=9000)
