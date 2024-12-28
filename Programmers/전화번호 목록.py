def solution(phone_book):
    phone_book.sort() # sort() method sorts the list in ascending order
    for i in range(len(phone_book) - 1): # compare the elements of the list
        if phone_book[i] in phone_book[i + 1]: # if the element is included in the next element
            return False # the answer is False
    return True