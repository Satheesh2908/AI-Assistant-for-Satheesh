# Example correction inside the Helper module
from google.generativeai import ChatCompletion  # or the correct import from the library you are using

def llm_model_object(api_key):
    try:
        # Correctly initialize your model here
        client = ChatCompletion(api_key=api_key)  # Assuming `ChatCompletion` is the correct model class
        return client
    except Exception as e:
        print(f"Failed to initialize the model: {e}")
        return None

