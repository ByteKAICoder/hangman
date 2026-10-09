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
