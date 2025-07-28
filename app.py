from flask import Flask, request, render_template, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Example: handling a form or JSON data
        data = request.form.get("message") or request.json.get("message")
        print("Received:", data)
        return jsonify({"response": f"You said: {data}"})
    
    # For GET request, return a simple HTML form or message
    return '''
        <form method="POST">
            <input name="message" placeholder="Type a message">
            <input type="submit" value="Send">
        </form>
    '''

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
