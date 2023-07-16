```python
from edgegpt import EdgeGPT
from config import config

class EdgeGPTModel:
    def __init__(self):
        self.model = EdgeGPT(
            api_key=config['bingai_api_key'],
            model_name=config['model_name'],
            use_gpu=config['use_gpu']
        )

    def generate_response(self, prompt):
        response = self.model.generate(prompt)
        return response

edgegpt_model = EdgeGPTModel()
```