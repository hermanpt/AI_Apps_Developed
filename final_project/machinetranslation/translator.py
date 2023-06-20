from deep_translator import MyMemoryTranslator


translator = MyMemoryTranslator(source="english", target="french")


def english_to_french(english_text: str) -> str:
    french_text = translator.translate(english_text)
    return french_text


translator2 = MyMemoryTranslator(source="french", target="english")


def french_to_english(french_text: str) -> str:
    english_text = translator2.translate(french_text)
    return english_text


if __name__ == '__main__':
    MyMemoryTranslator.deep_translator()
