def hangman(picture_number:int,
           word:str,
           string:str,
           false_letters:list
           )-> None:
   match picture_number:
       case 0:
           print(f"""
                    {string}
                    {'-' * len(word)}"""
                 )
       case 1:
           print(rf"""
                    |
                    |   
                    |   
                    |
                    |
                    |
                    {string}
                    {'-' * len(word)}
                    {''.join(false_letters)}"""
                 )
       case 2:
           print(rf"""
                    |   
                    |   
                    |
                    |
                    |
                   _|___
                    {string}
                    {'-' * len(word)}
                    {''.join(false_letters)}"""
                 )
       case 3:
           print(rf"""
                    ________
                    |/  
                    |   
                    |
                    |
                    |
                   _|___
                    {string}
                    {'-' * len(word)}
                    {''.join(false_letters)}"""
                 )
       case 4:
           print(rf"""
                    ________
                    |/     |
                    |  
                    |
                    |
                    |
                   _|___
                    {string}
                    {'-' * len(word)}
                    {''.join(false_letters)}"""
                 )
       case 5:
           print(rf"""
                    ________
                    |/     |
                    |     ⚪
                    |
                    |
                    |
                   _|___
                    {string}
                    {'-' * len(word)}
                    {''.join(false_letters)}"""
                 )
       case 6:
           print(rf"""
                    ________
                    |/     |
                    |     ⚪
                    |      |
                    |
                    |
                   _|___
                    {string}
                    {'-' * len(word)}
                    {''.join(false_letters)}"""
                 )
       case 7:
           print(rf"""
                    ________
                    |/     |
                    |     ⚪
                    |      |\
                    |
                    |
                   _|___
                    {string}
                    {'-' * len(word)}
                    {''.join(false_letters)}"""
                 )
       case 8:
           print(rf"""
                    ________
                    |/     |
                    |     ⚪
                    |     /|\
                    |       
                    |
                   _|___
                    {string}
                    {'-' * len(word)}
                    {''.join(false_letters)}"""
                 )
       case 9:
           print(rf"""
                    ________
                    |/     |
                    |     ⚪
                    |     /|\
                    |       \
                    |
                   _|___
                    {string}
                    {'-' * len(word)}
                    {''.join(false_letters)}"""
                 )
       case 10:
           print(rf"""
                    ________
                    |/     |
                    |     ⚪
                    |     /|\
                    |     / \
                    |
                   _|___
                    {string}
                    {'-' * len(word)}
                    {''.join(false_letters)}
                    Вы проиграли.\nЗагаданное слово: {word}"""
                 )
