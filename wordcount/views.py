from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    #".GET" gets the stuff by their "name tag" from the pervious html page

    wordlist = fulltext.split()
    #"split" splits any text into a list containing the word in it

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sortedlist = sorted(worddictionary.items(), key = operator.itemgetter(1), reverse=True)
    #that "operator.itemgetter(1)" part is just something to be looked up the next time sorting is used
    #"reverse" just reversed the sorted list.

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'sortedlist': sortedlist})
