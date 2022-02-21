"""
This file’s sole purpose is to serve the user’s score
currently in the scores.txt file over HTTP with HTML.
This will be done by using python’s flask library.
"""
from flask import Flask, request, render_template
from Score import get_users_scores_html

app = Flask("WorldOfGames")


@app.route('/', methods=['GET'])
def score_server():
    """
    Methods
    This function will serve the score.
    It will read the score from the scores file
    and will return an HTML that will be as follows:
    """
    if request.method == 'GET':
        html_addition = get_users_scores_html()
        return f"""
          <html>
          <head>
              <title>Scores Game</title>
          </head>
          <body>
              {html_addition}
          </body>
          </html>
          """


# @app.route('/')
# def index():
#     html_addition = get_users_scores_html()
#     return render_template('index.html', SCORE=html_addition)

if __name__ == '__main__':
    # app.run(host="127.0.0.1", port=5000, debug=True)
    app.run(host="0.0.0.0", debug=True)


