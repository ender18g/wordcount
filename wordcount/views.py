from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')    

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    numwords = len(wordlist)
    word_dict = {}

    for word in wordlist:
        word = word.lower()
        if word_dict.get(word):
            word_dict[word] +=1
        else:
            word_dict[word]=1
    wordlist = word_dict.items()

    wordlist = sorted(wordlist, key=lambda v:v[1],reverse=True)

    return render(request,'count.html', {'fulltext':fulltext, 'numwords':numwords, 'wordlist':wordlist})
