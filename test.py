import ollama
print("Ollama module geladen!")

response = ollama.chat(
    model="llama3",
    messages=[{"role": "user", "content": "Zeg hallo"}]
)

print(response["message"]["content"])
