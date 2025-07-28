from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Instagram Link Extractor</title>
</head>
<body>
    <h2>Paste your Instagram Reel URL</h2>
    <form method="POST">
        <input name="url" type="text" style="width: 400px;" placeholder="https://www.instagram.com/reel/..." required>
        <button type="submit">Submit</button>
    </form>

    {% if result %}
        <h3>Response:</h3>
        <p>{{ result }}</p>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        url = request.form['url']
        result = f'You said: {url}'
    return render_template_string(HTML_PAGE, result=result)

if __name__ == '__main__':
    app.run(debug=True)
