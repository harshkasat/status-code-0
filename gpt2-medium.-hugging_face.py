from flask import Flask, request, jsonify
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import json

app = Flask(__name__)

# Load pre-trained model and tokenizer
model_name = "gpt2-xl"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

@app.route('/generate', methods=['POST'])
def generate_text():
    try:
        # Read JSON data from the request
        json_data = request.get_json()

        # Extract the value of the "input_text" key from the dictionary
        input_text = f'Give me the precautions for this disease {json_data.get("input_text", "")}'

        # Encode the input text
        input_ids = tokenizer.encode(input_text, return_tensors="pt")

        # Generate text continuation
        output = model.generate(input_ids, max_length=100, num_return_sequences=1)

        # Decode the generated text
        generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

        response = {"generated_text": generated_text}
        return jsonify(response), 200
    except Exception as e:
        a=jsonify({"error": str(e)}), 500
        print(a)
        return a

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
