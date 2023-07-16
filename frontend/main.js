```javascript
import { agent } from './agent.js';
import { config } from './config.js';

document.addEventListener('DOMContentLoaded', () => {
    const inputField = document.getElementById('customer-input');
    const submitButton = document.getElementById('submit-button');

    submitButton.addEventListener('click', () => {
        const customerQuery = inputField.value;
        submitQuery(customerQuery);
    });
});

function submitQuery(query) {
    fetch(`${config.backendUrl}/query`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query })
    })
    .then(response => response.json())
    .then(data => {
        document.dispatchEvent(new CustomEvent('response-received', { detail: data }));
    })
    .catch(error => console.error('Error:', error));
}

document.addEventListener('response-received', (event) => {
    agent.displayResponse(event.detail);
});
```