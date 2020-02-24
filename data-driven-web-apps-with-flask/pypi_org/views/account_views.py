import flask

from pypi_org.infrastructure.view_modifiers import response

blueprint = flask.Blueprint("account", __name__, template_folder="templates")

# ################### INDEX #################################


@blueprint.route("/account")
@response(template_file="account/index.html")
def index():
    return {}


@blueprint.route("/<int:rank>")
def popular(rank: int):
    return f"The details for the {rank}th most popular package"


# ################### REGISTER #################################


@blueprint.route("/account/register", methods=["GET"])
@response(template_file="account/register.html")
def register_get():
    return {}


@blueprint.route("/account/register", methods=["POST"])
@response(template_file="account/register.html")
def register_post():
    r = flask.request

    name = r.form.get('name')
    email = r.form.get('email', '').lower().strip()
    password = r.form.get('password', '').strip()

    if not name or not email or not password:
        return {
            'name': name,
            'email': email,
            'password': password,
            'error': "Some required fields are missing.",
        }

    # TODO: Create the user
    # TODO: Log in browser as a session

    print('Redirecting to account page :)')
    return flask.redirect('/account')


# ################### LOGIN #################################


@blueprint.route("/account/login", methods=["GET"])
@response(template_file="account/login.html")
def login_get():
    return {}


@blueprint.route("/account/login", methods=["POST"])
@response(template_file="account/login.html")
def login_post():
    return {}


# ################### LOGOUT #################################


@blueprint.route("/account/logout")
def logout():
    return {}
