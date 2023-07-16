```python
import os

class Config:
    # Flask configuration
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    FLASK_DEBUG = os.getenv('FLASK_DEBUG', True)

    # EdgeGPT configuration
    EDGE_GPT_API_KEY = os.getenv('EDGE_GPT_API_KEY')
    EDGE_GPT_API_URL = os.getenv('EDGE_GPT_API_URL', 'https://api.bing.microsoft.com/v7.0/EdgeGPT')

    # Haminja configuration
    HAMINJA_API_KEY = os.getenv('HAMINJA_API_KEY')
    HAMINJA_API_URL = os.getenv('HAMINJA_API_URL', 'https://api.haminja.com')

    # Customer service configuration
    AGENT_NAME = os.getenv('AGENT_NAME', 'Booker')

config = Config()
```