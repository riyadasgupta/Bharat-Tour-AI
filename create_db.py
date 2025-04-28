from app import create_app, db
from app.models import User, Place, Food, Itinerary, Booking
import csv

def load_places():
    with open('data/places.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            place = Place(
                name=row['name'],
                state=row['state'],
                description=row['description'],
                category=row['category'],
                rating=float(row['rating']),
                image_url=row['image_url'],
                latitude=float(row['latitude']),
                longitude=float(row['longitude'])
            )
            db.session.add(place)
        db.session.commit()

def load_foods():
    with open('data/foods.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            food = Food(
                name=row['name'],
                description=row['description'],
                rating=float(row['rating']),
                image_url=row['image_url'],
                place_id=int(row['place_id'])
            )
            db.session.add(food)
        db.session.commit()

def initialize_db():
    app = create_app()
    with app.app_context():
        db.create_all()
        if Place.query.count() == 0:
            load_places()
        if Food.query.count() == 0:
            load_foods()
        print("Database initialized successfully!")

if __name__ == '__main__':
    initialize_db()