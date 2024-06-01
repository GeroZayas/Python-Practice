import marimo

__generated_with = "0.6.13"
app = marimo.App(width="medium")


@app.cell
def __():
    def sort_numbers(numbers_disordered):
        len_lista = len(numbers_disordered)
        for i in range(len_lista):
            for j in range(0, len_lista-i-1):
                siguiente_num = j + 1
                if numbers_disordered[j] > numbers_disordered[siguiente_num]:
                    numbers_disordered[j], numbers_disordered[siguiente_num] = numbers_disordered[siguiente_num], numbers_disordered[j]
        return numbers_disordered
    return sort_numbers,


@app.cell
def __(sort_numbers):
    numbers_disordered = [4, 1, 6, 43, 16, 88, 2, 100]
    list_ordered = sort_numbers(numbers_disordered)
    print(list_ordered)
    return list_ordered, numbers_disordered


@app.cell
def __():
    def sort_string(shakespeare):
        # List of punctuation marks to remove
        punctuation_marks = ['.', ',', '!', '?', ':', ';', '-', '(', ')', '"', "'"]

        # Remove punctuation marks
        cleaned_text = ''.join(char for char in shakespeare if char not in punctuation_marks)

        # Split the sentence into words
        words = cleaned_text.split()

        # Sort the words alphabetically (case-insensitive)
        words_sorted = sorted(words, key=lambda word: word.lower())

        # Join the sorted words back into a string
        string_sorted = ' '.join(words_sorted)

        return string_sorted

    shakespeare = 'All the world is a stage, and all the men and women merely players. They have their exits and their entrances, And one man in his time plays many parts.'
    string_sorted = sort_string(shakespeare)
    print(string_sorted)
    return shakespeare, sort_string, string_sorted


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
