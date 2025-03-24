from flask import Flask, render_template
import requests
import random

app = Flask(__name__)

# Credenciales de Imgflip
IMGFLIP_USERNAME = "arath04"
IMGFLIP_PASSWORD = "10112004aJ"

# Lista de plantillas populares
TEMPLATES = {
    "Drake": "181913649",
    "Two Buttons": "87743020",
    "Distracted Boyfriend": "112126428",
    "Expanding Brain": "93895088",
    "Mocking Spongebob": "102156234",
}

# Lista de frases aleatorias
PHRASES = [
    ("Nadie:", "Absolutamente nadie:"),
    ("Cuando intentas programar en viernes", "Pero falla en producción"),
    ("Código en local:", "Código en producción:"),
    ("Cuando el código funciona", "Pero no sabes por qué"),
]

def generar_meme():
    """Genera un meme aleatorio con Imgflip API."""
    template_id = random.choice(list(TEMPLATES.values()))
    top_text, bottom_text = random.choice(PHRASES)

    url = "https://api.imgflip.com/caption_image"
    params = {
        "template_id": template_id,
        "username": IMGFLIP_USERNAME,
        "password": IMGFLIP_PASSWORD,
        "text0": top_text,
        "text1": bottom_text,
    }

    response = requests.post(url, data=params)
    data = response.json()

    if data["success"]:
        return data["data"]["url"]
    return None

@app.route("/")
def home():
    meme_url = generar_meme()
    return render_template("index.html", meme_url=meme_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
