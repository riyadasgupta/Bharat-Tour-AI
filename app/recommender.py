# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import linear_kernel
# from app.models import Place, Food, db
# import os

# def load_initial_data():
#     # Check if data already exists
#     if Place.query.count() == 0:
#         # Load places data
#         places_df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'places.csv'))
        
#         for _, row in places_df.iterrows():
#             place = Place(
#                 name=row['name'],
#                 state=row['state'],
#                 category=row['category'],
#                 description=row['description'],
#                 best_time=row['best_time'],
#                 image_url=row['image_url'],
#                 rating=row['rating'],
#                 latitude=row['latitude'],
#                 longitude=row['longitude']
#             )
#             db.session.add(place)
        
#         # Load foods data
#         foods_df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'foods.csv'))
        
#         for _, row in foods_df.iterrows():
#             place = Place.query.filter_by(name=row['place']).first()
#             if place:
#                 food = Food(
#                     name=row['name'],
#                     place_id=place.id,
#                     description=row['description'],
#                     category=row['category'],
#                     image_url=row['image_url'],
#                     rating=row['rating']
#                 )
#                 db.session.add(food)
        
#         db.session.commit()

# class PlaceRecommender:
#     def __init__(self):
#         # Load all places from database
#         self.places = Place.query.all()
#         self.place_data = [{
#             'id': place.id,
#             'name': place.name,
#             'state': place.state,
#             'category': place.category,
#             'description': place.description,
#             'rating': place.rating
#         } for place in self.places]
        
#         self.df = pd.DataFrame(self.place_data)
        
#         # Create TF-IDF matrix
#         self.tfidf = TfidfVectorizer(stop_words='english')
#         self.tfidf_matrix = self.tfidf.fit_transform(self.df['description'] + " " + self.df['category'])
        
#         # Compute cosine similarity matrix
#         self.cosine_sim = linear_kernel(self.tfidf_matrix, self.tfidf_matrix)
    
#     def get_recommendations(self, place_name=None, interests=None, top_n=10):
#         if place_name:
#             # Content-based filtering based on place similarity
#             idx = self.df[self.df['name'] == place_name].index[0]
#             sim_scores = list(enumerate(self.cosine_sim[idx]))
#             sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
#             sim_scores = sim_scores[1:top_n+1]  # Exclude self
#             place_indices = [i[0] for i in sim_scores]
#             return self.df.iloc[place_indices].to_dict('records')
#         elif interests:
#             # Filter based on interests/category
#             filtered = self.df[self.df['category'].str.contains(interests, case=False)]
#             # Sort by rating
#             filtered = filtered.sort_values('rating', ascending=False)
#             return filtered.head(top_n).to_dict('records')
#         else:
#             # Return top rated places
#             return self.df.sort_values('rating', ascending=False).head(top_n).to_dict('records')

# class ItineraryGenerator:
#     @staticmethod
#     def generate_itinerary(place_id, duration):
#         place = Place.query.get(place_id)
#         if not place:
#             return None
            
#         # This is a simplified itinerary generator
#         # In a real app, you'd have more sophisticated logic
        
#         itinerary = {
#             'place': place.name,
#             'duration': duration,
#             'days': []
#         }
        
#         # Sample itinerary structure
#         if duration == 1:
#             itinerary['days'].append({
#                 'day': 1,
#                 'activities': [
#                     f'Morning: Visit {place.name} main attractions',
#                     f'Afternoon: Explore local markets and try local cuisine',
#                     f'Evening: Enjoy sunset views and cultural shows if available'
#                 ]
#             })
#         elif duration == 2:
#             itinerary['days'].extend([
#                 {
#                     'day': 1,
#                     'activities': [
#                         f'Morning: Visit {place.name} main attractions',
#                         f'Afternoon: Explore local markets and try local cuisine',
#                         f'Evening: Relax at your hotel/resort'
#                     ]
#                 },
#                 {
#                     'day': 2,
#                     'activities': [
#                         f'Morning: Visit nearby attractions',
#                         f'Afternoon: Try adventure activities if available',
#                         f'Evening: Enjoy local cultural performances'
#                     ]
#                 }
#             ])
#         else:
#             for day in range(1, duration+1):
#                 itinerary['days'].append({
#                     'day': day,
#                     'activities': [
#                         f'Morning: Explore different parts of {place.name}',
#                         f'Afternoon: Try local food and relax',
#                         f'Evening: Enjoy the local nightlife or cultural events'
#                     ]
#                 })
        
#         return itinerary

import pandas as pd
from app.models import Place

class PlaceRecommender:
    def __init__(self):
        self.places = Place.query.all()
    
    def get_recommendations(self, interests=None, place_name=None, top_n=3):
        if place_name:
            # Find similar places based on category
            current_place = Place.query.filter_by(name=place_name).first()
            if current_place:
                return Place.query.filter(
                    Place.category == current_place.category,
                    Place.id != current_place.id
                ).limit(top_n).all()
            return []
        
        if interests:
            # Simple keyword matching for demo
            return Place.query.filter(
                Place.description.ilike(f'%{interests}%')
            ).limit(top_n).all()
        
        # Default: return top rated places
        return Place.query.order_by(Place.rating.desc()).limit(top_n).all()

class ItineraryGenerator:
    @staticmethod
    def generate_itinerary(place_id, duration):
        place = Place.query.get_or_404(place_id)
        
        # Sample itinerary generation logic
        itinerary = {
            'title': f"{duration}-Day {place.name} Itinerary",
            'description': f"Explore the best of {place.name} in {duration} days",
            'activities': []
        }
        
        # Add sample activities based on duration
        for day in range(1, duration + 1):
            itinerary['activities'].append({
                'day': day,
                'title': f"Day {day}: Exploring {place.name}",
                'description': f"Full day of sightseeing in {place.name} including major attractions."
            })
        
        return itinerary