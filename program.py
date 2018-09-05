from bs4 import BeautifulSoup
import openpyxl
import requests


def main():
    tag = input("Type the tagline we are looking for div, a, p, br, h1-h5")
    id = input("Is it a class? Y or N") == "Y"
    
    wb = openpyxl.load_workbook('urllist.xlsx')
    urllist = wb.active
    for i in range(1, 4):
        html = get_html(requests.get(urllist['A'+str(i+1)].value))
        classname = urllist['B'+str(i+1)].value
        if id:
            result = get_child_by_id(html, tag, classname)
        else:
            result = get_child_by_class(html, tag, classname)
        print(result)
        urllist['C'+str(i+1)] = str(result)
    wb.save('urllist.xlsx')
    # TODO: Create function to save result to docx

    # TODO: Create function to interact with Joomla site
    # TODO: Create function to interact with WordPress site
    # TODO: Create function to find out if its a Joomla, or wordpress site
    # TODO: Interact with local DB to find username and password

    # TODO: ULTIMATE GOAL have a function that can quickly transfer content from any website to a joomla site.


def get_html(html) -> BeautifulSoup:
    return BeautifulSoup(html.text, 'html.parser')


def get_child_by_class(html, tag, classname):
    return html.find(tag,{'class': classname})

def get_child_by_id(html, tag, classname):
    return html.find(tag,{'class': classname})


if __name__ == "__main__":
    main()
