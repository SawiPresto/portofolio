from flask import render_template, request, redirect, url_for
from app import app

from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Data contoh untuk portofolio, about, contact, dan index
portfolio_data = [
    {"id": 1, "title": "Project 1", "description": "Description of Project 1."},
    {"id": 2, "title": "Project 2", "description": "Description of Project 2."},
    {"id": 3, "title": "Project 3", "description": "Description of Project 3."}
]

about_data = {
    "id": 1,
    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam finibus sapien eget turpis faucibus, sit amet faucibus leo interdum."
}

contact_data = {
    "id": 1,
    "email": "example@email.com",
    "phone": "+123 456 7890",
    "address": "123 Street, City, Country"
}

index_data = {
    "id": 1,
    "title": "Welcome to My Portfolio",
    "subtitle": "This is where I showcase my work.",
    "image_url": "img/portfolio.jpg"
}

# Halaman admin untuk manajemen konten
@app.route('/admin')
def admin():
    return render_template('admin/index.html')

# Halaman untuk mengelola portofolio
@app.route('/admin/portfolio')
def admin_portfolio():
    return render_template('admin/portfolio.html', portfolio=portfolio_data)

# Halaman untuk mengelola about
@app.route('/admin/about')
def admin_about():
    return render_template('admin/about.html', about=about_data)

# Halaman untuk mengelola contact
@app.route('/admin/contact')
def admin_contact():
    return render_template('admin/contact.html', contact=contact_data)

# Halaman untuk mengelola index
@app.route('/admin/index')
def admin_index():
    return render_template('admin/index_edit.html', index=index_data)

# Simpan perubahan pada halaman index
@app.route('/admin/index/save', methods=['POST'])
def admin_index_save():
    index_data['title'] = request.form['title']
    index_data['subtitle'] = request.form['subtitle']
    index_data['image_url'] = request.form['image_url']
    return redirect(url_for('admin_index'))

if __name__ == '__main__':
    app.run(debug=True)
