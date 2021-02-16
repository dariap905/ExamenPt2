import xml.etree.ElementTree as ET


class BuscarLibro:

    def __init__(self):
        pass


tree = ET.parse('books.xml')
root = tree.getroot()


def main():
    # estoy utilizando raw_input instead of input porque salia error SyntaxError: unexpected EOF while parsing
    nombre = raw_input("Dime el nombre del libro que quieres buscar: ")
    # nombre = 'Midnight Rain'
    idlibro = getbookidbyname(nombre)
    if idlibro is not None:
        buscarlibroporid(idlibro)
    else:
        print "Este libro no existe"


# devuelve el id del libro cuyo nombre ha coincidido con nuestra busqueda
def getbookidbyname(nombre):
    for book in root.findall('.//book[title="' + nombre + '"]'):
        bookid = book.attrib['id']
        return bookid


# muestra la informacion completa del libro segun su id
def buscarlibroporid(bookid):
    for book in root.findall('.//book[@id="' + str(bookid) + '"]'):
        print 'Author: ', book.find('author').text
        print 'Title: ', book.find('title').text
        print 'Genre: ', book.find('genre').text
        print 'Price: ', book.find('price').text
        print 'Publish date: ', book.find('publish_date').text
        print 'Description: ', book.find('description').text


if __name__ == "__main__":
    main()
