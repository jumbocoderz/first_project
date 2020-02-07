from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):

    # getting text from index.html
    djtext = request.GET.get('text','default')
    
    # getting checkbox values
    removepunc = request.GET.get('removepunc','off') 
    uppercasefirstletter = request.GET.get('uppercasefirstletter','off')
    uppercase = request.GET.get('uppercase','off')
    spaceremover = request.GET.get('sapceremover','off')
    newlineremover = request.GET.get('newlineremover','off')

    analyze=""

    if removepunc == 'on' :
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext :
            if char not in punctuations :
                analyze = analyze + char
        djtext = analyze
        analyze = ""

    if uppercasefirstletter == 'on' :
        for index, char in enumerate(djtext) :
            if djtext[index-1] == " " or index == 0 or djtext[index-1]=='\n':
                analyze = analyze + djtext[index].upper()
            else :
                analyze = analyze + djtext[index]
        djtext = analyze
        analyze = ""       

    if uppercase == 'on' :
        for char in djtext :
            analyze = analyze + char.upper()
        djtext = analyze
        analyze = ""

    if spaceremover == 'on' :
        for index, char in enumerate(djtext) : 
            if not(djtext[index]==" " and djtext[index+1] == " ") :
                analyze = analyze + char
        djtext = analyze
        analyze = ""

    if newlineremover == 'on' :
        flag = 0 
        for char in djtext :
            if char != '\n' and char != '\r' :
                flag = 0
                analyze = analyze + char
            if char == '\n' and flag == 0:
                flag = 1
                analyze = analyze + ' '
        djtext = analyze
        analyze = ""

    params = { 'djtext' : djtext }
    return render(request, 'analyze.html', params)