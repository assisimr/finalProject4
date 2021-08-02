"""Route declaration."""
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def home():
    """Landing page."""
    nav = [
        {'name': 'Home', 'url': 'https://example.com/1'},
        {'name': 'About', 'url': 'https://example.com/2'},
        {'name': 'Pics', 'url': 'https://example.com/3'}
    ]
    return render_template(
        'home.html',
        nav=nav,
        title="Jinja Demo Site",
        description="Smarter page templates with Flask & Jinja."
                    "Layout: The majority of web apps have some sort of structure shared between pages. This can be "
                    "as simple as repeating the same <head> across multiple pages or enforcing a general physical "
                    "structure, such as a standard content + sidebar look. A coherent web app will likely have very "
                    "few unique layouts."
                    "Page: Page templates are the self-explanatory meat and potatoes of templating. While this blog "
                    "has hundreds of posts, each post is merely an instance of a single post template: a uniquely "
                    "assembled section of our site that can be replicated with different data."
                    "Partial: Partials are standalone snippets that can be shared by pages where needed. Think of "
                    "navigation elements, widgets, or anything else designed to be shared across parts of your site.",
        status={'active': True}
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)