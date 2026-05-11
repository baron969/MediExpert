/**
 * script.js - MediExpert Redesign
 */

// Wizard Navigation
function nextStep(stepNum) {
    // Basic validation for Step 1
    if (stepNum === 2) {
        const umur = document.getElementById('umur').value;
        const jk = document.getElementById('jenis_kelamin').value;
        if (!umur || !jk) {
            alert("Mohon isi Umur dan Jenis Kelamin terlebih dahulu.");
            return;
        }
        
        // Show Floating Bar when entering Step 2
        document.getElementById('floatingBar').classList.add('visible');
    }

    // Hide all steps
    document.querySelectorAll('.wizard-step').forEach(step => {
        step.classList.remove('active');
    });

    // Show target step
    document.getElementById('step' + stepNum).classList.add('active');
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function prevStep(stepNum) {
    if (stepNum === 1) {
        document.getElementById('floatingBar').classList.remove('visible');
    }

    // Hide all steps
    document.querySelectorAll('.wizard-step').forEach(step => {
        step.classList.remove('active');
    });

    // Show target step
    document.getElementById('step' + stepNum).classList.add('active');
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Gejala Card Selection
function toggleCard(cardElement) {
    const checkbox = cardElement.querySelector('.selectable-checkbox');
    // The click event triggers both the label and the checkbox.
    // To prevent double toggling, we check if the class needs updating based on actual checkbox state.
    
    // We defer the visual update slightly to allow the checkbox state to change
    setTimeout(() => {
        if (checkbox.checked) {
            cardElement.classList.add('selected');
        } else {
            cardElement.classList.remove('selected');
        }
        updateGejalaCount();
    }, 10);
}

function updateGejalaCount() {
    const checkedCount = document.querySelectorAll('.selectable-checkbox:checked').length;
    const countEl = document.getElementById('gejalaCount');
    const textEl = document.getElementById('gejalaText');
    const btnSubmit = document.getElementById('btnSubmit');

    if (countEl) countEl.textContent = checkedCount;

    if (checkedCount < 3) {
        if (btnSubmit) btnSubmit.disabled = true;
        if (textEl) textEl.innerHTML = `Gejala Terpilih<br><small class="text-muted">Pilih minimal ${3 - checkedCount} lagi</small>`;
    } else {
        if (btnSubmit) btnSubmit.disabled = false;
        if (textEl) textEl.innerHTML = `Gejala Terpilih<br><small style="color: var(--success); font-weight: 600;">Siap dianalisis!</small>`;
    }
}

// Initialize on page load (in case of returning with pre-checked items)
document.addEventListener('DOMContentLoaded', () => {
    // If we are on step 2 natively (e.g. error redirect), show floating bar
    if (document.getElementById('step2') && document.getElementById('step2').classList.contains('active')) {
        document.getElementById('floatingBar').classList.add('visible');
    }
    
    // Initial count update
    if (document.querySelectorAll('.selectable-checkbox').length > 0) {
        updateGejalaCount();
    }
});
