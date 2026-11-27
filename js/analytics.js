// HeyCatch analytics, gated on visitor consent. Loaded by every public page.
import { analytics } from 'https://esm.sh/@heycatch/sdk@0.8.5';

const CHOICE_KEY = 'qs-analytics-consent'; // 'yes' | 'no'

analytics.init({
  projectKey: 'hck_pk_6BvijERVXjxjpAe3OqD0fxUPQ95gbhHz',
  site: 'landing',
  requestBatching: false,
  optOutCapturingByDefault: true, // nothing is collected until the visitor allows it
  install: { framework: 'web', agent: 'claude-code' },
});

function readChoice() {
  try { return localStorage.getItem(CHOICE_KEY); } catch { return null; }
}

function saveChoice(choice) {
  try { localStorage.setItem(CHOICE_KEY, choice); } catch { /* ask again next page */ }
}

// Removes what the SDK stored, for a visitor who withdraws consent.
function clearAnalyticsData() {
  const ours = (name) => /^(__)?ph_|^heycatch_/.test(name);
  for (const store of ['localStorage', 'sessionStorage']) {
    try {
      Object.keys(window[store]).filter(ours).forEach((key) => window[store].removeItem(key));
    } catch { /* storage unavailable */ }
  }
  const parent = location.hostname.split('.').slice(-2).join('.');
  document.cookie.split(';').map((c) => c.split('=')[0].trim()).filter(ours).forEach((name) => {
    for (const domain of ['', `; domain=.${parent}`, `; domain=${location.hostname}`]) {
      document.cookie = `${name}=; max-age=0; path=/${domain}`;
    }
  });
}

function choose(choice) {
  const previous = readChoice();
  saveChoice(choice);
  document.getElementById('qs-consent')?.remove();
  if (choice === 'yes') {
    analytics.optInCapturing();
  } else if (previous === 'yes') {
    analytics.optOutCapturing();
    clearAnalyticsData();
  }
}

function showBanner() {
  if (document.getElementById('qs-consent')) return;

  const style = document.createElement('style');
  style.textContent = `
    #qs-consent {
      position: fixed; z-index: 1000; left: 16px; right: 16px; bottom: 16px;
      max-width: 560px; margin: 0 auto; padding: 14px 18px;
      display: flex; flex-wrap: wrap; align-items: center; gap: 12px;
      background: #1a1a1f; border: 1px solid #2a2a32; border-radius: 14px;
      box-shadow: 0 8px 30px rgba(0, 0, 0, 0.5); text-align: left;
      font: 0.85rem/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }
    #qs-consent p { flex: 1 1 260px; margin: 0; color: #c0c0d0; font-size: inherit; }
    #qs-consent a { color: #8884ff; text-decoration: underline; }
    #qs-consent div { display: flex; gap: 8px; }
    #qs-consent button {
      cursor: pointer; padding: 7px 16px; border-radius: 9px;
      border: 1px solid #6e6af5; background: transparent; color: #f0f0f5;
      font: inherit; font-weight: 600;
    }
    #qs-consent button:hover { background: #6e6af5; color: #fff; }
  `;

  const banner = document.createElement('section');
  banner.id = 'qs-consent';
  banner.setAttribute('aria-label', 'Analytics consent');
  banner.innerHTML = `
    <p>May we use analytics cookies to see how this site is used? <a href="/privacy">Privacy policy</a></p>
    <div>
      <button type="button" data-choice="no">Decline</button>
      <button type="button" data-choice="yes">Allow</button>
    </div>
  `;
  banner.addEventListener('click', (event) => {
    const button = event.target.closest('button[data-choice]');
    if (button) choose(button.dataset.choice);
  });

  document.head.appendChild(style);
  document.body.appendChild(banner);
}

// "Change your analytics choice" buttons (on the privacy page).
document.querySelectorAll('[data-analytics-settings]').forEach((button) => {
  button.hidden = false;
  button.addEventListener('click', showBanner);
});

const choice = readChoice();
if (choice === 'yes') analytics.optInCapturing();
else if (choice !== 'no') showBanner();
