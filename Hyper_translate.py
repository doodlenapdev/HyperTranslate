import random
from googletrans import LANGUAGES, Translator
import asyncio



async def translate(times, language_orig, language_final, text_orig):
    languages = [lang for lang in LANGUAGES.keys() if lang != language_orig]
    
    text1 = text_orig
    language_src = language_orig
    translator = Translator()  

    while times > 1:
        
        language_dest = random.choice(languages)
        
        
        resultado = await translator.translate(text1, src=language_src, dest=language_dest)

        
        text1 = resultado.text
        language_src = language_dest

        times -= 1

    
    result_final = await translator.translate(text1, src=language_src, dest=language_final)
    
    
    print(f"\nTranslated text: {result_final.text}")


def main():
  times = int(input("How many times do you wish to translate: "))
  language_orig = input("Original language: ")
  language_final = input("Final language: ")
  text_orig = input("\nText to be translated: ")

    
  asyncio.run(translate(times, language_orig, language_final, text_orig))


if __name__ == "__main__":
    main()