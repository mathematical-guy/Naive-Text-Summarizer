import requests
import PyPDF2


FilePath = "Enter pdf file path here"
with open(FilePath, 'rb') as fileObject:
    readerObject = PyPDF2.PdfFileReader(fileObject)
    text = ''
    for i in range(1, 10):
        text += readerObject.getPage(i).extractText()
    
r = requests.post("https://api.deepai.org/api/summarization", 
                data={'text': text}, 
                headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
                )

print(r.json())