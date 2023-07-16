```python
import json
from typing import Dict

class CustomerQuery:
    def __init__(self, query_data: Dict):
        self.customer_id = query_data.get('customer_id')
        self.query_text = query_data.get('query_text')
        self.timestamp = query_data.get('timestamp')

    def process_query(self):
        # Process the query text and extract necessary information
        # This can be extended to include more complex processing like NLP, sentiment analysis etc.
        processed_query = self.query_text.lower()
        return processed_query

def load_rules():
    # Load the rules and guidelines from a JSON file
    with open('rules.json', 'r') as f:
        rules = json.load(f)
    return rules

def apply_rules(query: str, rules: Dict):
    # Apply the rules to the query and return the relevant ones
    relevant_rules = [rule for rule in rules if rule in query]
    return relevant_rules
```