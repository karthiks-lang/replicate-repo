from cog import BasePredictor, Input

class Predictor(BasePredictor):
    def predict(
        self,
        text: str = Input(description="Text input")
    ) -> str:
        return f"Hello from Replicate! You said: {text}"
