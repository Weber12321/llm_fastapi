import settings
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from models.llm import LLMModel


class ModelInfo(BaseModel):
    model_name: str
    model_param: dict

class Prompt(BaseModel):
    prompt: str

app = FastAPI()

model = LLMModel(
    model_path=settings.MODEL_CONFIG["LLAMA3"]["model_path"], 
    param1=settings.MODEL_CONFIG["LLAMA3"]["model_config"]["param"]
)

@app.get("/model")
def get_model_info():
    return model.get_current_model_info()

@app.post("/infer")
def inference(prompt: Prompt):
    return model.generate_text(prompt.prompt)

@app.post("/switch_model")
def switch_model(model_info: ModelInfo):
    model_name = model_info.model_name.upper()
    model_param = model_info.model_param
    if not model_name in settings.MODEL_CONFIG:
        raise ValueError(f"Model {model_name} not found in settings")
    model.reload_model(
        model_path=settings.MODEL_CONFIG[model_name]["model_path"],
        param1=settings.MODEL_CONFIG[model_name]["model_config"]["param"]
    )
    return {"message": f"Switched to model {model_name}"}