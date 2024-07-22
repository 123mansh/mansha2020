import gradio as gr
from googletrans import Translator

def translate_word(word):
    if len(word) != 10:
        return {"Error": "Please enter a 10-letter word."}

    translator = Translator()
    translations = {}
    target_languages = {'French': 'fr', 'Hindi': 'hi'}
    
    for lang_name, lang_code in target_languages.items():
        translated = translator.translate(word, dest=lang_code)
        translations[lang_name] = translated.text
    
    return translations

interface = gr.Interface(
    fn=translate_word,
    inputs="text",
    outputs="json",
    title="10-Letter Word Translator",
    description="Enter a 10-letter English word to get its translations in French and Hindi."
)

if __name__ == "__main__":
    interface.launch()
