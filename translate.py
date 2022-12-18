# Importing necessary modules required
import googletrans
from googletrans import Translator

# Getting input in English
MyText = input("Enter your input: ")
MyText = MyText.lower()

#Getting the language to translate to
print("\n\nList of languages supported for translation")
print(googletrans.LANGUAGES)

lang = input("\n\nEnter language to be translated to in shorthand notation: ")

# Translator method for translation
translator = Translator()

print("\nPhase to be Translated :"+ MyText)

text_to_translate = translator.translate(MyText, src= 'en', dest= lang)
text = text_to_translate.text
print("\n",text)
