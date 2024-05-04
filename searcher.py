from time import sleep

from mongoengine import DoesNotExist

from connect import create_connection
from models import Author, Quote


def search_by_name() -> list | str:
    """Searching quotes by author name"""
    global name
    try:
        name = input('Author`s name: ')
        author = Author.objects.get(fullname=name)
        quotes = Quote.objects(author=author)
        result = []
        for quote in quotes:
            result.append(quote['quote'])

        return result
    except DoesNotExist:
        return f'There is no matches for {name}'


def search_by_tag() -> list:
    """Searching quotes by the tag"""
    tag = input('Searching tag: ')
    quotes = Quote.objects(tags=tag)
    result = []
    for quote in quotes:
        result.append(quote['quote'])

    return result


def search_by_tags() -> list:
    """Searching quotes by tags"""
    tags = input('Searching tags: ')
    tag_1, tag_2 = tags.split(',')[0], tags.split(',')[0]
    quotes_1 = Quote.objects(tags=tag_1)
    quotes_2 = Quote.objects(tags=tag_2)
    quotes_set = set()
    for quote in quotes_1:
        quotes_set.add(quote['quote'])
    for quote in quotes_2:
        quotes_set.add(quote['quote'])

    return list(quotes_set)


def main():
    """Main function"""
    create_connection()
    waiting = True
    while waiting:
        print('Choose the searching option:\n'
              '[1] - Search by name\n'
              '[2] - Search by tags\n'
              '[3] - Search by tag\n'
              '[4] - Exit')
        searching_option = input('>>> ')
        if searching_option == '1':
            print(search_by_name())
        elif searching_option == '2':
            print(search_by_tags())
        elif searching_option == '3':
            print(search_by_tag())
        elif searching_option == '4'\
                or searching_option == 'exit':
            print('Good bye')
            sleep(1)
            waiting = False
        else:
            print('Unknown command, try again')


if __name__ == "__main__":
    main()