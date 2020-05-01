def reverseWords(input):
    inputWords = input.split(" ")

    inputWords = inputWords[-1::-1]
    # first -1 : inputWords's last element
    # second null : foreach until last
    # third -1: step , -1 means reverse

    # reverse for List..
    output = ' '.join(inputWords)
    return output


if __name__ == "__main__":
    input = " I love you "
    rw = reverseWords(input)
    print(rw)
