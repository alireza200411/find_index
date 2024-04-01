def address(word:str) -> int :
    """This function shows the address of the characters of a string in the output. To exit the execution of the function, just press the enter button when asking a question."""
    while True :
        adr = input('enter address or empty for canael. ')
        if adr == '' : 
            break
        else:
            if adr not in word :
                print(f'{adr} does not exist in the {word}.')

                continue
            else :
                if word.count(adr) > 1 :
                    answer1 = word.index(adr)
                    answer2= word.index(adr,answer1+1)
                    return(f'Current character {adr} position at {answer1} , {answer2}')
                else:
                    answer = word.index(adr)
                    return(f'Current character {adr} position at {answer}')