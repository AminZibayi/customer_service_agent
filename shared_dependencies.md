**Shared Dependencies**

1. **Exported Variables**
   - `app` (Flask instance) in `backend/app.py`
   - `edgegpt_model` (EdgeGPT model instance) in `backend/edgegpt.py`
   - `customer_service` (CustomerService class instance) in `backend/customer_service.py`
   - `config` (Configuration variables) in `backend/config.py`

2. **Data Schemas**
   - `CustomerQuery` (Schema for customer queries) in `backend/data_processor.py`
   - `CustomerResponse` (Schema for agent responses) in `backend/customer_service.py`

3. **DOM Element IDs**
   - `customer-input` (Text input for customer queries) in `frontend/index.html`
   - `agent-response` (Container for agent responses) in `frontend/index.html`
   - `submit-button` (Button for submitting queries) in `frontend/index.html`

4. **Message Names**
   - `query-submitted` (Event when a customer submits a query) in `frontend/main.js`
   - `response-received` (Event when a response is received from the backend) in `frontend/agent.js`

5. **Function Names**
   - `process_query` (Function to process customer queries) in `backend/data_processor.py`
   - `generate_response` (Function to generate responses using EdgeGPT) in `backend/edgegpt.py`
   - `handle_query` (Function to handle customer queries and generate responses) in `backend/customer_service.py`
   - `submit_query` (Function to submit customer queries from the frontend) in `frontend/main.js`
   - `display_response` (Function to display agent responses on the frontend) in `frontend/agent.js`