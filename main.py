import yaml

import torch
from transformers import MarianMTModel, MarianTokenizer


MARKET_MIXUP_YAML ="""
level: A2

title:
  en: "Market Mix-Up"
  es: "Confusión en el Mercado"

summary:
  en: "Join Elena navigating a market, encountering amusing mix-ups. Laughter and learning, discover the joy of communication across cultures."
  es: "Únete a Elena mientras navega por un bullicioso mercado, encontrándose con divertidas confusiones. Entre risas y aprendizaje, descubre la alegría de la comunicación entre culturas."

conversation:
  - en: "You enter the bustling market, greeted by the lively atmosphere."
    es: "Entras al bullicioso mercado, recibido por la animada atmósfera."
  - en: "Alayna, the vendor, smiles and says, '¡Hola!'"
    es: "Alayna, la vendedora, sonríe y dice, 'Hello!'"
  - en: "You return the greeting, 'Hola Alayna! ¿Cómo estás hoy?'"
    es: "Devuelves el saludo, 'Hi Alayna! How are you today?'"
  - en: "Alayna beams, '¡Buenos días! Mi día está siendo excelente, ¡gracias por preguntar!'"
    es: "'Good morning! My day is going great, thank you for asking!'"
  - en: "'That's wonderful to hear!' you reply. '¿Cómo ha sido tu día en el mercado?'"
    es: "'¡Qué maravilloso escuchar eso!' respondes. 'How has your day been at the market?'"
"""

MARKET_MIXUP = yaml.safe_load(MARKET_MIXUP_YAML)

def translate_text_to_audio(text):
    # Load pre-trained translation model
    model_name = "Helsinki-NLP/opus-mt-en-es"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    # Tokenize input text
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)

    # Perform translation
    outputs = model.generate(**inputs)

    # Decode the translated output
    translated_text = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]

    # Output translated text
    print("Translated Text:", translated_text)

    # Convert translated text to audio
    from gtts import gTTS
    import IPython.display as ipd

    tts = gTTS(translated_text, lang='es')
    tts.save("translated_audio.mp3")

    # Display the audio
    ipd.display(ipd.Audio("translated_audio.mp3"))


def market_mixup():
    """
    This function translates the English text to Spanish and converts it to audio.
    """
    # Translate the English text to Spanish
    translate_text_to_audio(MARKET_MIXUP["summary"]["en"])

    # Translate the English conversation to Spanish
    for line in MARKET_MIXUP["conversation"]:
        translate_text_to_audio(line["en"])


if __name__ == "__main__":
    #
    # Example usage
    #
    input_text = input("Enter the English text to translate and convert to audio: ")
    translate_text_to_audio(input_text + " was what you entered.")

    market_mixup()
