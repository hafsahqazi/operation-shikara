from app import db, create_app, models, unauthorized

app = create_app()


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", use_reloader=False)
