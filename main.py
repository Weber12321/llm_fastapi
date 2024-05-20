import settings
from typing import Union

from fastapi import FastAPI
from models.llm import LLMModel

app = FastAPI()

model = LLMModel(
    model_path=settings.MODEL_CONFIG["LLAMA3"]["model_path"], 
    param1=settings.MODEL_CONFIG["LLAMA3"]["model_config"]["param"]
)

@app.get("/model")
def read_root():
    return {"Hello": "World"}

@app.post("/infer")
def inference(prompt: str):
    return model.generate_text(prompt)

@app.post("/switch_model")
def switch_model(model_name: str):
    model_name = model_name.upper()
    if not model_name in settings.MODEL_CONFIG:
        raise ValueError(f"Model {model_name} not found in settings")
    model.reload_model(
        model_path=settings.MODEL_CONFIG[model_name]["model_path"],
        param1=settings.MODEL_CONFIG[model_name]["model_config"]["param"]
    )
    return {"message": f"Switched to model {model_name}"}