sentences = {
    'Kim': 'Nutmeg rolled in a bed of flowers. ',
    'Tijuan': 'Nutmeg jumped over the moon. ',
    'Allison': 'Nutmeg patrols the neighborhood for gremlins. ',
    'Chris': 'Nutmeg races for pink slips against Dominic Torreto. ',
}

# for name, sentence in sentences.items():
#     print(name + ': ' + sentence)

class Sentence:
    def __init__(self, author, text):
        self.author = author
        self.text = text

    def __str__(self):
        return f'{self.text}, by: {self.author}'

class Paragraph:
    def __init__(self, sentence_dict):
        self.sentence_list = []
        for name, words in sentence_dict.items():
            self.sentence_list.append(Sentence(name, words))
        self.content = ''
        for sentence_instance in self.sentence_list:
            self.content += sentence_instance.text

my_new_paragraph = Paragraph(sentences)

print(my_new_paragraph.content)
print(my_new_paragraph.sentence_list)




# for sentence in our_sentences:
#     print(sentence)


