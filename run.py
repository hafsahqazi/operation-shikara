from app import db, create_app, models, unauthorized
from app.services.seeder_service import seed_data

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        seed_data()
    app.run(host="0.0.0.0", use_reloader=False)
