```javascript
import { config } from './config.js';

class Agent {
    constructor() {
        this.name = "Booker";
    }

    async getResponse(query) {
        const response = await fetch(config.backendUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ query: query })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        return data.response;
    }
}

const agent = new Agent();

document.getElementById('submit-button').addEventListener('click', async () => {
    const query = document.getElementById('customer-input').value;
    const response = await agent.getResponse(query);
    display_response(response);
});

function display_response(response) {
    const responseContainer = document.getElementById('agent-response');
    responseContainer.textContent = response;
}

export { agent };
```