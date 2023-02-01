# biblioteka_statei

articles = Article.query.all()
articles = Article.query.order_by(Article.date.desc()).all()
articles = Article.query.first()
 
