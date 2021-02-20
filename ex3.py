import pickle
from xml.dom import minidom
import xml.etree.ElementTree as ET

# sabem que l'estructura dels objectes és la següent:
# String Categoria
# String Titulo
# String Autor
# Date Año
# Float Precio


class PtU2:

    def __init__(self):
        pass


def main():
    archivo = input("Dime el nombre del archivo:  ")
    parsefile(archivo)

# sale error ModuleNotFoundError: No module named 'PtU2'
# me imagino que hay algo en el archivo externlibrary.dat que requiere ese modulo
# no se a que se refiere o como arregarlo
# pero creo que la estructura es correcta y deberia funcionar si no fuera por eso


def parsefile(archivo):
    # abre el archivo indicado en el main
    books = pickle.load(open(archivo, mode='rb'))
    data = ET.Element('books')
    # parsea los datos y saca la informacion de cada libro
    for book in books:
        items = ET.SubElement(data, 'book')
        print(str.format("Category: {0}, Title: {1}, Author: {2}, Publish date: {3}, Price: {4},", book.getgenre(),
                         book.gettitle(), book.getauthor(), book.getpublishdate(), book.getprice()))
        item1 = ET.SubElement(items, 'Category')
        item2 = ET.SubElement(items, 'Title')
        item3 = ET.SubElement(items, 'Author')
        item4 = ET.SubElement(items, 'Publish date')
        item5 = ET.SubElement(items, 'Price')
        item1.text = str(book.getgenre())
        item2.text = str(book.gettitle())
        item3.text = str(book.getauthor())
        item4.text = str(book.getpublishdate())
        item5.text = str(book.getprice())
    temp = ET.tostring(data)
    xml = minidom.parseString(temp)
    # crea un archivo xml con toda la informacion parseada antes
    xmlfile = open("libros.xml", "w")
    xmlfile.write(xml.toprettyxml(encoding="utf-8").decode("utf-8"))


if __name__ == "__main__":
    main()
