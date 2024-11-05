from pprint import pprint


class WordsFinder:
    def __init__(self,*file_names):
        self.file_names=file_names

    def get_all_words(self):
        all_words={}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                words = []
                for line in file:
                    line_ = ''
                        # [',', '.', '=', '!', '?', ';', ':', ' - '])
                    for char in line:
                        if char not in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                            line_+=char
                    words+=(line_.lower()).split()
                all_words.update({file_name:words})
        return all_words
    def find(self,word):
        dict_={}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                dict_.update({name:(words.index(word.lower())+1)})
            else:
                print("Такого слова нет")
                return None
        return dict_
    def count(self, word):
        dict_={}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                dict_.update({name: words.count(word.lower())})
            else:
                print("Такого слова нет")
                return None
        return dict_
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
#                       'Rudyard Kipling - If.txt',
#                       'Mother Goose - Monday’s Child.txt')
# print(finder1.get_all_words())
# print(finder1.find('the'))
# print(finder1.count('the'))