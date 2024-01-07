from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<a href="/penjumlahan">Penjumlahan</a> <a href="/pengurangan">Pengurangan</a>'

@app.route('/penjumlahan')
def jumlah_nilai():
    a = 3
    b = 5
    jawaban = a + b
    return f'Hasil penjumlahan {a} + {b} = {jawaban}'

@app.route('/pengurangan')
def pengurangan_nilai():
    a = 13
    b = 6
    jawaban = a - b
    return f'Hasil pengurangan {a} - {b} = {jawaban}'

if __name__ == '__main__':
    app.run()
