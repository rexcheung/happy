def userInput(list, onInput):
    if list is None or len(list) == 0:
        print('list不能为空')
        return

    length = len(list)
    while(True):
        print('\n\n')
        for i in range(0, length):
            print(list[i])

        print('99. exit\n')
        text = input("Input code: ")

        if len(text) <= 0:
            print('invalid code')

        if text == '99':
            return 0

        onInput(text)
