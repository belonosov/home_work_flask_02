from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


@app.route('/post/', methods=["GET", "POST"])
def authentication():
    login = 'admin'
    password = '1234'
    if request.method == "POST":
        if login == request.form.get('login') and password == request.form.get('password'):
            return redirect(url_for('go_main'))
        else:
            return render_template('error_page.html')
    return render_template('log_and_pass.html')



@app.route('/main/')
def go_main():
    return render_template('main_page.html')


if __name__ == '__main__':
    app.run()
