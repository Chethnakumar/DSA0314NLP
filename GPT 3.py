import openai

# Set your OpenAI API key
openai.api_key = 'your-api-key-here'

# Function to generate text using GPT-3
def generate_text(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",  # You can use other models like "gpt-3.5-turbo"
        prompt=prompt,
        max_tokens=150  # Adjust the number of tokens as needed
    )
    return response.choices[0].text.strip()

# Example usage
prompt = "Once upon a time in a land far, far away"
generated_text = generate_text(prompt)
print(generated_text)
