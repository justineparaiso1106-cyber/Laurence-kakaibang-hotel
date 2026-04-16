# ============================================================================
# LAURENCE HOTEL — COMPLETE DATA STORE
# ============================================================================

rooms = {
    'mystic': {
        'name': 'Mystic Chamber',
        'subtitle': 'Intimate Sorcery',
        'price': 8900,
        'guests': 2,
        'size': 35,
        'floor': '3rd–5th',
        'bed': 'Queen Bed',
        'tag': 'Most Intimate',
        'tag_color': 'purple',
        'features': ['Aromatherapy System', 'Copper Soaking Tub', 'Biringan Herb Garden View', 'Smart Mood Lighting'],
        'image': 'https://images.unsplash.com/photo-1566195992011-5f6b21e53930?w=800&q=80',
        'gallery': [
            'https://images.unsplash.com/photo-1582719508461-905c673771fd?w=400&q=80',
            'https://images.unsplash.com/photo-1578683010236-d716f9a3f461?w=400&q=80'
        ]
    },
    'ethereal': {
        'name': 'Ethereal Suite',
        'subtitle': 'Floating Between Worlds',
        'price': 12500,
        'guests': 2,
        'size': 45,
        'floor': '6th–9th',
        'bed': 'King Bed',
        'tag': 'Best Value',
        'tag_color': 'gold',
        'features': ['Panoramic Floor-to-Ceiling Windows', 'Rain Shower + Chromotherapy', 'Smart Ambient System', 'Nespresso Station'],
        'image': 'https://images.unsplash.com/photo-1631049307264-da0ec9d70304?w=800&q=80',
        'gallery': [
            'https://images.unsplash.com/photo-1590490360182-c33d57733427?w=400&q=80',
            'https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=400&q=80'
        ]
    },
    'shadow': {
        'name': 'Shadow Loft',
        'subtitle': 'Urban Darkness, Refined',
        'price': 14800,
        'guests': 2,
        'size': 52,
        'floor': '7th–10th',
        'bed': 'King Bed',
        'tag': 'Urban Noir',
        'tag_color': 'gray',
        'features': ['Industrial Dark Aesthetic', 'Floor-to-Ceiling Glass', 'Hidden Bar Cabinet', 'Smart Mirror TV'],
        'image': 'https://images.unsplash.com/photo-1629140727571-9b5c6f6267b4?w=800&q=80',
        'gallery': [
            'https://images.unsplash.com/photo-1616594039964-ae9021a400a0?w=400&q=80',
            'https://images.unsplash.com/photo-1591088398332-8a7791972843?w=400&q=80'
        ]
    },
    'aurora': {
        'name': 'Aurora Chamber',
        'subtitle': 'Dawn Awakening',
        'price': 16500,
        'guests': 2,
        'size': 58,
        'floor': '10th–14th',
        'bed': 'Super King',
        'tag': 'Sunrise Views',
        'tag_color': 'orange',
        'features': ['East-Facing Sunrise Terrace', 'Aurora Lighting System', 'Infinity Bathtub', 'Couples Spa Corner'],
        'image': 'https://images.unsplash.com/photo-1568495248636-6432b97bd949?w=800&q=80',
        'gallery': [
            'https://images.unsplash.com/photo-1571003123894-1f0594d2b5d9?w=400&q=80',
            'https://images.unsplash.com/photo-1590490360182-c33d57733427?w=400&q=80'
        ]
    },
    'garden': {
        'name': 'Garden Sanctuary',
        'subtitle': 'Nature Within Walls',
        'price': 18900,
        'guests': 3,
        'size': 65,
        'floor': '2nd',
        'bed': 'King + Day Bed',
        'tag': 'Nature Retreat',
        'tag_color': 'green',
        'features': ['Private Garden Terrace', 'Living Plant Walls', 'Outdoor Rain Shower', 'Japanese Soaking Tub'],
        'image': 'https://images.unsplash.com/photo-1596394516093-501ba68a0ba6?w=800&q=80',
        'gallery': [
            'https://images.unsplash.com/photo-1566073771259-6a8506099945?w=400&q=80',
            'https://images.unsplash.com/photo-1614773238800-8dde11f01e58?w=400&q=80'
        ]
    },
    'obsidian': {
        'name': 'Obsidian Suite',
        'subtitle': 'Volcanic Luxury',
        'price': 22000,
        'guests': 2,
        'size': 75,
        'floor': '15th–18th',
        'bed': 'Emperor Bed',
        'tag': 'Most Dramatic',
        'tag_color': 'black',
        'features': ['Volcanic Rock Spa Bath', 'Lava Stone Massage Bed', 'Private Balcony', 'Black Marble Everything'],
        'image': 'https://images.unsplash.com/photo-1600210492493-0946911123ea?w=800&q=80',
        'gallery': [
            'https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=400&q=80',
            'https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=400&q=80'
        ]
    },
    'sapphire': {
        'name': 'Sapphire Retreat',
        'subtitle': 'Ocean of Calm',
        'price': 26500,
        'guests': 4,
        'size': 90,
        'floor': '19th–22nd',
        'bed': 'King + Twin',
        'tag': 'Family Luxury',
        'tag_color': 'blue',
        'features': ['Blue-Light Therapy Room', 'Separate Children\'s Suite', 'Sapphire Tile Pool Access', 'Family Kitchen'],
        'image': 'https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?w=800&q=80',
        'gallery': [
            'https://images.unsplash.com/photo-1571896349842-33c89424de2d?w=400&q=80',
            'https://images.unsplash.com/photo-1613977257363-707ba9348227?w=400&q=80'
        ]
    },
    'golden': {
        'name': 'Golden Horizon',
        'subtitle': 'Wealth Without Limit',
        'price': 29800,
        'guests': 4,
        'size': 110,
        'floor': '23rd–25th',
        'bed': 'King + King',
        'tag': 'Gold Standard',
        'tag_color': 'amber',
        'features': ['24k Gold Leaf Accents', 'Private Dining Room', 'Panoramic Dual Balconies', 'Champagne Butler'],
        'image': 'https://images.unsplash.com/photo-1560472354-b33ff0c44a43?w=800&q=80',
        'gallery': [
            'https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=400&q=80',
            'https://images.unsplash.com/photo-1602002418082-a4443e081dd1?w=400&q=80'
        ]
    },
    'royal': {
        'name': 'Royal Biringan',
        'subtitle': 'Command Absolute Respect',
        'price': 35000,
        'guests': 4,
        'size': 120,
        'floor': '26th–28th',
        'bed': 'Four-Poster King',
        'tag': 'Butler Service',
        'tag_color': 'crimson',
        'features': ['24/7 Dedicated Butler', 'Private Terrace + Jacuzzi', 'Silk-Draped Four-Poster', 'Samar Marble Bathroom'],
        'image': 'https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=800&q=80',
        'gallery': [
            'https://images.unsplash.com/photo-1591088398332-8a7791972843?w=400&q=80',
            'https://images.unsplash.com/photo-1602002418082-a4443e081dd1?w=400&q=80'
        ]
    },
    'crystal': {
        'name': 'Crystal Spire',
        'subtitle': 'Transparent Magnificence',
        'price': 38500,
        'guests': 4,
        'size': 135,
        'floor': '29th–31st',
        'bed': 'Emperor + Twin',
        'tag': 'Unique Design',
        'tag_color': 'cyan',
        'features': ['Glass-Floor Living Area', 'Crystal Chandelier Bathroom', 'Retractable Sky Ceiling', 'Personal Sommelier'],
        'image': 'https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=800&q=80',
        'gallery': [
            'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=400&q=80',
            'https://images.unsplash.com/photo-1615874959474-d609969a20ed?w=400&q=80'
        ]
    },
    'celestial': {
        'name': 'Celestial Villa',
        'subtitle': 'Your Own Private World',
        'price': 45000,
        'guests': 6,
        'size': 200,
        'floor': '32nd–34th',
        'bed': 'King + King + Twin',
        'tag': 'Private Pool',
        'tag_color': 'teal',
        'features': ['Private Infinity Pool', '3 Bedrooms', 'Full Gourmet Kitchen', 'Dedicated Concierge Team'],
        'image': 'https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=800&q=80',
        'gallery': [
            'https://images.unsplash.com/photo-1571896349842-33c89424de2d?w=400&q=80',
            'https://images.unsplash.com/photo-1613977257363-707ba9348227?w=400&q=80'
        ]
    },
    'lunar': {
        'name': 'Lunar Observatory',
        'subtitle': 'Sleep Under the Stars',
        'price': 52000,
        'guests': 4,
        'size': 175,
        'floor': '35th',
        'bed': 'Rotating King',
        'tag': 'Stargazing',
        'tag_color': 'indigo',
        'features': ['Retractable Glass Roof', 'Private Telescope & Observatory', 'Rotating Bed Platform', 'Astrologer On-Call'],
        'image': 'https://images.unsplash.com/photo-1518780664697-55e3ad937233?w=800&q=80',
        'gallery': [
            'https://images.unsplash.com/photo-1436891678271-9c672565d8f6?w=400&q=80',
            'https://images.unsplash.com/photo-1444703686981-a3abbc4d4fe3?w=400&q=80'
        ]
    },
    'phantom': {
        'name': 'Phantom Residence',
        'subtitle': 'Between Seen & Unseen',
        'price': 58000,
        'guests': 6,
        'size': 240,
        'floor': '36th–37th',
        'bed': 'King + King + Queen',
        'tag': 'Most Mysterious',
        'tag_color': 'violet',
        'features': ['Hidden Secret Rooms', 'Scrying Mirror System', 'Biringan Artifact Collection', 'Private Séance Parlor'],
        'image': 'https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=800&q=80',
        'gallery': [
            'https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=400&q=80',
            'https://images.unsplash.com/photo-1631049307264-da0ec9d70304?w=400&q=80'
        ]
    },
    'infinity': {
        'name': 'Infinity Estate',
        'subtitle': 'Space Without Horizon',
        'price': 62000,
        'guests': 8,
        'size': 280,
        'floor': '38th–39th',
        'bed': 'Emperor + King + King',
        'tag': 'Largest Suite',
        'tag_color': 'rose',
        'features': ['5-Room Layout', 'Indoor Garden Atrium', 'Private Chef\'s Kitchen', 'Entertainment Wing + Cinema'],
        'image': 'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=800&q=80',
        'gallery': [
            'https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=400&q=80',
            'https://images.unsplash.com/photo-1616594039964-ae9021a400a0?w=400&q=80'
        ]
    },
    'enchanted': {
        'name': 'Enchanted Penthouse',
        'subtitle': 'The Crown Jewel of Biringan',
        'price': 65000,
        'guests': 8,
        'size': 300,
        'floor': 'Top Floor — 40th',
        'bed': 'Emperor + All Types',
        'tag': 'Pinnacle',
        'tag_color': 'gold',
        'features': ['360° Panoramic Views', 'Rooftop Garden & Helipad', 'Private Cinema', '24/7 Full Staff'],
        'image': 'https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=800&q=80',
        'gallery': [
            'https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=400&q=80',
            'https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=400&q=80'
        ]
    }
}

entertainment = {
    'badminton': {
        'name': 'Badminton Arena',
        'price': 500,
        'guest_price': 0,
        'max': 4,
        'hours': '6AM–10PM',
        'equipment': ['Pro Rackets', 'Feather Shuttlecocks', 'Shoe Rental', 'Towels'],
        'image': 'https://images.unsplash.com/photo-1626224583764-f87db24ac4ea?w=600&q=80',
        'desc': '2 indoor professional-grade courts with Yonex flooring and LED lighting',
        'icon': 'zap'
    },
    'basketball': {
        'name': 'Basketball Court',
        'price': 800,
        'guest_price': 0,
        'max': 20,
        'hours': '6AM–10PM',
        'equipment': ['Spalding Balls', 'Reversible Jerseys', 'Referee Service', 'Scoreboard'],
        'image': 'https://images.unsplash.com/photo-1504450758481-7338eba7524a?w=600&q=80',
        'desc': 'Full NBA-regulation court with parquet flooring and pro-grade backboards',
        'icon': 'circle'
    },
    'volleyball': {
        'name': 'Volleyball Complex',
        'price': 600,
        'guest_price': 0,
        'max': 12,
        'hours': '6AM–10PM',
        'equipment': ['Mikasa Balls', 'Net Setup', 'Sand Court Access', 'Knee Pads'],
        'image': 'https://images.unsplash.com/photo-1612872087720-bb876e2e67d1?w=600&q=80',
        'desc': 'Indoor hardcourt + outdoor beach volleyball with imported sand',
        'icon': 'sun'
    },
    'swimming': {
        'name': 'Olympic Pool',
        'price': 0,
        'guest_price': 0,
        'max': 50,
        'hours': '6AM–10PM',
        'equipment': ['Speedo Towels', 'Goggles Rental', 'Swim Caps', 'Float Boards'],
        'image': 'https://images.unsplash.com/photo-1576013551627-0cc20b96c2a7?w=600&q=80',
        'desc': '50-meter heated infinity pool with mystical underwater lighting',
        'icon': 'waves'
    },
    'tennis': {
        'name': 'Tennis Club',
        'price': 700,
        'guest_price': 0,
        'max': 4,
        'hours': '6AM–10PM',
        'equipment': ['Wilson Rackets', 'Balls', 'Umpire Chair', 'Ball Machine'],
        'image': 'https://images.unsplash.com/photo-1554068865-24cecd4e34b8?w=600&q=80',
        'desc': '2 clay courts + 1 hard court with night lighting and pro coaching',
        'icon': 'target'
    },
    'gym': {
        'name': 'Mystic Fitness',
        'price': 0,
        'guest_price': 0,
        'max': 30,
        'hours': '24/7',
        'equipment': ['Lockers', 'Towels', 'Protein Shakes', 'Personal Trainers'],
        'image': 'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=600&q=80',
        'desc': '24/7 Technogym-equipped fitness center with personal trainers and yoga studio',
        'icon': 'activity'
    },
    'spa': {
        'name': 'Biringan Spa',
        'price': 2500,
        'guest_price': 2000,
        'max': 8,
        'hours': '8AM–10PM',
        'equipment': ['Aromatherapy Oils', 'Hot Stones', 'Herbal Wraps', 'Facial Kits'],
        'image': 'https://images.unsplash.com/photo-1544161515-4ab6ce6db874?w=600&q=80',
        'desc': 'Full-service spa with Biringan herbal treatments and hot stone therapy',
        'icon': 'heart'
    },
    'archery': {
        'name': 'Archery Range',
        'price': 900,
        'guest_price': 600,
        'max': 10,
        'hours': '8AM–6PM',
        'equipment': ['Recurve Bows', 'Arrows', 'Safety Gear', 'Coaching'],
        'image': 'https://images.unsplash.com/photo-1578826249636-1aa5c7ca63da?w=600&q=80',
        'desc': '30-meter indoor/outdoor archery range with pro coaching available',
        'icon': 'crosshair'
    },
    'billiards': {
        'name': 'Billiards Lounge',
        'price': 400,
        'guest_price': 0,
        'max': 6,
        'hours': '10AM–2AM',
        'equipment': ['Premium Cues', 'Chalk', 'Bridge Sticks', 'Cue Rack'],
        'image': 'https://images.unsplash.com/photo-1611321277419-7b5f2f37eed7?w=600&q=80',
        'desc': '4 professional pool tables in an atmospheric lounge setting',
        'icon': 'disc'
    },
    'cinema': {
        'name': 'Private Cinema',
        'price': 3500,
        'guest_price': 2800,
        'max': 12,
        'hours': '10AM–12MN',
        'equipment': ['4K Laser Projector', 'Dolby Atmos', 'Recliner Seats', 'Popcorn & Bar'],
        'image': 'https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=600&q=80',
        'desc': 'Private 12-seat cinema with 4K laser projector and full bar service',
        'icon': 'film'
    }
}

menu_items = [
    # Signatures
    {'name': 'Adobong Hotdog', 'desc': 'Our world-famous signature creation — Filipino adobo meets premium bratwurst, served with garlic fried rice', 'price': 450, 'image': 'https://images.unsplash.com/photo-1529692236671-f1f6cf9683ba?w=400&q=80', 'category': 'Signature', 'spicy': False, 'vegan': False},
    {'name': 'Biringan Feast Platter', 'desc': 'Mystical seafood selection with ghost pepper aioli, edible flowers, and ethereal garnishes', 'price': 2500, 'image': 'https://images.unsplash.com/photo-1534939561126-855b8675edd7?w=400&q=80', 'category': 'Seafood', 'spicy': True, 'vegan': False},
    {'name': 'Golden Tomahawk Steak', 'desc': 'Wagyu A5 tomahawk with 24k gold dust, Biringan herb butter, and truffle jus', 'price': 3500, 'image': 'https://images.unsplash.com/photo-1546833999-b9f581a1996d?w=400&q=80', 'category': 'Premium', 'spicy': False, 'vegan': False},
    # Italian
    {'name': 'Enchanted Wood-Fire Pizza', 'desc': 'Black truffle, burrata, 48-hour dough, mystical herb oil from rooftop garden', 'price': 1200, 'image': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=400&q=80', 'category': 'Italian', 'spicy': False, 'vegan': False},
    {'name': 'Mystic Pasta Nero', 'desc': 'Black squid ink pasta, 24k gold leaf, scallops, and a sauce crafted from ancient Samar recipe', 'price': 850, 'image': 'https://images.unsplash.com/photo-1563379926898-05f4575a45d8?w=400&q=80', 'category': 'Pasta', 'spicy': False, 'vegan': False},
    {'name': 'Truffle Risotto Royale', 'desc': 'Carnaroli rice, black truffle shavings, aged parmesan foam, saffron gold dust', 'price': 980, 'image': 'https://images.unsplash.com/photo-1476124369491-e7addf5db371?w=400&q=80', 'category': 'Italian', 'spicy': False, 'vegan': True},
    # Asian
    {'name': 'Phantom Ramen', 'desc': '24-hour tonkotsu broth with charcoal-black noodles, chashu pork, and spirit egg', 'price': 780, 'image': 'https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=400&q=80', 'category': 'Asian', 'spicy': True, 'vegan': False},
    {'name': 'Celestial Sushi Omakase', 'desc': '12-piece chef\'s selection with A5 wagyu nigiri, ghost shrimp, and lunar roll', 'price': 2800, 'image': 'https://images.unsplash.com/photo-1553621042-f6e147245754?w=400&q=80', 'category': 'Asian', 'spicy': False, 'vegan': False},
    {'name': 'Biringan Kare-Kare', 'desc': 'Oxtail in golden peanut sauce, bagoong cloud, and heirloom vegetable medley', 'price': 650, 'image': 'https://images.unsplash.com/photo-1547592166-23ac45744acd?w=400&q=80', 'category': 'Filipino', 'spicy': False, 'vegan': False},
    {'name': 'Dragon Dim Sum Tower', 'desc': '9-piece premium dim sum selection: har gow, siu mai, truffle bao, and century egg custard', 'price': 890, 'image': 'https://images.unsplash.com/photo-1563245372-f21724e3856d?w=400&q=80', 'category': 'Asian', 'spicy': False, 'vegan': False},
    # Healthy
    {'name': 'Ethereal Garden Salad', 'desc': 'Organic greens, edible flowers, gold vinaigrette, candied walnuts, and goat cheese snow', 'price': 650, 'image': 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&q=80', 'category': 'Healthy', 'spicy': False, 'vegan': True},
    {'name': 'Aurora Acai Bowl', 'desc': 'Açaí base with spirulina, dragon fruit, edible gold, and activated charcoal granola', 'price': 520, 'image': 'https://images.unsplash.com/photo-1490323814980-e0f37f0a8d45?w=400&q=80', 'category': 'Healthy', 'spicy': False, 'vegan': True},
    # Desserts
    {'name': 'Black Moon Soufflé', 'desc': 'Activated charcoal soufflé with white chocolate interior, gold-dusted, flambéed tableside', 'price': 680, 'image': 'https://images.unsplash.com/photo-1488477181946-6428a0291777?w=400&q=80', 'category': 'Dessert', 'spicy': False, 'vegan': False},
    {'name': 'Biringan Halo-Halo Supreme', 'desc': 'Elevated Filipino classic: ube cream, gold leaf, rare tropical fruits, silver shavings', 'price': 480, 'image': 'https://images.unsplash.com/photo-1549007994-cb92caebd54b?w=400&q=80', 'category': 'Filipino', 'spicy': False, 'vegan': True},
    # Drinks
    {'name': 'Smoke & Spirits Cocktail', 'desc': 'Smoked aged rum, butterfly pea flower gin, gold syrup — changes color when stirred', 'price': 580, 'image': 'https://images.unsplash.com/photo-1551538827-9c037cb4f32a?w=400&q=80', 'category': 'Drinks', 'spicy': False, 'vegan': True},
    {'name': 'Biringan Blue Elixir', 'desc': 'Blue butterfly pea lemonade, lavender foam, edible glitter — our non-alcoholic signature', 'price': 320, 'image': 'https://images.unsplash.com/photo-1497534446932-c925b458314e?w=400&q=80', 'category': 'Drinks', 'spicy': False, 'vegan': True},
]

spa_services = [
    {'name': 'Biringan Spirit Ritual', 'duration': '120 min', 'price': 4500, 'desc': 'Full body wrap with sacred herbs, hot stone placement, and chanting therapy'},
    {'name': 'Golden Radiance Facial', 'duration': '60 min', 'price': 2800, 'desc': '24k gold leaf facial with diamond powder exfoliation'},
    {'name': 'Couples Infinity Journey', 'duration': '90 min', 'price': 7500, 'desc': 'Synchronized couples massage with private bath ritual'},
]
