import os

def get_path(filename) -> str:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)
    return file_path

def madlib(filename):
    story = ""
    with open(get_path(filename), "r") as file:
        story = file.read()

    words = {}
    begin_symb = "<"
    end_symb = ">"
    word_start = -1
    
    for i, char in enumerate(story):
        if char == begin_symb:
            word_start = i
        elif char == end_symb and (word_start != -1):
            word = story[word_start:i+1]
            words[word] = ""
            word_start = -1

    for key in words:
        repl = input("Enter a word to replace " + key + ": ")
        words[key] = repl

    for word, repl in words.items():
        story = story.replace(word, repl)

    return story

print(madlib("story.txt"))
