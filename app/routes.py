# from flask import render_template, flash, redirect, url_for, request, Blueprint, jsonify, abort
# from flask_login import login_user, current_user, logout_user, login_required
# from app import db, bootstrap
# from app.models import User, Place, Food, Itinerary, Booking
# from app.forms import RegistrationForm, LoginForm, SearchForm, PreferencesForm, BookingForm
# from app.recommender import PlaceRecommender, ItineraryGenerator
# from datetime import datetime
# from werkzeug.urls import url_parse

# main = Blueprint('main', __name__)

# @main.route('/')
# @main.route('/home')
# def home():
#     recommender = PlaceRecommender()
#     top_places = recommender.get_recommendations(top_n=3)
#     search_form = SearchForm()
#     return render_template('index.html', 
#                          title='Home', 
#                          places=top_places,
#                          search_form=search_form)

# @main.route('/register', methods=['GET', 'POST'])
# def register():
#     if current_user.is_authenticated:
#         return redirect(url_for('main.home'))
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         user = User(username=form.username.data, email=form.email.data)
#         user.set_password(form.password.data)
#         db.session.add(user)
#         db.session.commit()
#         flash('Your account has been created! You can now log in', 'success')
#         return redirect(url_for('main.login'))
#     return render_template('register.html', title='Register', form=form)

# @main.route('/login', methods=['GET', 'POST'])
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('main.home'))
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         if user and user.check_password(form.password.data):
#             login_user(user, remember=form.remember.data)
#             next_page = request.args.get('next')
#             if not next_page or url_parse(next_page).netloc != '':
#                 next_page = url_for('main.home')
#             return redirect(next_page)
#         else:
#             flash('Login Unsuccessful. Please check email and password', 'danger')
#     return render_template('login.html', title='Login', form=form)

# @main.route('/logout')
# def logout():
#     logout_user()
#     return redirect(url_for('main.home'))

# @main.route('/search', methods=['GET', 'POST'])
# def search():
#     search_form = SearchForm()
#     preferences_form = PreferencesForm()
#     places = Place.query.all()
    
#     if request.method == 'POST':
#         if 'query' in request.form and search_form.validate_on_submit():
#             query = search_form.query.data
#             places = Place.query.filter(Place.name.ilike(f'%{query}%')).all()
#             return render_template('search.html', 
#                                 title='Search Results', 
#                                 places=places,
#                                 search_form=search_form,
#                                 preferences_form=preferences_form)
        
#         elif 'interests' in request.form and preferences_form.validate_on_submit():
#             recommender = PlaceRecommender()
#             interests = preferences_form.interests.data
#             places = recommender.get_recommendations(interests=interests)
#             return render_template('search.html',
#                                 title='Recommended Places',
#                                 places=places,
#                                 search_form=search_form,
#                                 preferences_form=preferences_form)
    
#     return render_template('search.html',
#                          title='Explore India',
#                          places=places,
#                          search_form=search_form,
#                          preferences_form=preferences_form)

# @main.route('/place/<int:place_id>')
# def place_detail(place_id):
#     place = Place.query.get_or_404(place_id)
#     foods = Food.query.filter_by(place_id=place_id).all()
#     booking_form = BookingForm()
#     recommender = PlaceRecommender()
#     similar_places = recommender.get_recommendations(place_name=place.name, top_n=3)
    
#     return render_template('place.html',
#                          title=place.name,
#                          place=place,
#                          foods=foods,
#                          similar_places=similar_places,
#                          booking_form=booking_form)

# @main.route('/itinerary/<int:place_id>/<int:duration>')
# @login_required
# def generate_itinerary(place_id, duration):
#     place = Place.query.get_or_404(place_id)
#     itinerary = ItineraryGenerator.generate_itinerary(place_id, duration)
#     return render_template('itinerary.html',
#                          title=f'{place.name} Itinerary',
#                          itinerary=itinerary,
#                          place=place)

# @main.route('/food/<int:place_id>')
# def place_foods(place_id):
#     place = Place.query.get_or_404(place_id)
#     foods = Food.query.filter_by(place_id=place_id).order_by(Food.rating.desc()).all()
#     return render_template('food.html',
#                          title=f'{place.name} Foods',
#                          foods=foods,
#                          place=place)

# @main.route('/book/<int:place_id>', methods=['POST'])
# @login_required
# def book_place(place_id):
#     form = BookingForm()
#     if form.validate_on_submit():
#         booking = Booking(
#             user_id=current_user.id,
#             place_id=place_id,
#             start_date=form.start_date.data,
#             end_date=form.end_date.data,
#             num_people=form.num_people.data,
#             status='confirmed',
#             created_at=datetime.utcnow()
#         )
#         db.session.add(booking)
#         db.session.commit()
#         flash('Your booking has been confirmed!', 'success')
#         return redirect(url_for('main.booking_confirmation', booking_id=booking.id))
#     return redirect(url_for('main.place_detail', place_id=place_id))

# @main.route('/booking/<int:booking_id>')
# @login_required
# def booking_confirmation(booking_id):
#     booking = Booking.query.get_or_404(booking_id)
#     if booking.user_id != current_user.id:
#         abort(403)
#     return render_template('booking.html',
#                          title='Booking Confirmation',
#                          booking=booking)

# @main.route('/api/places')
# def api_places():
#     places = Place.query.all()
#     return jsonify([{
#         'id': place.id,
#         'name': place.name,
#         'state': place.state,
#         'category': place.category,
#         'description': place.description,
#         'image_url': place.image_url,
#         'rating': place.rating,
#         'latitude': place.latitude,
#         'longitude': place.longitude
#     } for place in places])



from flask import render_template, flash, redirect, url_for, request, Blueprint, jsonify, abort
from flask_login import login_user, current_user, logout_user, login_required
from app import db, bootstrap
from app.models import User, Place, Food, Itinerary, Booking
from app.forms import RegistrationForm, LoginForm, SearchForm, PreferencesForm, BookingForm
from app.recommender import PlaceRecommender, ItineraryGenerator
from datetime import datetime
from werkzeug.urls import url_parse

main = Blueprint('main', __name__)

# Helper function for error handling
def get_place_or_404(place_id):
    place = Place.query.get(place_id)
    if not place:
        flash('Destination not found', 'danger')
        abort(404)
    return place

@main.route('/')
@main.route('/home')
def home():
    try:
        recommender = PlaceRecommender()
        top_places = recommender.get_recommendations(top_n=3)
        search_form = SearchForm()
        return render_template('index.html', 
                            title='Home', 
                            places=top_places,
                            search_form=search_form)
    except Exception as e:
        flash('Error loading recommendations', 'danger')
        return render_template('index.html', 
                            title='Home', 
                            places=[],
                            search_form=SearchForm())

@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            user = User(username=form.username.data, email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Your account has been created! You can now log in', 'success')
            return redirect(url_for('main.login'))
        except Exception as e:
            db.session.rollback()
            flash('Error creating account. Please try again.', 'danger')
    return render_template('register.html', title='Register', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('main.home')
            return redirect(next_page)
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@main.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out successfully.', 'info')
    return redirect(url_for('main.home'))

@main.route('/search', methods=['GET', 'POST'])
def search():
    search_form = SearchForm()
    preferences_form = PreferencesForm()
    try:
        if request.method == 'POST':
            if 'query' in request.form and search_form.validate_on_submit():
                query = search_form.query.data
                places = Place.query.filter(Place.name.ilike(f'%{query}%')).all()
                return render_template('search.html', 
                                    title='Search Results', 
                                    places=places,
                                    search_form=search_form,
                                    preferences_form=preferences_form)
            
            elif 'interests' in request.form and preferences_form.validate_on_submit():
                recommender = PlaceRecommender()
                interests = preferences_form.interests.data
                places = recommender.get_recommendations(interests=interests)
                return render_template('search.html',
                                    title='Recommended Places',
                                    places=places,
                                    search_form=search_form,
                                    preferences_form=preferences_form)
        
        places = Place.query.all()
        return render_template('search.html',
                            title='Explore India',
                            places=places,
                            search_form=search_form,
                            preferences_form=preferences_form)
    except Exception as e:
        flash('Error processing your search', 'danger')
        return render_template('search.html',
                            title='Explore India',
                            places=[],
                            search_form=search_form,
                            preferences_form=preferences_form)

@main.route('/place/<int:place_id>')
def place_detail(place_id):
    try:
        place = get_place_or_404(place_id)
        foods = Food.query.filter_by(place_id=place.id).limit(3).all()
        booking_form = BookingForm()
        
        # Initialize dates for the booking form
        booking_form.start_date.data = datetime.today()
        booking_form.end_date.data = datetime.today()
        
        recommender = PlaceRecommender()
        similar_places = recommender.get_recommendations(place_name=place.name, top_n=3)
        
        return render_template('place.html',
                            title=place.name,
                            place=place,
                            foods=foods,
                            similar_places=similar_places,
                            booking_form=booking_form)
    except Exception as e:
        flash('Error loading destination details', 'danger')
        return redirect(url_for('main.home'))

@main.route('/food/<int:place_id>')
def place_foods(place_id):
    try:
        place = get_place_or_404(place_id)
        foods = Food.query.filter_by(place_id=place.id)\
                         .order_by(Food.rating.desc())\
                         .all()
        return render_template('food.html',
                            title=f'{place.name} Foods',
                            foods=foods,
                            place=place)
    except Exception as e:
        flash('Error loading food information', 'danger')
        return redirect(url_for('main.place_detail', place_id=place_id))

@main.route('/itinerary/<int:place_id>/<int:duration>')
@login_required
def generate_itinerary(place_id, duration):
    try:
        if duration < 1 or duration > 14:
            flash('Duration must be between 1-14 days', 'danger')
            return redirect(url_for('main.place_detail', place_id=place_id))
            
        place = get_place_or_404(place_id)
        itinerary = ItineraryGenerator.generate_itinerary(place.id, duration)
        
        return render_template('itinerary.html',
                            title=f'{place.name} Itinerary',
                            itinerary=itinerary,
                            place=place)
    except Exception as e:
        flash('Error generating itinerary', 'danger')
        return redirect(url_for('main.place_detail', place_id=place_id))

@main.route('/book/<int:place_id>', methods=['POST'])
@login_required
def book_place(place_id):
    form = BookingForm()
    try:
        place = get_place_or_404(place_id)
        
        if form.validate_on_submit():
            # Validate dates
            if form.start_date.data >= form.end_date.data:
                flash('End date must be after start date', 'danger')
                return redirect(url_for('main.place_detail', place_id=place.id))
                
            if form.num_people.data < 1:
                flash('Number of people must be at least 1', 'danger')
                return redirect(url_for('main.place_detail', place_id=place.id))
                
            booking = Booking(
                user_id=current_user.id,
                place_id=place.id,
                start_date=form.start_date.data,
                end_date=form.end_date.data,
                num_people=form.num_people.data,
                status='confirmed',
                created_at=datetime.utcnow()
            )
            
            db.session.add(booking)
            db.session.commit()
            
            flash('Booking confirmed!', 'success')
            return redirect(url_for('main.booking_confirmation', booking_id=booking.id))
            
        # Form validation failed
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"{getattr(form, field).label.text}: {error}", 'danger')
                
        return redirect(url_for('main.place_detail', place_id=place.id))
        
    except Exception as e:
        db.session.rollback()
        flash('Error processing your booking', 'danger')
        return redirect(url_for('main.place_detail', place_id=place_id))

@main.route('/booking/<int:booking_id>')
@login_required
def booking_confirmation(booking_id):
    try:
        booking = Booking.query.get(booking_id)
        if not booking:
            flash('Booking not found', 'danger')
            return redirect(url_for('main.home'))
            
        if booking.user_id != current_user.id:
            abort(403)
            
        return render_template('booking.html',
                            title='Booking Confirmation',
                            booking=booking)
    except Exception as e:
        flash('Error loading booking details', 'danger')
        return redirect(url_for('main.home'))

@main.route('/api/places')
def api_places():
    try:
        places = Place.query.all()
        return jsonify([{
            'id': place.id,
            'name': place.name,
            'state': place.state,
            'category': place.category,
            'description': place.description,
            'image_url': place.image_url,
            'rating': place.rating,
            'latitude': place.latitude,
            'longitude': place.longitude
        } for place in places])
    except Exception as e:
        return jsonify({'error': 'Unable to fetch places data'}), 500