// Message/Notification Timer Functionality
let messageTimeout = document.getElementById("message-timer");

setTimeout(() => {
    messageTimeout.style.display = "none";
}, 5000);

// AI Chat Functionality
const chatForm = document.getElementById('chat-form');
const chatInput = document.getElementById('chat-input');
const chatHistory = document.getElementById('chat-history');

chatForm.addEventListener('submit', function(event) {
    event.preventDefault();
    const message = chatInput.value.trim();
    if (message) {
        const messageWrapper = document.createElement('div');
        messageWrapper.classList.add('chat-message', 'user');

        const messageElement = document.createElement('div');
        messageElement.classList.add('message', 'user');
        messageElement.textContent = message;

        messageWrapper.appendChild(messageElement);
        chatHistory.appendChild(messageWrapper);
        chatInput.value = '';

        fetch('/chat/response/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({
                'csrfmiddlewaretoken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                'message': message
            })
        })
        .then(response => response.json())
        .then(data => {
            const response = data.response;
            const messageWrapperAi = document.createElement('div');
            messageWrapperAi.classList.add('chat-message', 'ai');

            const messageElementAi = document.createElement('div');
            messageElementAi.classList.add('message', 'ai');
            messageElementAi.innerHTML = DOMPurify.sanitize(response);

            messageWrapperAi.appendChild(messageElementAi);
            chatHistory.appendChild(messageWrapperAi);
        })
        .catch(error => {
            console.error('Error:', error);
        });
        chatHistory.scrollTop = chatHistory.scrollHeight;
    }
});
