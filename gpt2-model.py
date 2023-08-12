from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained model and tokenizer
model_name = "gpt2"  # You can also use "gpt2-medium", "gpt2-large", "gpt2-xl" for larger models
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Example text for generating continuation
input_text = "Once upon a time"

# Encode the input text
input_ids = tokenizer.encode(input_text, return_tensors="pt")

# Generate text continuation
output = model.generate(input_ids, max_length=100, num_return_sequences=1)

# Decode and print the generated text
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(generated_text)


# pip install transformers