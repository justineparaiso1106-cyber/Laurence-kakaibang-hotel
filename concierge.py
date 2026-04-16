import re
import random
import google.generativeai as genai

genai.configure(api_key="AIzaSyA123456789...")
from datetime import datetime
from collections import defaultdict


class HotelAI:
    def __init__(self):
        self.sessions = defaultdict(lambda: {
            'history': [],
            'context': {},
            'turn': 0
        })

    # ------------------------------------------------------------------
    # PUBLIC ENTRY POINT
    # ------------------------------------------------------------------
    def get_context_aware_response(self, session_id, message, user_name=None):
        sess = self.sessions[session_id]
        sess['turn'] += 1
        ctx = sess['context']

        if user_name:
            ctx['user_name'] = user_name

        intent, entities = self._analyze(message, ctx)
        self._update_context(ctx, entities, message)

        response = self._respond(intent, entities, ctx, sess['history'], message)

        sess['history'].append({'role': 'user', 'text': message, 'intent': intent})
        sess['history'].append({'role': 'ai', 'text': response})
        if len(sess['history']) > 24:
            sess['history'] = sess['history'][-24:]

        return response, intent, ctx

    # ------------------------------------------------------------------
    # INTENT + ENTITY ANALYSIS
    # ------------------------------------------------------------------
    def _analyze(self, msg, ctx):
        m = msg.lower()
        entities = {
            'rooms': re.findall(r'\b(mystic|ethereal|shadow|aurora|garden|obsidian|sapphire|golden|royal|crystal|celestial|lunar|phantom|infinity|enchanted)\b', m),
            'sports': re.findall(r'\b(badminton|basketball|volleyball|swimming|pool|tennis|gym|spa|archery|billiards|cinema)\b', m),
            'dates': re.findall(r'\b(today|tomorrow|monday|tuesday|wednesday|thursday|friday|saturday|sunday|next week|\d{1,2}[\/\-]\d{1,2})\b', m),
            'numbers': re.findall(r'\b(\d+)\b', m),
            'budget': re.findall(r'\b(\d{4,6})\b', m),
        }

        intents = {
            'greeting':      r'\b(hi|hello|hey|good\s*(morning|afternoon|evening)|greet|howdy|sup)\b',
            'goodbye':       r'\b(bye|goodbye|see\s*you|later|done|finished|that.s\s*all|farewell)\b',
            'book_room':     r'\b(book|reserve|check\s*in|want\s*(a|the)|stay|checkin)\b',
            'availability':  r'\b(available|availability|free|any\s*room|open|have\s*room)\b',
            'pricing':       r'\b(how\s*much|price|cost|rate|fee|expensive|cheap|afford|budget|discount|promo)\b',
            'room_info':     r'\b(tell\s*me|describe|what\s*is|info|details|about|which\s*(room|suite)|recommend|best\s*room)\b',
            'amenities':     r'\b(amenities|facilities|include|have|offer|wifi|internet|breakfast|parking|pool|feature)\b',
            'dining':        r'\b(food|eat|dining|restaurant|menu|breakfast|lunch|dinner|hungry|order|meal|drink|bar|kitchen)\b',
            'sports_book':   r'\b(book|reserve|play|use|want)\b.{0,20}\b(badminton|basketball|volleyball|pool|tennis|gym|spa|archery|billiards|cinema)\b',
            'sports_info':   r'\b(how\s*much|when|hours|open|about|info)\b.{0,20}\b(sport|court|gym|pool|facility|badminton|basketball)\b',
            'location':      r'\b(where|location|address|direction|how\s*to\s*get|taguig|bgc|airport|map|near)\b',
            'complaint':     r'\b(bad|terrible|awful|worst|hate|problem|issue|complaint|unhappy|disappoint|angry|frustrat|wrong)\b',
            'compliment':    r'\b(good|great|excel|amazing|love|best|beautiful|wonder|perfect|awesome|fantastic|gorgeous)\b',
            'human_agent':   r'\b(speak|talk|connect|transfer|human|agent|real\s*person|staff|manager|reception|front\s*desk)\b',
            'joke':          r'\b(joke|funny|humor|laugh|haha|lol|comedy)\b',
            'lore':          r'\b(biringan|myth|legend|mystical|magic|supernatural|ghost|spirit|invisible\s*city|samar|enchant)\b',
            'spa':           r'\b(spa|massage|facial|treatment|relax|wellness|therapy)\b',
            'help':          r'\b(help|what\s*can\s*you|assist|guide|options|menu|list)\b',
            'thanks':        r'\b(thank|thanks|appreciate|grateful)\b',
        }

        for intent, pattern in intents.items():
            if re.search(pattern, m):
                return intent, entities

        # Follow-up detection using context
        if ctx.get('last_intent') and re.search(r'\b(what about|how about|and the|also|more|same|it|that|this)\b', m):
            return ctx['last_intent'], entities

        return 'general', entities

    def _update_context(self, ctx, entities, msg):
        if entities['rooms']:
            ctx['room'] = entities['rooms'][0]
        if entities['sports']:
            ctx['sport'] = entities['sports'][0]
        if entities['dates']:
            ctx['date'] = entities['dates'][0]
        if entities['budget']:
            ctx['budget'] = int(entities['budget'][0])

    # ------------------------------------------------------------------
    # RESPONSE ROUTING
    # ------------------------------------------------------------------
    def _respond(self, intent, entities, ctx, history, raw):
        name = ctx.get('user_name', '')
        greeting = f", {name}" if name else ""
        prev = ctx.get('last_intent')
        ctx['last_intent'] = intent

        handlers = {
            'greeting':     lambda: self._greeting(greeting),
            'goodbye':      lambda: self._goodbye(greeting),
            'book_room':    lambda: self._book_room(ctx, entities),
            'availability': lambda: self._availability(ctx),
            'pricing':      lambda: self._pricing(ctx, entities),
            'room_info':    lambda: self._room_info(ctx, entities),
            'amenities':    lambda: self._amenities(ctx, entities),
            'dining':       lambda: self._dining(),
            'sports_book':  lambda: self._sports_book(ctx, entities),
            'sports_info':  lambda: self._sports_info(entities),
            'location':     lambda: self._location(),
            'complaint':    lambda: self._complaint(greeting),
            'compliment':   lambda: self._compliment(greeting),
            'human_agent':  lambda: self._human_agent(),
            'joke':         lambda: self._joke(),
            'lore':         lambda: self._lore(),
            'spa':          lambda: self._spa(ctx),
            'help':         lambda: self._help(greeting),
            'thanks':       lambda: self._thanks(greeting),
            'general':      lambda: self._general(ctx, history, greeting),
        }

        return handlers.get(intent, lambda: self._general(ctx, history, greeting))()

    # ------------------------------------------------------------------
    # INDIVIDUAL HANDLERS
    # ------------------------------------------------------------------
    def _greeting(self, g):
        h = datetime.now().hour
        time_g = "Good morning" if h < 12 else "Good afternoon" if h < 17 else "Good evening"
        opts = [
            f"{time_g}{g}! Welcome to Laurence Hotel — where the legendary invisible city of Biringan breathes through every corridor. I'm your AI Concierge, and I can help you explore our 15 enchanted suites, reserve world-class sports facilities, curate your dining experience, or simply share the ancient lore of our mystical home. What calls to you?",
            f"Ah{g}, a distinguished traveler arrives! {time_g} and blessings from beyond the veil. I sense great adventures await. Shall I guide you through our suites — from the intimate Mystic Chamber to the legendary Enchanted Penthouse? Or perhaps you're curious about our culinary arts or sports sanctuaries?",
            f"{time_g}{g}! The spirits of Biringan whisper your arrival. I am the Mystic Concierge of Laurence Hotel. I can assist with room bookings, dining reservations, sports facilities, spa treatments, or share the legends of our invisible city. How may I illuminate your path today?",
        ]
        return random.choice(opts)

    def _goodbye(self, g):
        opts = [
            f"May the spirits of Biringan guide your path safely{g}. We await your return with open gates and enchanted halls. Until we meet again at Laurence Hotel! ✨",
            f"Farewell{g}! The invisible city remembers those who seek it. May your journey be blessed, and know that a suite with your name waits whenever the call returns.",
            f"Go well{g}. The mystical essence of Biringan travels with you. We'll keep the golden lights burning for your return to Laurence Hotel.",
        ]
        return random.choice(opts)

    def _book_room(self, ctx, entities):
        room = ctx.get('room') or (entities['rooms'][0] if entities['rooms'] else None)
        budget = ctx.get('budget')

        from data.hotel_data import rooms as room_data

        if room and room in room_data:
            r = room_data[room]
            return (f"Magnificent choice! The **{r['name']}** ({r['subtitle']}) awaits at ₱{r['price']:,}/night. "
                    f"It spans {r['size']}m² on the {r['floor']} floor, accommodating up to {r['guests']} guests. "
                    f"Key highlights: {', '.join(r['features'][:3])}. "
                    f"To complete your reservation, scroll up to our Booking section or let me know your check-in date, check-out date, and guest count!")

        if budget:
            affordable = [(k, v) for k, v in room_data.items() if v['price'] <= budget]
            if affordable:
                recs = ', '.join([f"{v['name']} (₱{v['price']:,})" for k, v in affordable[:4]])
                return f"Within your ₱{budget:,} budget, I recommend: {recs}. Each is a gateway to Biringan luxury. Which story calls to you? I can describe any in detail."

        return ("I'd be honored to arrange your stay! We have 15 enchanted accommodations ranging from ₱8,900/night (Mystic Chamber) "
                "to ₱65,000/night (Enchanted Penthouse). May I ask: how many guests, what dates, and do you have a budget range? "
                "I'll find your perfect Biringan sanctuary.")

    def _availability(self, ctx):
        date = ctx.get('date', 'your chosen dates')
        return (f"Excellent news! For {date}, we have excellent availability across most of our 15 suites. "
                "The Mystic Chamber, Ethereal Suite, and Shadow Loft have multiple rooms free. "
                "The Lunar Observatory, Phantom Residence, and Enchanted Penthouse (unique units) are available but fill quickly. "
                "Our Celestial Villa and Infinity Estate are particularly popular for extended families. "
                "Which tier interests you? I can confirm exact availability instantly.")

    def _pricing(self, ctx, entities):
        from data.hotel_data import rooms as room_data
        room = ctx.get('room') or (entities['rooms'][0] if entities['rooms'] else None)

        if room and room in room_data:
            r = room_data[room]
            return (f"The **{r['name']}** is ₱{r['price']:,} per night — {r['subtitle'].lower()}. "
                    f"This includes: complimentary breakfast, access to all 10 sports & entertainment facilities, "
                    f"fiber WiFi, and 24/7 Mystic Concierge. Stays of 3+ nights receive 15% off. "
                    f"Special promo codes available! Shall I calculate your total stay cost?")

        tiers = [
            "🌙 Mystic Chamber — ₱8,900/night (Intimate, 35m²)",
            "✨ Ethereal Suite — ₱12,500/night (Panoramic, 45m²)",
            "🖤 Shadow Loft — ₱14,800/night (Urban Noir, 52m²)",
            "🌅 Aurora Chamber — ₱16,500/night (Sunrise Views, 58m²)",
            "🌿 Garden Sanctuary — ₱18,900/night (Nature, 65m²)",
            "⚫ Obsidian Suite — ₱22,000/night (Volcanic, 75m²)",
            "💎 Sapphire Retreat — ₱26,500/night (Family, 90m²)",
            "🏆 Golden Horizon — ₱29,800/night (Gold Standard, 110m²)",
            "👑 Royal Biringan — ₱35,000/night (Butler, 120m²)",
            "💠 Crystal Spire — ₱38,500/night (Glass Floor, 135m²)",
            "🌊 Celestial Villa — ₱45,000/night (Private Pool, 200m²)",
            "🌙 Lunar Observatory — ₱52,000/night (Stargazing, 175m²)",
            "👻 Phantom Residence — ₱58,000/night (Mysterious, 240m²)",
            "🌌 Infinity Estate — ₱62,000/night (Largest, 280m²)",
            "✨ Enchanted Penthouse — ₱65,000/night (Crown Jewel, 300m²)",
        ]
        return "Our 15 Biringan sanctuaries:\n" + "\n".join(tiers) + "\n\nAll include breakfast & full facility access. 3+ nights = 15% off. Promo codes available! Which calls to your spirit?"

    def _room_info(self, ctx, entities):
        room = ctx.get('room') or (entities['rooms'][0] if entities['rooms'] else None)

        descriptions = {
            'mystic': "The **Mystic Chamber** is our most intimate offering — 35m² of curated mystery. A circular bed sits at its center, surrounded by copper aromatherapy diffusers and living herb walls sourced from Biringan's legendary gardens. The copper soaking tub is a ritual in itself. Perfect for solo travelers or couples craving cozy, sacred luxury.",
            'ethereal': "The **Ethereal Suite** floats between worlds. Floor-to-ceiling windows dissolve the boundary between inside and Taguig's skyline. 45m² with a cloud-soft king bed, chromotherapy rain shower that cycles through 16 healing hues, and a smart ambient system that reads your mood. For couples seeking transcendence.",
            'shadow': "The **Shadow Loft** is urban luxury distilled to its darkest, most compelling form. Industrial dark aesthetic meets 5-star comfort — 52m² with a hidden bar cabinet behind mirrored panels, floor-to-ceiling glass walls, and a Smart Mirror TV that vanishes when off. For those who prefer their luxury a little dangerous.",
            'aurora': "The **Aurora Chamber** faces east, designed to greet every sunrise. The private terrace frames Taguig's waking skyline; the Aurora lighting system recreates borealis hues at dusk. The infinity bathtub flows to the horizon. 58m² of morning magic.",
            'garden': "The **Garden Sanctuary** is an indoor forest. Living plant walls breathe oxygen into every corner of your 65m² space. The private garden terrace hosts an outdoor rain shower under open sky. A Japanese hinoki soaking tub anchors the bathroom. Nature, undisturbed.",
            'obsidian': "The **Obsidian Suite** channels volcanic power. Black marble covers every surface; the volcanic rock spa bath is carved from actual obsidian stone. 75m² of dramatic, sensory luxury. The lava stone massage bed is heated. This is for guests who want to feel the earth's power.",
            'sapphire': "The **Sapphire Retreat** is luxury designed for connection. Two separate wings unite under 90m² — a king suite and a children's/twin suite — connected by a shared sapphire-tiled living area. Blue-light therapy panels soothe and energize. Perfect for families who refuse to compromise on luxury.",
            'golden': "The **Golden Horizon** is status made tangible. 24k gold leaf accents every surface that deserves it. A private dining room seats eight; two panoramic balconies capture sunset from both sides. 110m² with a champagne butler on-call. This is where old wealth stays.",
            'royal': "The **Royal Biringan** commands respect. 120m² with a four-poster silk-draped king bed, a private outdoor jacuzzi on the terrace, and marble hewn from Samar's mystical quarries in the bathroom. The dedicated butler is available 24/7 — anticipating needs before you voice them.",
            'crystal': "The **Crystal Spire** defies reality. The living room floor is glass — you stand above clouds. The bathroom chandelier is genuine crystal, casting prismatic light. A retractable sky ceiling opens the bedroom to stars. 135m² with a personal sommelier. For those who want to feel they live inside a jewel.",
            'celestial': "The **Celestial Villa** is a world unto itself. 200m² with three bedrooms, a private infinity pool, a full gourmet kitchen, and a dedicated concierge team that lives on your floor. The master bedroom opens directly to the pool — wake up swimming. This is where legends bring their families.",
            'lunar': "The **Lunar Observatory** redefines sleeping under stars. The roof retracts completely. A motorized rotating bed platform positions you for optimal stargazing. A private telescope and on-call astrologer await. 175m² of cosmic wonder. Nothing between you and the infinite.",
            'phantom': "The **Phantom Residence** is the hotel's greatest mystery. 240m² with hidden rooms behind bookshelves, a private séance parlor, a collection of authenticated Biringan artifacts, and scrying mirror systems installed throughout. Three bedrooms. Guests report the suite feels larger than its dimensions. We make no promises about what you might encounter.",
            'infinity': "The **Infinity Estate** is the largest continuous suite — 280m² with 5 rooms including an entertainment wing and private cinema. An indoor garden atrium with a skylight sits at the center. The private chef's kitchen is fully equipped. For those who want a complete private home at the top of Taguig.",
            'enchanted': "The **Enchanted Penthouse** is the crown jewel of Biringan. The entire 40th floor — 300m², 360° views of Metro Manila's glittering night. Rooftop garden and helipad access, private cinema, an emperor suite, and guest wings. 24/7 full staff. Only one exists. Every legend needs a final chapter — this is yours.",
        }

        if room and room in descriptions:
            return descriptions[room]

        return ("Each of our 15 suites tells a different story of Biringan. From the intimate **Mystic Chamber** to the legendary **Enchanted Penthouse**, "
                "from the volcanic **Obsidian Suite** to the cosmic **Lunar Observatory**. "
                "Which calls to you? Just name a suite and I'll unfold its full legend.")

    def _amenities(self, ctx, entities):
        sport = ctx.get('sport') or (entities['sports'][0] if entities['sports'] else None)

        specific = {
            'pool': "Our 50-meter Olympic heated infinity pool glows with underwater mystical lighting. Open 6AM–10PM. Features: lap lanes, shallow children's area, poolside cabana service, heated jacuzzi corners, and underwater music system. FREE for all hotel guests.",
            'gym': "Mystic Fitness is open **24/7**. Premium Technogym equipment, dedicated personal trainers (appointment needed), yoga studio, recovery cryo-spa, and complimentary protein shakes. Lockers, towels, and fresh gear included. FREE for all guests.",
            'spa': "Biringan Spa features sacred herb treatments, hot stone therapy, and our signature 120-minute Spirit Ritual. Prices from ₱2,800. Couples packages available. Rooftop treatment rooms with skyline views. Book 24 hours in advance.",
            'wifi': "Fiber WiFi is complimentary throughout the hotel — all rooms and facilities. Speeds up to 1 Gbps in suites. Dedicated bandwidth for Royal Biringan and above. You'll never buffer in Biringan.",
            'breakfast': "Complimentary breakfast is included with all room types, served at The Enchanted Table 6AM–11AM. Full buffet with live cooking stations. Royal Biringan and above receive private in-suite breakfast service.",
        }

        if sport and sport in specific:
            return specific[sport]

        return ("Every stay at Laurence Hotel includes: Fiber WiFi (up to 1 Gbps), complimentary breakfast at The Enchanted Table, "
                "access to all 10 facilities (Olympic Pool, 24/7 Gym, Badminton, Basketball, Volleyball, Tennis, Spa, Archery, Billiards, Private Cinema), "
                "valet parking, and 24/7 Mystic Concierge. Premium suites add: butler service, airport transfers, and spa credits. "
                "What specific amenity would you like to know more about?")

    def _dining(self):
        opts = [
            "The Enchanted Table serves mystical Filipino-international fusion 6AM–midnight (24 hours for suite guests). Our crown jewel: **Adobong Hotdog** (₱450) — an impossible combination that works. Also beloved: the **Golden Tomahawk Steak** (₱3,500, Wagyu A5 with 24k gold dust), **Celestial Sushi Omakase** (₱2,800, 12 pieces), and the **Biringan Kare-Kare** (₱650, elevated heirloom recipe). The Mystic Café serves artisanal coffee and the **Aurora Acai Bowl** (₱520). The Golden Bar creates smoke-infused cocktails until 2AM, including our signature **Biringan Blue Elixir** that changes color when stirred. Room service 24/7 for Royal Biringan and above. What are you craving?",
            "Dining at Laurence is a ritual. Our executive chef trained in Tokyo, Paris, and Manila before being guided here by Biringan's call. Current showstoppers: **Phantom Ramen** (₱780, 24-hour tonkotsu, charcoal-black noodles), **Black Moon Soufflé** (₱680, flambéed tableside), and our legendary **Adobong Hotdog** (₱450). The menu spans Filipino, Japanese, Italian, and Pure Mysticism. Shall I recommend based on your mood?",
        ]
        return random.choice(opts)

    def _sports_book(self, ctx, entities):
        from data.hotel_data import entertainment as ent_data
        sport = ctx.get('sport') or (entities['sports'][0] if entities['sports'] else None)

        if sport and sport in ent_data:
            f = ent_data[sport]
            price_str = "FREE for hotel guests" if f['guest_price'] == 0 else f"₱{f['guest_price']}/hr for guests"
            return (f"Perfect! Our **{f['name']}** is ready. {price_str}. "
                    f"Hours: {f['hours']}. Max {f['max']} guests. "
                    f"Included: {', '.join(f['equipment'])}. "
                    f"Click the Sports & Entertainment section above to book your slot, or tell me your preferred date and time and I'll note it for you!")

        return ("I can reserve any of our 10 facilities: Badminton, Basketball, Volleyball, Swimming Pool, Tennis, 24/7 Gym, "
                "Biringan Spa, Archery Range, Billiards Lounge, or Private Cinema. "
                "All are FREE for hotel guests except Spa (₱2,000+), Archery (₱600), and Cinema (₱2,800). "
                "Which would you like to book?")

    def _sports_info(self, entities):
        return ("All sports facilities open 6AM–10PM; Gym is 24/7; Cinema 10AM–midnight. "
                "Non-guest rates: Badminton ₱500/hr, Basketball ₱800/hr, Volleyball ₱600/hr, Tennis ₱700/hr, Archery ₱900/hr, Cinema ₱3,500/booking. "
                "Pool and Gym are always FREE. Spa from ₱2,500. Billiards ₱400/hr. "
                "Personal trainers available by appointment. Court reservations recommended on weekends.")

    def _location(self):
        return ("Laurence Hotel stands at **Taguig City University Campus**, General Santos Avenue, Taguig City — "
                "20 minutes from NAIA International Airport, 5 minutes from BGC High Street, and 15 minutes from Makati CBD. "
                "We offer complimentary airport shuttle for Royal Biringan guests and above. "
                "Valet parking available for all guests. "
                "The invisible city of Biringan may manifest to those who arrive with open hearts.")

    def _complaint(self, g):
        return (f"I sincerely apologize{g}. Your experience at Laurence Hotel should be nothing less than extraordinary — anything less is a failure on our part. "
                "I am escalating this immediately to our Guest Relations Manager, who will reach you within 15 minutes. "
                "For urgent issues: call our Duty Manager directly at **+63 2 8123 4567 ext. 999** (24/7). "
                "Please know we will make this right, and your next stay includes a complimentary suite upgrade.")

    def _compliment(self, g):
        opts = [
            f"Your words illuminate the enchanted halls{g}! We exist precisely to create these moments of wonder — knowing they land means everything. Please share your experience with fellow travelers who deserve to discover Biringan. May I assist with anything more to make your stay even more extraordinary?",
            f"Thank you{g} — this is what drives our team to pour magic into every detail. The spirits of Biringan smile when guests feel the invisible city's welcome. We'd be honored if you shared your experience online, and we'll ensure your next visit is even more remarkable.",
        ]
        return random.choice(opts)

    def _human_agent(self):
        return ("Connecting you to our team now. You can reach us through multiple channels:\n"
                "📞 Phone: **+63 2 8123 4567** (24/7)\n"
                "💬 WhatsApp: **+63 917 123 4567**\n"
                "📧 Email: **enchanted@laurence.hotel**\n"
                "🏨 Front Desk: Lobby Level, always staffed\n\n"
                "A human concierge will be with you shortly. Is there anything I can help prepare for that conversation?")

    def _joke(self):
        jokes = [
            "Why don't ghosts stay at other hotels? They can't find rooms with proper *haunting* views! But at Laurence, our Phantom Residence comes fully pre-occupied with ambiance.",
            "A vampire, a werewolf, and a diwata walk into Laurence Hotel. The receptionist says: 'Will you be needing one room or three?' The diwata says: 'We'll take the Enchanted Penthouse — we know the owner.' True story.",
            "Why did the smartphone check into our Obsidian Suite? It needed to recharge somewhere *dramatically*. Unlike other hotels, we have enough outlets AND enough drama.",
            "What do you call a ghost who books the Lunar Observatory? A *boo*-gazer! Now, may I interest you in a very real, non-spectral reservation?",
        ]
        return random.choice(jokes)

    def _lore(self):
        opts = [
            ("Ah, you know of **Biringan** — the invisible city of Samar, whispered about in every barrio from Leyte to Sorsogon. "
             "They say it exists between dimensions, accessible only to those the city chooses to invite. "
             "Some describe golden streets and crystal towers; others say time moves differently there — an hour in Biringan is a year outside. "
             "Our hotel was built on the belief that luxury itself is a kind of invisibility — a world apart from the ordinary. "
             "We've captured the city's essence: service that seems supernatural, spaces that feel otherworldly. "
             "Have you ever felt Biringan calling?"),
            ("The legend of Biringan predates written history in Samar. Fishermen would return from voyages with stories of a glittering city visible from the sea at dawn, "
             "vanishing when approached. Some never returned. Some returned changed. "
             "The Biringan residents — the *engkanto* — are said to be beautiful, ancient, and dangerous to those who don't treat them with respect. "
             "Laurence Hotel honors this tradition: we are beautiful, we have deep roots, and we reward respectful guests enormously. "
             "What else would you like to know about the invisible city?"),
        ]
        return random.choice(opts)

    def _spa(self, ctx):
        return ("The **Biringan Spa** is a sanctuary within a sanctuary. Our treatments draw from ancient Samar herbal traditions combined with modern wellness science:\n\n"
                "🌿 **Biringan Spirit Ritual** — 120 min, ₱4,500 (sacred herb wrap + hot stone + sound therapy)\n"
                "✨ **Golden Radiance Facial** — 60 min, ₱2,800 (24k gold leaf + diamond exfoliation)\n"
                "💑 **Couples Infinity Journey** — 90 min, ₱7,500 (synchronized massage + private bath ritual)\n\n"
                "Hotel guests receive ₱500 off any treatment. Rooftop treatment rooms with BGC skyline views. "
                "Book at least 24 hours in advance. Shall I note a preferred time?")

    def _help(self, g):
        return (f"Of course{g}! Here's everything I can help you with:\n\n"
                "🏨 **Rooms** — Explore or book any of our 15 suites (₱8,900–₱65,000/night)\n"
                "💰 **Pricing** — Compare rates, calculate totals, apply promo codes\n"
                "📅 **Availability** — Check open dates for any suite\n"
                "🍽️ **Dining** — Menu recommendations, dining hours, room service\n"
                "⚽ **Sports & Facilities** — Book courts, pool, spa, cinema\n"
                "🌿 **Spa** — Treatment menu and bookings\n"
                "📍 **Location** — Directions, airport transfers\n"
                "✨ **Biringan Lore** — The mythology behind our hotel\n"
                "👤 **Human Staff** — Connect to our front desk team\n\n"
                "What would you like to explore first?")

    def _thanks(self, g):
        opts = [
            f"It's my pleasure{g}! The Mystic Concierge lives to guide. Is there anything else I can illuminate for you?",
            f"Always{g}! The invisible city thanks you for visiting. What else may I assist with?",
            f"Of course{g} — enchanting guests is what we do best. Anything else I can help arrange?",
        ]
        return random.choice(opts)

    def _general(self, ctx, history, g):
        if len(history) > 6:
            return (f"I may have drifted into the ethereal realm{g} — forgive me. Let me refocus: "
                    "I can help you book one of our 15 suites, reserve sports facilities, explore dining, book a spa treatment, or share Biringan lore. "
                    "What would you like?")
        return (f"Greetings from the crossroads of the seen and unseen{g}! "
                "I am the Mystic Concierge of Laurence Hotel — keeper of reservations, lore, and secrets. "
                "Ask me about our 15 enchanted suites, our 10 world-class facilities, "
                "dining at The Enchanted Table, or the ancient legend of Biringan. "
                "What brings you to our threshold?")
