/**
 * script.js
 * MediExpert - Sistem Pakar Diagnosa Penyakit
 * JavaScript utama untuk interaktivitas UI
 */

// ============================================================
// NAVBAR
// ============================================================
const navbar    = document.getElementById('navbar');
const hamburger = document.getElementById('hamburger');
const navMenu   = document.getElementById('navbarMenu');

// Scroll effect navbar
window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        navbar?.classList.add('scrolled');
    } else {
        navbar?.classList.remove('scrolled');
    }
});

// Mobile hamburger toggle
hamburger?.addEventListener('click', () => {
    navMenu?.classList.toggle('open');
    hamburger.classList.toggle('active');
});

// Tutup menu jika klik di luar
document.addEventListener('click', (e) => {
    if (!navbar?.contains(e.target)) {
        navMenu?.classList.remove('open');
        hamburger?.classList.remove('active');
    }
});

// ============================================================
// FORM DIAGNOSA — Checkbox Gejala Interaktif
// ============================================================
const checkboxes  = document.querySelectorAll('.gejala-cb');
const counterNum  = document.getElementById('counterNum');
const hintText    = document.getElementById('hintText');
const progressBar = document.getElementById('progressBar');
const btnDiagnosa = document.getElementById('btnDiagnosa');
const btnReset    = document.getElementById('btnReset');
const formDiagnosa = document.getElementById('formDiagnosa');
const TOTAL_GEJALA = checkboxes.length;
const MIN_GEJALA   = 3;

/**
 * Update tampilan counter, progress bar, dan state tombol diagnosa
 */
function updateCounter() {
    const checked = document.querySelectorAll('.gejala-cb:checked').length;

    // Update counter number
    if (counterNum) counterNum.textContent = checked;

    // Update progress bar
    const pct = TOTAL_GEJALA > 0 ? (checked / TOTAL_GEJALA) * 100 : 0;
    if (progressBar) progressBar.style.width = Math.min(pct, 100) + '%';

    // Update hint text
    if (hintText) {
        if (checked === 0) {
            hintText.textContent = 'Pilih minimal 3 gejala';
            hintText.className = 'hint-warn';
        } else if (checked < MIN_GEJALA) {
            hintText.textContent = `Perlu ${MIN_GEJALA - checked} gejala lagi`;
            hintText.className = 'hint-warn';
        } else {
            hintText.textContent = `${checked} gejala terpilih — siap diagnosa!`;
            hintText.className = 'hint-ok';
        }
    }

    // Enable/disable tombol diagnosa
    if (btnDiagnosa) {
        btnDiagnosa.disabled = checked < MIN_GEJALA;
    }
}

// Bind event ke setiap checkbox gejala
checkboxes.forEach(cb => {
    cb.addEventListener('change', () => {
        const label = cb.closest('.gejala-item');
        if (cb.checked) {
            label?.classList.add('checked');
        } else {
            label?.classList.remove('checked');
        }
        updateCounter();
    });
});

// Klik pada label gejala item → toggle checkbox
document.querySelectorAll('.gejala-item').forEach(item => {
    item.addEventListener('click', (e) => {
        // Hindari double-fire jika klik langsung di checkbox
        if (e.target.type === 'checkbox') return;
        const cb = item.querySelector('.gejala-cb');
        if (cb) {
            cb.checked = !cb.checked;
            cb.dispatchEvent(new Event('change'));
        }
    });
});

// Tombol "Pilih Semua" per kategori
document.querySelectorAll('.btn-pilih-semua').forEach(btn => {
    btn.addEventListener('click', () => {
        const katIdx = btn.dataset.kategori;
        const kategori = document.querySelector(`.gejala-kategori[data-kategori="${katIdx}"]`);
        if (!kategori) return;

        const cbs = kategori.querySelectorAll('.gejala-cb');
        const allChecked = [...cbs].every(cb => cb.checked);

        cbs.forEach(cb => {
            cb.checked = !allChecked;
            cb.dispatchEvent(new Event('change'));
        });

        btn.textContent = allChecked ? 'Pilih Semua' : 'Batal Pilih';
    });
});

// Tombol Reset — hapus semua pilihan
btnReset?.addEventListener('click', () => {
    checkboxes.forEach(cb => {
        cb.checked = false;
        cb.closest('.gejala-item')?.classList.remove('checked');
    });
    // Reset semua tombol "pilih semua"
    document.querySelectorAll('.btn-pilih-semua').forEach(btn => {
        btn.textContent = 'Pilih Semua';
    });
    updateCounter();
});

// Form submit — tampilkan loading state
formDiagnosa?.addEventListener('submit', (e) => {
    const checked = document.querySelectorAll('.gejala-cb:checked').length;
    if (checked < MIN_GEJALA) {
        e.preventDefault();
        showToast(`Pilih minimal ${MIN_GEJALA} gejala terlebih dahulu.`, 'warn');
        return;
    }
    // Tampilkan loading
    const content = btnDiagnosa?.querySelector('.btn-content');
    const loading = btnDiagnosa?.querySelector('.btn-loading');
    if (content) content.style.display = 'none';
    if (loading) loading.style.display = 'flex';
    if (btnDiagnosa) btnDiagnosa.disabled = true;
});

// Inisialisasi counter saat halaman load
updateCounter();

// ============================================================
// SMOOTH SCROLL ke #form-diagnosa
// ============================================================
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', (e) => {
        const target = document.querySelector(anchor.getAttribute('href'));
        if (target) {
            e.preventDefault();
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });
});

// ============================================================
// TOAST NOTIFICATION
// ============================================================
function showToast(message, type = 'info') {
    const existing = document.getElementById('toastNotif');
    if (existing) existing.remove();

    const colors = {
        info : { bg: '#3B82F6', icon: 'fa-info-circle' },
        warn : { bg: '#F59E0B', icon: 'fa-triangle-exclamation' },
        error: { bg: '#EF4444', icon: 'fa-circle-xmark' },
        ok   : { bg: '#10B981', icon: 'fa-circle-check' },
    };
    const c = colors[type] || colors.info;

    const toast = document.createElement('div');
    toast.id = 'toastNotif';
    toast.innerHTML = `<i class="fas ${c.icon}"></i> ${message}`;
    Object.assign(toast.style, {
        position  : 'fixed',
        bottom    : '24px',
        right     : '24px',
        zIndex    : '9999',
        padding   : '14px 20px',
        background: c.bg,
        color     : '#fff',
        borderRadius: '12px',
        fontSize  : '14px',
        fontWeight: '600',
        fontFamily: "'Inter', sans-serif",
        boxShadow : '0 8px 24px rgba(0,0,0,0.3)',
        display   : 'flex',
        alignItems: 'center',
        gap       : '9px',
        animation : 'slideUp 0.3s ease',
        maxWidth  : '380px',
    });

    // Inject keyframe jika belum ada
    if (!document.getElementById('toastKeyframe')) {
        const style = document.createElement('style');
        style.id = 'toastKeyframe';
        style.textContent = `
            @keyframes slideUp{from{transform:translateY(20px);opacity:0}to{transform:none;opacity:1}}
        `;
        document.head.appendChild(style);
    }

    document.body.appendChild(toast);
    setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transform = 'translateY(20px)';
        toast.style.transition = 'all 0.3s ease';
        setTimeout(() => toast.remove(), 300);
    }, 3500);
}

// ============================================================
// ANIMATE ON SCROLL (IntersectionObserver)
// ============================================================
const observerOpts = { threshold: 0.12, rootMargin: '0px 0px -40px 0px' };
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            observer.unobserve(entry.target);
        }
    });
}, observerOpts);

// Inject CSS animasi
const animStyle = document.createElement('style');
animStyle.textContent = `
    .fade-up{opacity:0;transform:translateY(30px);transition:opacity 0.6s ease,transform 0.6s ease}
    .fade-up.visible{opacity:1;transform:none}
    .navbar.scrolled{box-shadow:0 4px 24px rgba(0,0,0,0.3)}
`;
document.head.appendChild(animStyle);

// Apply ke elemen-elemen
document.querySelectorAll(
    '.step-card, .disease-card, .gejala-kategori, .kp-card, .stats-card, .chart-card, .saran-item'
).forEach((el, i) => {
    el.classList.add('fade-up');
    el.style.transitionDelay = `${(i % 4) * 0.08}s`;
    observer.observe(el);
});

// ============================================================
// UTILS
// ============================================================
// Highlight search result di tabel riwayat
const searchRiwayat = document.getElementById('searchRiwayat');
searchRiwayat?.addEventListener('input', function () {
    const q = this.value.toLowerCase().trim();
    document.querySelectorAll('#tableRiwayat tbody tr').forEach(row => {
        const text = row.textContent.toLowerCase();
        row.style.display = q === '' || text.includes(q) ? '' : 'none';
    });
});
