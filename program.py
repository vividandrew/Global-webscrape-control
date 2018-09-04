from bs4 import BeautifulSoup
import requests


def main():
    url = input("Type url here")
    html = get_html(requests.get(url))


    # TODO: Create function to get list of url from excel sheet
    # TODO: Create function to save result to docx

    # TODO: Create function to interact with Joomla site
    # TODO: Create function to interact with WordPress site
    # TODO: Create function to find out if its a Joomla, or wordpress site
    # TODO: Interact with local DB to find username and password

    # TODO: ULTIMATE GOAL have a function that can quickly transfer content from any website to a joomla site.


def get_html(html) -> BeautifulSoup:
    return BeautifulSoup(html.text, 'html.parser')


def get_child_by_class(html, classname):
    return html.find('div',{'class': classname})


def get_child_by_id(html, id):
    return html.find('div', {'id': id})


if __name__ == "__main__":
    main()
