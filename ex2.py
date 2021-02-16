import pickle
import xml.etree.ElementTree as ET

path = 'books.xml'
tree = ET.parse(path)
root = tree.getroot()


class Book:

    def __init__(self, author, title, genre, price, publish_date, description):
        self.author = author
        self.title = title
        self.genre = genre
        self.price = price
        self.publish_date = publish_date
        self.description = description

    def getauthor(self):
        return self.author

    def gettitle(self):
        return self.title

    def getgenre(self):
        return self.genre

    def getprice(self):
        return self.price

    def getpublishdate(self):
        return self.publish_date

    def getdescription(self):
        return self.description

# https://www.geeksforgeeks.org/xml-parsing-python/

