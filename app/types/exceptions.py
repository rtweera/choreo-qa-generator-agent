class APIKeyNotFoundError(Exception):
    """Raised when a required API key is not found in the environment"""
    
    def __init__(self, key_name):
        self.key_name = key_name
        self.message = f"API key not found: {key_name} environment variable is not set"
        super().__init__(self.message)


class InvalidModelProviderError(Exception):
    """Raised when the given Model provider name is invalid"""

    def __init__(self, provider_name):
        self.provider_name = provider_name
        self.message = f"Invalid model provider name: {provider_name} is not a valid model provider"


class InvalidModelNameError(Exception):
    """Raised when the given Model name is invalid"""

    def __init__(self, model_name):
        self.model_name = model_name
        self.message = f"Invalid model name: {model_name} is not a valid model name"