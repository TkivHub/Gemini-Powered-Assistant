const chatForm = document.getElementById('chat-form');
const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');
const resetBtn = document.getElementById('reset-btn');

function removeEmptyState() {
  const empty = document.querySelector('.empty-state');
  if (empty) empty.remove();
}

function addMessage(role, content) {
  removeEmptyState();
  const div = document.createElement('div');
  div.className = `message ${role}`;
  const avatarLabel = role === 'user' ? 'Tu' : 'IA';
  div.innerHTML = `
    <div class="avatar ${role}">${avatarLabel}</div>
    <div class="bubble">${content}</div>
  `;
  chatBox.appendChild(div);
  chatBox.scrollTop = chatBox.scrollHeight;
}

chatForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  const message = userInput.value.trim();
  if (!message) return;

  addMessage('user', message);
  userInput.value = '';

  const res = await fetch('/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message }),
  });
  const data = await res.json();
  addMessage('assistant', data.success ? data.message : 'Error: ' + data.message);
});

resetBtn.addEventListener('click', async () => {
  await fetch('/reset', { method: 'POST' });
  chatBox.innerHTML = `
    <div class="empty-state">
      <h1>ALFHEIMR</h1>
      <p>Escribe cualquier pregunta para comenzar la conversacion.</p>
    </div>
  `;
});

// Modal "Acerca del nombre"
const aboutBtn = document.getElementById('about-btn');
const aboutModal = document.getElementById('about-modal');
const closeModal = document.getElementById('close-modal');

aboutBtn.addEventListener('click', () => {
  aboutModal.classList.remove('hidden');
});

closeModal.addEventListener('click', () => {
  aboutModal.classList.add('hidden');
});

aboutModal.addEventListener('click', (e) => {
  if (e.target === aboutModal) {
    aboutModal.classList.add('hidden');
  }
});