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


def install_words(language:str='Rus')-> list:
   match language:
       case 'Eng':
           file_path = 'english_words.txt'
       case 'Rus':
           file_path = 'russian_words.txt'

   try:
       with open(file_path, 'r', encoding='utf-8') as file:
           words = file.read().splitlines()

   except FileNotFoundError:
       print('Ошибка! Файл не найден.\n'
             'Использую список слов по умолчанию.'
             )
       words = (['корабль',
                'виноград',
                'космонавт',
                'кенгуру',
                'спортзал'] if language == 'Rus' else ['monkey',
                                                       'tennis',
                                                       'strawberry',
                                                       'keyboard',
                                                       'library']
                )
     
   except UnicodeDecodeError:
       print('Ошибка! Не удалось прочитать файл.\n'
             'Использую список слов по умолчанию.'
             )
       words = ['корабль',
                'виноград',
                'космонавт',
                'кенгуру',
                'спортзал'] if language == 'Rus' else ['monkey',
                                                       'tennis',
                                                       'strawberry',
                                                       'keyboard',
                                                       'library']
           
   return words
