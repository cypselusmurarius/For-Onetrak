# P.s. вывод в программе использован для наглядности

str = input()

def StringEvaluator(s):
    sentences = s.split('. ') # выделение предложений из строки в массив
    words = s.split(' ') # выделение слов из строки в массив
    qSentences = len(sentences) # кол-во предложений
    qWords = len(words) # кол-во слов

    return (sentences, words, qSentences, qWords)

print(StringEvaluator(str))
