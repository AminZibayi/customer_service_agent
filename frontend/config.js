const config = {
    apiEndpoint: 'http://localhost:5000/api',
    agentName: 'Booker',
    domElements: {
        customerInput: 'customer-input',
        agentResponse: 'agent-response',
        submitButton: 'submit-button'
    },
    eventNames: {
        querySubmitted: 'query-submitted',
        responseReceived: 'response-received'
    }
};

export default config;