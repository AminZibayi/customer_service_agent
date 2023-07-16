```python
from flask import Flask, request, jsonify
from edgegpt import edgegpt_model
from data_processor import process_query
from customer_service import customer_service
from config import config

app = Flask(__name__)

@app.route('/api/query', methods=['POST'])
def handle_customer_query():
    data = request.get_json()
    query = data.get('query')

    processed_query = process_query(query)
    response = customer_service.handle_query(processed_query)

    return jsonify(response)

if __name__ == '__main__':
    app.run(host=config['HOST'], port=config['PORT'])
```