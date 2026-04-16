// =================================================================
// LAURENCE HOTEL — MAIN JAVASCRIPT
// Biringan Holographic Edition
// =================================================================

// ===== PARTICLES =====
(function initParticles() {
    const canvas = document.getElementById('particles-canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    let particles = [];

    function resize() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }

    function createParticle() {
        return {
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            size: Math.random() * 1.5 + 0.3,
            speedX: (Math.random() - 0.5) * 0.3,
            speedY: -Math.random() * 0.5 - 0.1,
            opacity: Math.random() * 0.5 + 0.1,
            color: Math.random() > 0.6 ? '#c9a84c' : Math.random() > 0.5 ? '#6478ff' : '#ffffff'
        };
    }

    resize();
    for (let i = 0; i < 80; i++) particles.push(createParticle());

    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        particles.forEach((p, i) => {
            ctx.save();
            ctx.globalAlpha = p.opacity;
            ctx.fillStyle = p.color;
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
            ctx.fill();
            ctx.restore();
            p.x += p.speedX;
            p.y += p.speedY;
            p.opacity -= 0.0008;
            if (p.y < -10 || p.opacity <= 0) particles[i] = createParticle();
        });
        requestAnimationFrame(animate);
    }

    animate();
    window.addEventListener('resize', resize);
})();

// ===== NAVBAR SCROLL =====
window.addEventListener('scroll', () => {
    const nav = document.getElementById('navbar');
    if (window.scrollY > 60) nav.classList.add('scrolled');
    else nav.classList.remove('scrolled');
}, { passive: true });

// ===== LUCIDE ICONS =====
document.addEventListener('DOMContentLoaded', () => {
    lucide.createIcons();
    checkAuthState();
    initFilters();
    initDiningFilters();
    setTodayDates();
});

function setTodayDates() {
    const today = new Date().toISOString().split('T')[0];
    ['checkin', 'checkout', 'ent-date'].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.min = today;
    });
}

// ===== HOLOGRAPHIC ROOM CARD MOUSE EFFECT =====
document.addEventListener('mousemove', (e) => {
    document.querySelectorAll('.room-card').forEach(card => {
        const rect = card.getBoundingClientRect();
        const x = ((e.clientX - rect.left) / rect.width) * 100;
        const y = ((e.clientY - rect.top) / rect.height) * 100;
        if (x > 0 && x < 100 && y > 0 && y < 100) {
            card.style.setProperty('--mouse-x', x + '%');
            card.style.setProperty('--mouse-y', y + '%');
        }
    });
});

// ===== ROOM FILTERS =====
function initFilters() {
    const filterBtns = document.querySelectorAll('#rooms-filter .filter-btn');
    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            const filter = btn.dataset.filter;
            document.querySelectorAll('.room-card').forEach(card => {
                if (filter === 'all' || card.dataset.tier === filter) {
                    card.classList.remove('hidden-card');
                } else {
                    card.classList.add('hidden-card');
                }
            });
        });
    });
}

// ===== DINING FILTERS =====
function initDiningFilters() {
    const filterBtns = document.querySelectorAll('.dining-filter .filter-btn');
    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            const cat = btn.dataset.cat;
            document.querySelectorAll('.dining-card').forEach(card => {
                if (cat === 'all' || card.dataset.category === cat) {
                    card.classList.remove('hidden-item');
                } else {
                    card.classList.add('hidden-item');
                }
            });
        });
    });
}

// ===== BOOKING =====
function selectRoom(key) {
    const select = document.getElementById('room-type');
    if (select) {
        select.value = key;
        calcPrice();
    }
    document.getElementById('book').scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function calcPrice() {
    const checkin = document.getElementById('checkin').value;
    const checkout = document.getElementById('checkout').value;
    const roomType = document.getElementById('room-type').value;
    if (!checkin || !checkout || !roomType) {
        document.getElementById('price-preview').classList.add('hidden');
        return;
    }
    const d1 = new Date(checkin), d2 = new Date(checkout);
    if (d2 <= d1) return;
    const nights = Math.ceil((d2 - d1) / (1000 * 60 * 60 * 24));
    const pricePerNight = ROOMS_DATA[roomType]?.price || 0;
    const total = nights * pricePerNight;
    document.getElementById('nights-label').textContent = `${nights} night${nights > 1 ? 's' : ''}`;
    document.getElementById('total-price').textContent = '₱' + total.toLocaleString();
    document.getElementById('price-preview').classList.remove('hidden');
}

async function submitBooking(e) {
    e.preventDefault();
    const data = {
        name: document.getElementById('guest-name').value,
        email: document.getElementById('guest-email').value,
        checkin: document.getElementById('checkin').value,
        checkout: document.getElementById('checkout').value,
        room: document.getElementById('room-type').value,
        promo: document.getElementById('promo-code').value
    };
    try {
        const res = await fetch('/api/book', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) });
        const result = await res.json();
        if (result.success) {
            const discountText = result.discount > 0 ? ` (${(result.discount * 100).toFixed(0)}% off applied!)` : '';
            showToast(`✨ Booking confirmed! Ref: ${result.ref} — ₱${result.total.toLocaleString()} for ${result.nights} nights${discountText}`);
            document.getElementById('booking-form').reset();
            document.getElementById('price-preview').classList.add('hidden');
            document.getElementById('discount-note').textContent = '';
        } else {
            showToast('❌ ' + (result.error || 'Booking failed. Please try again.'));
        }
    } catch {
        showToast('❌ Connection error. Please try again.');
    }
}

// ===== ENT MODAL =====
function openEntModal(key) {
    const data = ENT_DATA[key];
    if (!data) return;
    document.getElementById('ent-facility').value = key;
    document.getElementById('ent-modal-title').textContent = data.name;
    document.getElementById('ent-modal-desc').textContent = data.desc + ' Equipment included: ' + data.equipment.join(', ') + '.';
    document.getElementById('ent-modal').classList.remove('hidden');
    lucide.createIcons();
}
function closeEntModal(e) {
    if (e.target === document.getElementById('ent-modal')) closeEntModalForce();
}
function closeEntModalForce() {
    document.getElementById('ent-modal').classList.add('hidden');
}
async function submitEntBooking(e) {
    e.preventDefault();
    const data = {
        facility: document.getElementById('ent-facility').value,
        date: document.getElementById('ent-date').value,
        time: document.getElementById('ent-time').value,
        hours: document.getElementById('ent-hours').value,
        guests: document.getElementById('ent-guests').value
    };
    try {
        const res = await fetch('/api/ent-book', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) });
        const result = await res.json();
        if (result.success) {
            showToast(`🎯 ${ENT_DATA[data.facility]?.name || 'Facility'} booked for ${data.date} at ${data.time}!`);
            closeEntModalForce();
        } else {
            showToast('❌ Booking failed. Please try again.');
        }
    } catch {
        showToast('❌ Connection error.');
    }
}

// ===== LIGHTBOX =====
function openLightbox(src) {
    document.getElementById('lightbox-img').src = src;
    document.getElementById('lightbox').classList.remove('hidden');
    document.body.style.overflow = 'hidden';
    lucide.createIcons();
}
function closeLightbox() {
    document.getElementById('lightbox').classList.add('hidden');
    document.body.style.overflow = '';
}
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        closeLightbox();
        closeEntModalForce();
        closeAuthModalForce();
    }
});

// ===== AUTH =====
async function checkAuthState() {
    try {
        const res = await fetch('/api/me');
        const data = await res.json();
        if (data.logged_in) {
            setLoggedIn(data.name);
        }
    } catch {}
}

function setLoggedIn(name) {
    document.getElementById('nav-auth').classList.add('hidden');
    document.getElementById('nav-user').classList.remove('hidden');
    document.getElementById('user-menu-name').textContent = name;
    lucide.createIcons();
}
function setLoggedOut() {
    document.getElementById('nav-auth').classList.remove('hidden');
    document.getElementById('nav-user').classList.add('hidden');
}

function openAuthModal(tab) {
    document.getElementById('auth-modal').classList.remove('hidden');
    switchAuthTab(tab);
    document.body.style.overflow = 'hidden';
    lucide.createIcons();
}
function closeAuthModal(e) {
    if (e.target === document.getElementById('auth-modal')) closeAuthModalForce();
}
function closeAuthModalForce() {
    document.getElementById('auth-modal').classList.add('hidden');
    document.body.style.overflow = '';
}
function switchAuthTab(tab) {
    const isLogin = tab === 'login';
    document.getElementById('tab-login').classList.toggle('active', isLogin);
    document.getElementById('tab-signup').classList.toggle('active', !isLogin);
    document.getElementById('login-form').classList.toggle('hidden', !isLogin);
    document.getElementById('signup-form').classList.toggle('hidden', isLogin);
}
function toggleUserMenu() {
    document.getElementById('user-menu').classList.toggle('hidden');
}
document.addEventListener('click', (e) => {
    const userSection = document.getElementById('nav-user');
    if (userSection && !userSection.contains(e.target)) {
        document.getElementById('user-menu').classList.add('hidden');
    }
});

async function doLogin(e) {
    e.preventDefault();
    const errEl = document.getElementById('login-error');
    errEl.classList.add('hidden');
    const data = {
        email: document.getElementById('login-email').value,
        password: document.getElementById('login-password').value
    };
    try {
        const res = await fetch('/api/login', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) });
        const result = await res.json();
        if (result.success) {
            setLoggedIn(result.name);
            closeAuthModalForce();
            showToast(`✨ Welcome back, ${result.name}! The invisible city awaits.`);
            // Pre-fill booking form
            const nameEl = document.getElementById('guest-name');
            if (nameEl && !nameEl.value) nameEl.value = result.name;
        } else {
            errEl.textContent = result.error;
            errEl.classList.remove('hidden');
        }
    } catch {
        errEl.textContent = 'Connection error. Please try again.';
        errEl.classList.remove('hidden');
    }
}

async function doSignup(e) {
    e.preventDefault();
    const errEl = document.getElementById('signup-error');
    errEl.classList.add('hidden');
    const data = {
        name: document.getElementById('signup-name').value,
        email: document.getElementById('signup-email').value,
        password: document.getElementById('signup-password').value
    };
    try {
        const res = await fetch('/api/signup', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) });
        const result = await res.json();
        if (result.success) {
            setLoggedIn(result.name);
            closeAuthModalForce();
            showToast(`🌟 Welcome to Biringan, ${result.name}! Your legend begins now.`);
            const nameEl = document.getElementById('guest-name');
            if (nameEl) nameEl.value = result.name;
        } else {
            errEl.textContent = result.error;
            errEl.classList.remove('hidden');
        }
    } catch {
        errEl.textContent = 'Connection error. Please try again.';
        errEl.classList.remove('hidden');
    }
}

async function doLogout() {
    try {
        await fetch('/api/logout', { method: 'POST' });
    } catch {}
    setLoggedOut();
    toggleUserMenu();
    showToast('👋 Farewell. The invisible city bids you safe travels.');
}

// ===== AI CHAT =====
let chatHistory = [];
let chatOpen = false;

function toggleChat() {
    chatOpen = !chatOpen;
    const win = document.getElementById('chat-window');
    if (chatOpen) {
        win.classList.remove('hidden');
        document.getElementById('chat-input').focus();
    } else {
        win.classList.add('hidden');
    }
}

function clearChat() {
    chatHistory = [];
    const container = document.getElementById('chat-messages');
    container.innerHTML = '';
    appendChatMsg('ai', 'Conversation cleared. The mystical energies have been reset. How may I assist you? ✨');
}

function quickAsk(text) {
    document.getElementById('chat-input').value = text;
    sendChat();
}

async function sendChat() {
    const input = document.getElementById('chat-input');
    const msg = input.value.trim();
    if (!msg) return;
    input.value = '';

    appendChatMsg('user', msg);
    const typingId = showTyping();

    try {
        const res = await fetch('/api/ai-chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: msg, history: chatHistory })
        });
        const data = await res.json();
        removeTyping(typingId);

        // Format markdown-ish text
        const formatted = formatChatResponse(data.response);
        appendChatMsg('ai', formatted, true);

        chatHistory.push({ role: 'user', message: msg });
        chatHistory.push({ role: 'ai', message: data.response });
        if (chatHistory.length > 16) chatHistory = chatHistory.slice(-16);

    } catch {
        removeTyping(typingId);
        appendChatMsg('ai', "The mystical energies are momentarily disrupted. Please try again, or reach our front desk at +63 2 8123 4567. 📞");
    }
}

function formatChatResponse(text) {
    // Bold **text**
    text = text.replace(/\*\*(.*?)\*\*/g, '<strong class="text-white">$1</strong>');
    // Line breaks
    text = text.replace(/\n/g, '<br>');
    // Bullet-ish lines starting with 🌙 ✨ 💎 etc.
    return text;
}

function appendChatMsg(role, htmlContent, isHtml = false) {
    const container = document.getElementById('chat-messages');
    const div = document.createElement('div');
    div.className = `chat-msg ${role}`;

    const avatarIcon = role === 'ai'
        ? '<i data-lucide="sparkles" class="w-3.5 h-3.5"></i>'
        : '<i data-lucide="user" class="w-3.5 h-3.5"></i>';

    div.innerHTML = `
        <div class="msg-avatar">${avatarIcon}</div>
        <div class="msg-bubble">${isHtml ? htmlContent : escapeHtml(htmlContent)}</div>
    `;
    container.appendChild(div);
    container.scrollTop = container.scrollHeight;
    lucide.createIcons();
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.appendChild(document.createTextNode(text));
    return div.innerHTML;
}

function showTyping() {
    const container = document.getElementById('chat-messages');
    const id = 'typing-' + Date.now();
    const div = document.createElement('div');
    div.id = id;
    div.className = 'chat-msg ai';
    div.innerHTML = `
        <div class="msg-avatar"><i data-lucide="sparkles" class="w-3.5 h-3.5"></i></div>
        <div class="msg-bubble"><div class="typing-dots"><div class="typing-dot"></div><div class="typing-dot"></div><div class="typing-dot"></div></div></div>
    `;
    container.appendChild(div);
    container.scrollTop = container.scrollHeight;
    lucide.createIcons();
    return id;
}
function removeTyping(id) {
    const el = document.getElementById(id);
    if (el) el.remove();
}

// ===== TOAST =====
let toastTimer = null;
function showToast(message) {
    const toast = document.getElementById('toast');
    document.getElementById('toast-msg').innerHTML = message;
    toast.classList.add('show');
    toast.classList.remove('hidden');
    if (toastTimer) clearTimeout(toastTimer);
    toastTimer = setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => toast.classList.add('hidden'), 400);
    }, 5000);
}

// ===== SMOOTH ENTRANCE ANIMATIONS =====
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
            observer.unobserve(entry.target);
        }
    });
}, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

window.addEventListener('load', () => {
    document.querySelectorAll('.room-card, .dining-card, .ent-card, .gallery-item').forEach((el, i) => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(24px)';
        el.style.transition = `opacity 0.5s ease ${(i % 6) * 0.08}s, transform 0.5s ease ${(i % 6) * 0.08}s, box-shadow 0.4s ease, border-color 0.4s ease`;
        observer.observe(el);
    });
});
