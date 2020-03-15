# words = input("Введите текст: ").split()
# list_ = []
# print(words)
# for word in min(words):
#     # res_pop = words.pop(word)
#     list_.append(word)
#     words.pop()
# print(list_)

words = input("Введите текст: ").split()
words.sort(key = len)
print(words)
