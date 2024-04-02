from flask import Flask, render_template, redirect

web=Flask(__name__)

@web.route("/")
def index_page():

    return render_template("index.html")

@web.route("/about-us")
def about_page():

    return render_template("about.html")

@web.route("/services")
def serv_page():

    return render_template("services.html")

@web.route("/contact_us")
def cont_page():

    return render_template("contact.html")
    


if __name__=="__main__":
    web.run(port="2034", debug=True)
