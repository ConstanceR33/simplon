import tensorflow as tf
from transformers import GPT2Tokenizer, TFGPT2LMHeadModel
from fastapi import FastAPI

app = FastAPI()


tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = TFGPT2LMHeadModel.from_pretrained('gpt2', pad_token_id=tokenizer.eos_token_id)

@app.post("/")
async def transform(prompt:str):
    input_ids = tokenizer.encode(prompt, return_tensors='tf')

    # Générer du texte
    outputs = model.generate(
        input_ids=input_ids,
        max_length=200,
        do_sample=True,
        top_p=0.95,
        top_k=50)

    # Convertir les output_ids en texte
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {'result' : text}
