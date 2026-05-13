// Dark Mode Logic
const htmlEl = document.documentElement;
const themeBtn = document.getElementById('themeToggle');
const themeBtnMobile = document.getElementById('themeToggleMobile');

function setTheme(isDark) {
    if (isDark) {
        htmlEl.classList.add('dark');
        localStorage.theme = 'dark';
    } else {
        htmlEl.classList.remove('dark');
        localStorage.theme = 'light';
    }
}

// Init Theme
if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    setTheme(true);
} else {
    setTheme(false);
}

[themeBtn, themeBtnMobile].forEach(btn => {
    if(btn) btn.addEventListener('click', () => setTheme(!htmlEl.classList.contains('dark')));
});

// Fix PDF printing in dark mode
window.addEventListener('beforeprint', () => {
    htmlEl.classList.remove('dark');
});
window.addEventListener('afterprint', () => {
    if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        htmlEl.classList.add('dark');
    }
});

// Initialize Animations
if (typeof AOS !== 'undefined') {
    AOS.init({
        duration: 800,
        once: true,
        offset: 50,
        easing: 'ease-out-cubic',
    });
}

// Mobile Menu
const mobileMenuBtn = document.getElementById('mobileMenuBtn');
if (mobileMenuBtn) {
    mobileMenuBtn.addEventListener('click', function() {
        document.getElementById('mobileMenu').classList.toggle('hidden');
    });
}

// Navbar scroll effect
window.addEventListener('scroll', () => {
    const nav = document.getElementById('navbar');
    if (nav) {
        if (window.scrollY > 10) {
            nav.classList.add('shadow-sm');
        } else {
            nav.classList.remove('shadow-sm');
        }
    }
});

// Accordion (Tentang)
function toggleAccordion(id) {
    const content = document.getElementById(id);
    if (!content) return;
    
    const iconId = id.replace('acc-', 'icon-');
    const icon = document.getElementById(iconId);
    
    const isHidden = content.classList.contains('hidden');
    
    // Close all
    document.querySelectorAll('[id^="acc-"]').forEach(el => el.classList.add('hidden'));
    document.querySelectorAll('[id^="icon-"]').forEach(el => {
        el.classList.remove('fa-minus', 'text-brand-500', 'rotate-180');
        el.classList.add('fa-plus', 'text-slate-400');
    });
    
    // Open clicked if it was hidden
    if (isHidden) {
        content.classList.remove('hidden');
        if (icon) {
            icon.classList.remove('fa-plus', 'text-slate-400');
            icon.classList.add('fa-minus', 'text-brand-500', 'rotate-180');
        }
    }
}

// Index Form Logic
function updateGejalaCount() {
    const allRadios = document.querySelectorAll('.keyakinan-radio:checked');
    let count = 0;
    allRadios.forEach(r => { if (parseFloat(r.value) > 0) count++; });
    
    const countEl = document.getElementById('gejalaCount');
    const textEl = document.getElementById('gejalaText');
    const btnSubmit = document.getElementById('btnSubmit');
    const floatBar = document.getElementById('floatingBar');

    if (countEl) countEl.textContent = count;

    if (floatBar) {
        if (count > 0) {
            floatBar.classList.add('show');
        } else {
            floatBar.classList.remove('show');
        }
    }

    if (count < 3) {
        if (btnSubmit) btnSubmit.disabled = true;
        if (textEl) textEl.innerHTML = `Kurang ${3 - count} gejala lagi`;
    } else {
        if (btnSubmit) btnSubmit.disabled = false;
        if (textEl) textEl.innerHTML = `<span class="text-brand-300 font-bold">Siap dianalisis!</span>`;
    }
}

document.addEventListener('DOMContentLoaded', () => {
    // Gejala count init
    if (document.getElementById('gejalaCount')) {
        updateGejalaCount();
    }
    
    // Auto-focus logic when clicking "Mulai Analisis" from Hero
    const btnMulai = document.getElementById('btnMulaiHero');
    if (btnMulai) {
        btnMulai.addEventListener('click', (e) => {
            setTimeout(() => {
                const inputNama = document.getElementById('inputNama');
                if (inputNama) inputNama.focus();
            }, 600); // Wait for smooth scroll
        });
    }

    const diagnosaForm = document.getElementById('diagnosaForm');
    if (diagnosaForm) {
        diagnosaForm.addEventListener('submit', function(e) {
            const btn = document.getElementById('btnSubmit');
            if(btn && !btn.disabled) {
                btn.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i> Sedang memproses...';
                btn.classList.add('opacity-80');
            }
        });
    }
});
