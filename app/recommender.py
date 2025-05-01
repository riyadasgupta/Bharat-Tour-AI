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