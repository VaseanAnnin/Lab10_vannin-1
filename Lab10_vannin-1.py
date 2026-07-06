"""
Word Count
Vasean Annin

This program displays a menu of 4 text files. 
Once the user chooses a text file the application will read the file
and count the frequency of every word and print an alphabetical report 

"""

from pathlib import Path
import string

class WordAnalyzer:

    def __init__(self, filepath):
        self.__filepath = Path(filepath)
        self.__frequency = {}
        

    def process_file(self):
        try:
            if self.__filepath.exists() == False:
                raise FileNotFoundError
            
            translator = str.maketrans("","",string.punctuation + "“”‘’—")
            with self.__filepath.open("r") as file:
                for line in file:
                    line = line.lower()
                    line = line.translate(translator)
                    words = line.split()

                    for word in words:
                        if word in self.__frequency:
                            self.__frequency[word] +=1
                        else:
                            self.__frequency[word] = 1

            return True
        except FileNotFoundError:
            print("File not found")
            return False
        
        





    def print_report(self):
        sorted_words = sorted(self.__frequency.keys())

        for word in sorted_words:
            print(f"{word: <10} :: {self.__frequency[word]}")

        

def main():
    files = {
            "1": ("Monte Cristo",Path("Monte Cristo Assessment.txt")),
            "2": ("Princess Mars",Path("Princess Mars Assessment.txt")),
            "3": ("Tarzan",Path("Tarzan Assessment.txt")),
            "4": ("Treasure Island",Path("Treasure Island Assessment.txt"))
    }

    running = True
    while running:
        print("--- Word Analyzer ---")
        print("Please select a file to analyze:")
        for key in files:
            print(f"{key}. {files[key][0]}")
        print("5. Exit")

        user_input = input("Enter your choice (1-5): ")

        if user_input == '5':

            running = False
        elif user_input not in files:
            print("Please enter a valid number")
            input("Press Enter to return to the menu...")

        else:
            file_path = files[user_input][1]
            analyzer = WordAnalyzer(file_path)

            result = analyzer.process_file()

            if result:
                analyzer.print_report()
                input("Press Enter to return to the menu...")

    print("Goodbye!")

main()
        





    