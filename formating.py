while True:
    beforeStripping = input(': ')
    formated = beforeStripping.replace('. ', '-')
    formated = formated.replace(' ', '_')
    formated += '.py'

    f = open(formated, 'a')
    f.close()
