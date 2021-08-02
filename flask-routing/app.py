from flask import Flask, render_template, make_response, redirect, url_for, request
from forms import SignupForm
from flask import g

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path=''
)
app.config.from_object('config.Config')


@app.route("/home")
def home():
    return "Hello World!"


@app.route("/api/v1/users/", methods=['GET', 'POST', 'PUT'])
def users():
    # ... Logic goes here
    return "This API endpoint accepts GET, POST, or PUT requests"


@app.route('/user/<username>')
def profile(username):
    # ... Logic goes here
    return "Hello, " + str(username)


@app.route('/<int:year>/<int:month>/<title>')
def article(year, month, title):
    # ... Logic goes here
    return "Article Title: " + str(title) + "<br/> Month: " + str(month) + "<br/> Year: " + str(year)


@app.route("/")
def index():
    """Serve homepage template."""
    return render_template(
        "index.html",
        title='Flask Tutorial: Part 4- Flask Routing',
        body='At first glance, it is hard to imagine routing to be an "art." We will typically reserve a URL path, '
             'such as / or /home, associate this with a page template, and serve said template to the user, '
             'perhaps with added business logic. That perspective works fine for small-scale applications, '
             'but meaningful applications (or APIs) are not static one-to-one mappings. Apps are a medium for data '
             'such as user-generated content such as user profiles or author posts, and routes define the way our '
             'users will access data which is always changing. '
    )


@app.route("/api/v2/test_response")
def api_users():
    response = make_response('Test worked!', 200)
    response.headers['Content-Type'] = 'application/json'
    return response


@app.route("/signin")
def dashboard():
    return redirect('/dashboard.html')


@app.route("/login")
def login():
    return redirect(url_for('dashboard'))


@app.route('/signup', methods=['GET', 'POST'])
def signup_page():
    """User sign-up page."""

    return render_template(
        '/signup.html',
        title='Create an Account | Flask-Login Tutorial.',
        form=SignupForm(),
        template='signup-page',
        body="Sign up."
    )


@app.route("/g")
def get_test_value():
    if 'test_value' not in g:
        g.test_value = 'This the g-value'
    return g.test_value


@app.route("/rm/g")
def rm_test_value():
    if 'test_value' in g:
        redirect(url_for('remove_test_value'))
    else:
        return "There is NO g-value"


# @app.teardown_testable
def remove_test_value():
    test_value = g.pop('test_value', None)
    return test_value + " being removed"


@app.errorhandler(404)
def not_found(arg):
    """Page not found."""
    # return make_response(
    return render_template('/404.html', message='Page Not Found')  # ,
    # 404
    # )


@app.errorhandler(400)
def bad_request():
    """Bad request."""
    return make_response(
        render_template("400.html", message='Page Not Found'),
        400
    )


@app.errorhandler(500)
def server_error(arg):
    """Internal server error."""
    # return make_response(
    return render_template("/500.html", message='Server Error')  # ,
    # 500
    # )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
