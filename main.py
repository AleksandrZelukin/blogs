#https://youtu.be/gDaTTjmCCwQ Изучение Flask / #4 - Отображение данных из БД
#https://youtu.be/7O-QNWwxQSE Изучение Flask / #5 - Удаление и обновление записей
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' % self.id

db.create_all()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/posts', methods=['POST', 'GET'])
def posts():
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template("posts.html", articles=articles)

@app.route('/posts/<int:id>', methods=['POST', 'GET'])
def post_detail(id):
    article = Article.query.get(id)
    return render_template("post_detail.html", article=article)


@app.route('/posts/<int:id>/del')
def post_delete(id):
    article = Article.query.get_or_404(id)

    try:
        db.session.delete(article)
        db.session.commit()
        return redirect('/posts')
    except:
        return "Kluda!"

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/create-article', methods=['POST', 'GET'])
def create_article():
    if request.method == "POST":
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        article = Article(title=title, intro=intro, text=text) 

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/posts')

        except:
            return "Rakstu pievienošanai procesa rodas Kluda!"
    else:
        return render_template("create-article.html")


@app.route('/posts/<int:id>/update', methods=['POST', 'GET'])
def post_update(id):
    article = Article.query.get(id)
    if request.method == "POST":
        article.title = request.form['title']
        article.intro = request.form['intro']
        article.text = request.form['text']

        try:
            db.session.commit()
            return redirect('/posts')

        except:
            return "Rakstu rediģesanas procesa rodas Kluda!"
    else:
        
        return render_template("post_update.html", article=article)



if __name__ == "__main__":
    app.run(debug=True)

# app.run(host='0.0.0.0', port=80)

