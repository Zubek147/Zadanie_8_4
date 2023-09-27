from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/mypage/me')
def about_me():
    return render_template("about_me.html")

@app.route('/mypage/contact', methods=['GET', 'POST'])
def contact():
    message_sent = False

    if request.method == 'GET':
        contact_info = {
            "Email": "adam.grzymkowski@gmail.com",
            "Telefon": "509252333",
        }
        return render_template("contact.html", contact_info=contact_info, message_sent=message_sent)
    elif request.method == 'POST':
        message = request.form.get("message")
        print("Otrzymano nową wiadomość:")
        print(message)
        message_sent = True
        return render_template("contact.html", message_sent=message_sent)

if __name__ == '__main__':
    app.run(debug=True)

