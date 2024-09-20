from googletrans import Translator
import requests
from bs4 import BeautifulSoup

translator = Translator()
url = "https://randomword.com/"

response = requests.get(url)


# define the function to get information from the url
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        soup = BeautifulSoup(response.content, "html.parser")
        english_words = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    except:
        print("Error")


# define the function to create the game
def word_game():
    print("Welcome to the game!")
    while True:
        word_dict = get_english_words()
        word = word_dict.get("english_words")
        result1 = translator.translate(word, dest="ru")  #using the Translate method according to the task
        word_definition = word_dict.get("word_definition")
        result2 = translator.translate(word_definition, dest="ru")

        print(f"The meaning of the word - {result2.text}")
        user = input("What for a word is it? ")
        if user == word:
            print("That`s right!")
        else:
            print(f"False, the right word is {result1.text}")

        play_again = input("Wanna play again? y/n")
        if play_again != "y":
            print("Thanks for playing!")
            break


word_game()
