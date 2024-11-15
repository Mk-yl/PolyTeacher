import os
import google.generativeai as genai

API_KEY = os.getenv("API_KEY")
if API_KEY is None:
        raise ValueError("La clé API n'est pas définie dans les variables d'environnement")


genai.configure(api_key=API_KEY)


model = genai.GenerativeModel("gemini-1.5-flash")


response = model.generate_content("Écrit une la traduction de j'ai faim j'ai envie d'un bon poulet curry.")

print(response.text)
