from utils import install_words, hangman


def user_input(text:str='',
              some_type:str='str',
              values:tuple=()
              )-> str|int:
   if some_type == 'str':
       while True:
           some_param = input(text)
           if not some_param:
               print('Пустой ввод! Попробуйте снова.')
               continue
           if values and some_param not in values:
               print('Неверный ввод! Попробуйте снова.')
               continue
           break

   return some_param


def main():
   print('============= ВИСИЛИЦА =============')

   language = user_input('Какие слова хотите отгадывать? ("Rus"/"Eng"): ',
                         values=('Rus', 'Eng')
                         )
   words = install_words(language)
   word = random.choice(words)
   user_string = ' ' * len(word) 
   picture_number = 0
   false_letters = []

   print('Слово загадано! Попробуй его отгадать!')
   
   while user_string != word:
       hangman(picture_number, word, user_string, false_letters)
       letter = user_input('Введите букву: ',
                           values=
                           tuple(string.ascii_letters) if language == 'Eng'
                           else
                           tuple(chr(index) for index in range(ord('А'), ord('я') + 1))
                           ).lower()

       if letter in word:
           if letter in user_string:
               print('Вы уже вводили эту букву. Повторите ввод.')
               continue
           for index in range(len(word)):
               if word[index] == letter:
                   user_string = user_string[:index] + letter + user_string[index + 1:]
           print('Верно! Такая буква есть.')

       else:
           if letter in false_letters:
               print('Вы уже вводили эту букву. Повторите ввод.')
               continue
           picture_number += 1
           false_letters.append(letter)
           print('Упс! Такой буквы нет.')

           if picture_number == 10:
               hangman(picture_number, word, user_string, false_letters)
               break

   else:
       hangman(picture_number, word, user_string, false_letters)
       print('Поздравляем! Вы угадали!')
