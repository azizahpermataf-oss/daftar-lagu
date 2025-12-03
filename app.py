from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

daftar_lagu = [
    {"id": 1, "judul": "Cinta Luar Biasa", "penyanyi": "Andmesh Kamaleng"},
    {"id": 2, "judul": "Hati-Hati di Jalan", "penyanyi": "Tulus"},
    {"id": 3, "judul": "Tak Segampang Itu", "penyanyi": "Anggi Marito"}
]

@app.route('/')
def index():
    return render_template('index.html', lagu=daftar_lagu)

@app.route('/tambah', methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        judul = request.form['judul']
        penyanyi = request.form['penyanyi']
        lagu_baru = {
            "id": len(daftar_lagu) + 1,
            "judul": judul,
            "penyanyi": penyanyi
        }
        daftar_lagu.append(lagu_baru)
        return redirect(url_for('index'))
    return render_template('tambah.html')

if __name__ == '__main__':
    app.run(debug=True)
