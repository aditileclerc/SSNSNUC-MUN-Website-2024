from app import app
from flask import render_template, request, url_for, send_file, redirect
import config
import copy
import os
import webbrowser


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


@app.route("/", methods=["GET"])
def index():
    if request.method == "GET":
        comm_copy = [copy.deepcopy(x) for x in config.committees]
        for committee_obj in comm_copy:
            if committee_obj["name"] != "IPC":
                committee_obj["img"] = url_for("static", filename=committee_obj["img"])
            else:
                committee_obj["ipr_img"] = url_for("static", filename=committee_obj["ipr_img"])
                committee_obj["ipp_img"] = url_for("static", filename=committee_obj["ipp_img"])

        return render_template(
            "index.html", page_title="Home", committees=comm_copy
        )


@app.route("/organising-committee/", methods=["GET"])
def organising_committee():
    if request.method == "GET":
        # creating copy to avoid modifying original info - fixes images disappearing on refresh issue
        members_copy = [copy.deepcopy(x) for x in config.members]

        for member in members_copy:
            member["img"] = url_for("static", filename=member["img"])
        return render_template(
            "organising_committee.html",
            members=members_copy,
            page_title="Organising Committee",
        )


@app.route("/committee/<commname>", methods=["GET"])
def committee(commname):
    display_committee = None
    # Figure out which committe info to display
    for committee in config.committees:
        if committee["url"] == commname:
            display_committee = committee

    if display_committee is None:
        return render_template("404.html"), 404

    # Only get info about EB members for required committee
    comm_eb = [x for x in config.eb_members if x["committee"] == commname]
    comm_eb_copy = [copy.deepcopy(x) for x in comm_eb]
    for eb_member in comm_eb_copy:
        eb_member["img"] = url_for("static", filename=eb_member["img"])

    if request.method == "GET":
        return render_template(
            "committee.html",
            committee=display_committee,
            members=comm_eb_copy,
            page_title=commname.upper(),
        )



@app.route("/about/", methods=["GET"])
def about():
    if request.method == "GET":
        return render_template("about.html", page_title="About Us")

@app.route("/sponsors/", methods=["GET"])
def sponsors():
    if request.method == "GET":
        return render_template("sponsors.html", page_title="Sponsors")

@app.route("/con-details/", methods=["GET"])
def details():
    if request.method == "GET":
        return render_template("con-details.html", page_title="Conference Details")
    
@app.route("/registrations/<type>", methods=["GET"])
@app.route("/registrations/", methods=["GET"])
def registrations(type=""):
    # print(type)
    # if type == "delegate":
    #     # return render_template("coming-soon.html", page_title='Coming Soon')
    #     return render_template(
    #         "registration_form_delegate.html",
    #         page_title="Delegate Matrix",
    #         doc_link="",
    #     )
    # if type == "ip":
    #     return redirect(url_for("registrations"))
    # return render_template(
    #     "registration_form_ip.html",
    #     page_title="IP Registration"
    #     # doc_link="https://docs.google.com/forms/d/e/1FAIpQLSf7kfF79qbK3LaXDxFx7zoxSiWFUNbn0wXcKpPl17dOQLa4-Q/viewform",
    # )
    # elif type == 'eb':
    #     return render_template('registration_form.html', page_title='EB Registration', doc_link="https://docs.google.com/forms/d/e/1FAIpQLSfAmJ62D7SHiKNAsJzO1iIkYfSEqpoYLyvdJ0xCuvnSG-2xfg/viewform?embedded=true")
    # elif type == 'priority':
    #     # comm_copy = [copy.deepcopy(x) for x in config.committees if x['name'] != "IP"]
    #     # return render_template("committee_selection.html", page_title="Priority Delegate Registration", committees = comm_copy)
    #     return render_template("payment_rules.html")
    # elif type is not None:
    #     return render_template("404.html"), 404
    return render_template("registrations.html", page_title="Registrations")


@app.route("/coming-soon/", methods=["GET"])
def coming_soon():
    return render_template("coming-soon.html", page_title="Coming Soon")



# @app.route("/payments", methods=["GET"])
# def payments():
#     return render_template("payments.html", page_title="Payments")


@app.route("/contact/", methods=["GET"])
def contact():
    return render_template("contact_us.html", page_title="Contact Us")


@app.route("/announcements", methods=["GET"])
def announcements():
    return render_template("announcements.html", page_title="Announcements")


@app.route("/rop-guide", methods=["GET"])
def rop_guide():
    return send_file(os.path.join(config.ROOT_DIR, "static", "rop.pdf"))



@app.route("/download_files", methods=["GET"])
def download_files():
    return render_template("download.html")
