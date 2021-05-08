from flask import Flask, render_template, request


app = Flask(__name__)
app.config.from_object('config')

# DB settings

# col = db["Index"]


@app.route('/', methods=['GET', 'POST'])
def index():
    """Return index.html
    """
    if request.method == 'POST':
        keyword = request.form['keyword']
        if keyword:
            return render_template(
                'index.html',
                query=col.find_one({'keyword': keyword}),
                keyword=keyword)
    return render_template('index.html')
