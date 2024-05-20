import threading

class LLMModel:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._initialize(*args, **kwargs)
        return cls._instance

    def _initialize(self, model_path, **generation_params):
        # Initial model loading logic
        self.load_model(model_path, **generation_params)

    def load_model(self, model_path, **generation_params):
        # Logic to load the model from the model_path with generation_params
        self.model_path = model_path
        self.generation_params = generation_params
        # Here you would load the model from the file system or a URL
        print(f"Loading model from {model_path} with params {generation_params}")
        # Placeholder for actual model loading
        self.model = self._load_model_from_path(model_path, generation_params)

    def _load_model_from_path(self, model_path, generation_params):
        # This is a placeholder function where you would implement the actual
        # model loading logic.
        # Add factories here to ensure we can utilize different sources models.
        return "Loaded Model"  # Replace with actual model loading

    def reload_model(self, model_path, **new_generation_params):
        # Method to reload the model with new parameters and path
        self.load_model(model_path, **new_generation_params)

    # Example of other methods that use the loaded model
    def generate_text(self, prompt):
        # Use self.model and self.generation_params to generate text
        return f"Generated text based on prompt: {prompt}"


