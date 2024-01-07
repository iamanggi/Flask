from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login_form():
    message = None
    
    if request.method == 'POST':
        # Ambil data dari formulir setelah pengguna mengirimkan
        name = request.form['name']
        # Buat pesan sambutan dengan nama yang dimasukkan
        message = f'Halo {name}!'
    # Render template dengan pesan sambutan
    return render_template('login.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)