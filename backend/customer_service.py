```python
from flask import Flask, request, jsonify
from edgegpt import edgegpt_model
from data_processor import process_query
from config import config

class CustomerService:
    def __init__(self, name="Booker"):
        self.name = name

    def handle_query(self, query):
        processed_query = process_query(query)
        response = self.generate_response(processed_query)
        return response

    def generate_response(self, processed_query):
        response = edgegpt_model.generate(processed_query)
        return response

customer_service = CustomerService()

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query():
    data = request.get_json()
    query = data['query']
    response = customer_service.handle_query(query)
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(host=config['host'], port=config['port'])
```