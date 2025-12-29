import ollama

def lokale_chatbot():
    print("Lokale Bot (Llama 3): Stel een vraag! (Typ 'stop' om te stoppen)")
    
    # Zorg dat je eerst in je terminal 'ollama pull llama3' hebt gedaan
    model_naam = "llama3" 
    chat_history = []

    while True:
        user_input = input("Jij: ")
        
        if user_input.lower() == "stop":
            break

        # Voeg bericht toe aan geschiedenis
        chat_history.append({'role': 'user', 'content': user_input})

        try:
            print("Bot is aan het nadenken...", end="\r")
            
            # Stuur de vraag naar je lokale Ollama instantie
            response = ollama.chat(model=model_naam, messages=chat_history)
            
            bot_antwoord = response['message']['content']
            
            # Wis de "nadenken" tekst en toon antwoord
            print(f"Bot: {bot_antwoord}")

            # Voeg antwoord toe aan geschiedenis
            chat_history.append({'role': 'assistant', 'content': bot_antwoord})
            
        except Exception as e:
            print(f"\nEr ging iets mis. Heb je Ollama wel opgestart? Fout: {e}")

if __name__ == "__main__":
    lokale_chatbot()