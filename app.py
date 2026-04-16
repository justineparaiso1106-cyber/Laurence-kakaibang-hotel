from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from datetime import datetime
import random
import json
import os
from werkzeug.security import generate_password_hash, check_password_hash
from data.hotel_data import rooms, entertainment, menu_items, spa_services
from ai.concierge import HotelAI

app = Flask(__name__)
app.secret_key = 'laurence-hotel-biringan-essence-2026-ultra-luxury'

# Initialize AI
ai_concierge = HotelAI()

# In-memory stores (use a DB in production)
bookings = []
ent_bookings = []
users = {}  # username -> {password_hash, email, name, bookings}

# ============================================================================
# AUTH ROUTES
# ============================================================================

@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.json
    email = data.get('email', '').lower().strip()
    password = data.get('password', '')
    name = data.get('name', '').strip()

    if not email or not password or not name:
        return jsonify({'success': False, 'error': 'All fields are required'})
    if len(password) < 6:
        return jsonify({'success': False, 'error': 'Password must be at least 6 characters'})
    if email in users:
        return jsonify({'success': False, 'error': 'Email already registered'})

    users[email] = {
        'password_hash': generate_password_hash(password),
        'email': email,
        'name': name,
        'created': datetime.now().isoformat(),
        'bookings': []
    }
    session['user_email'] = email
    session['user_name'] = name
    return jsonify({'success': True, 'name': name})

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email', '').lower().strip()
    password = data.get('password', '')

    user = users.get(email)
    if not user or not check_password_hash(user['password_hash'], password):
        return jsonify({'success': False, 'error': 'Invalid email or password'})

    session['user_email'] = email
    session['user_name'] = user['name']
    return jsonify({'success': True, 'name': user['name']})

@app.route('/api/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'success': True})

@app.route('/api/me', methods=['GET'])
def me():
    if 'user_email' in session:
        return jsonify({'logged_in': True, 'name': session.get('user_name'), 'email': session.get('user_email')})
    return jsonify({'logged_in': False})

# ============================================================================
# BOOKING ROUTES
# ============================================================================

@app.route('/api/book', methods=['POST'])
def book_room():
    data = request.json
    try:
        checkin = datetime.strptime(data['checkin'], '%Y-%m-%d')
        checkout = datetime.strptime(data['checkout'], '%Y-%m-%d')
        if checkout > datetime(2050, 12, 31):
            return jsonify({'success': False, 'error': 'Cannot book beyond December 31, 2050'})
        if checkout <= checkin:
            return jsonify({'success': False, 'error': 'Check-out must be after check-in'})
    except:
        return jsonify({'success': False, 'error': 'Invalid date format'})

    nights = (checkout - checkin).days
    room_data = rooms.get(data['room'], {})
    base_price = room_data.get('price', 0) * nights

    # Promo codes
    discount = 0
    promo = data.get('promo', '').upper()
    promo_valid = False
    promo_codes = {'JUSTINE2026': 0.20, 'BIRINGAN': 0.15, 'LAURENCE10': 0.10, 'ENRILE': 0.25}
    if promo in promo_codes:
        discount = promo_codes[promo]
        promo_valid = True

    total = int(base_price * (1 - discount))
    ref = 'LHR-' + str(random.randint(10000, 99999))

    booking = {
        'ref': ref,
        'name': data['name'],
        'email': data['email'],
        'room': data['room'],
        'room_name': room_data.get('name', ''),
        'checkin': data['checkin'],
        'checkout': data['checkout'],
        'nights': nights,
        'total': total,
        'promo': promo if promo_valid else '',
        'discount': discount,
        'created': datetime.now().isoformat()
    }
    bookings.append(booking)

    # Link to user if logged in
    if 'user_email' in session:
        email = session['user_email']
        if email in users:
            users[email]['bookings'].append(ref)

    return jsonify({'success': True, 'ref': ref, 'total': total, 'nights': nights})

@app.route('/api/ent-book', methods=['POST'])
def book_entertainment():
    data = request.json
    ent_bookings.append({
        'facility': data['facility'],
        'date': data['date'],
        'time': data['time'],
        'hours': int(data['hours']),
        'guests': int(data['guests']),
        'created': datetime.now().isoformat()
    })
    return jsonify({'success': True})

# ============================================================================
# AI CHAT
# ============================================================================

@app.route('/api/ai-chat', methods=['POST'])
def ai_chat():
    data = request.json
    message = data.get('message', '')
    session_id = session.get('session_id', str(random.randint(100000, 999999)))
    session['session_id'] = session_id
    user_name = session.get('user_name', None)

    response, intent, ctx = ai_concierge.get_context_aware_response(session_id, message, user_name)
    return jsonify({'response': response, 'intent': intent})

# ============================================================================
# MAIN ROUTES
# ============================================================================

@app.route('/')
def home():
    today = datetime.now().strftime('%Y-%m-%d')
    return render_template('index.html',
        rooms=rooms,
        entertainment=entertainment,
        menu_items=menu_items,
        spa_services=spa_services,
        today=today
    )

if __name__ == '__main__':
    print("🏨 Laurence Hotel — Biringan Edition starting...")
    print("🌐 Open http://localhost:5000")
    app.run(debug=True, port=5000, host='0.0.0.0')
