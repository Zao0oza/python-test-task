def black_box(page: int):
    if page <= 7922400:
        return True
    else:
        return False


def main():
    pages = [x for x in range(1, 10000001)]
    while len(pages)// 2 != 0:
        mid = len(pages)// 2
        if black_box(pages[mid]):
            pages = pages[mid:]
        else:
            pages = pages[0:mid]
    return pages


if __name__ == '__main__':
    main()

print(main())