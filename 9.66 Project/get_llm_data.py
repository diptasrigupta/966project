import openai

# Set your API key here
api_key = "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"
openai.api_key = api_key

# Initialize an empty list to store the answers
answers = []

# Run the prompt 50 times and record the answers
for _ in range(50):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="It's very cold for summer in Boston. How cold is it?(provide an estimate - only a numerical answer in farenheit) Answer should be in format: xxF.",
        max_tokens=10,
        n=1,
    )
    answer = response.choices[0].text.strip()
    answers.append(answer)

# Save the recorded answers to a file
with open("llm_data/very_cold_summer.txt", "w") as file:
    for i, answer in enumerate(answers):
        file.write(f"Answer {i+1}: {answer}\n")

