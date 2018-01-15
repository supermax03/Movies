#TODO: Add Google book api
import requests

class GoogleBook:
     __url__="https://www.googleapis.com/books/v1/volumes?q={0}"
     @staticmethod
     def getbooks(term):
                 page=requests.get(GoogleBook.__url__.format(term))
                 return page.content
