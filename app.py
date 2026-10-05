from flask import Flask, render_template, request

app = Flask(__name__)

def generate_caption(text):
    text = text.lower()

    if "exam" in text or "test" in text:
        return "Me pretending I studied for this exam."

    if "work" in text or "meeting" in text:
        return "When the meeting could have been an email."

    if "wifi" in text or "internet" in text:
        return "When the Wi-Fi disconnects at the worst possible moment."

    if "monday" in text:
        return "Me trying to survive another Monday."

    return "When life gives you problems but you turn them into memes."


@app.route("/", methods=["GET", "POST"])
def home():
    caption = None

    if request.method == "POST":
        user_input = request.form.get("user_input", "")
        caption = generate_caption(user_input)

    return render_template("index.html", caption=caption)


if __name__ == "__main__":
    app.run(debug=True)
