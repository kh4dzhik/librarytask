import json
import os

class Library:

    def __init__(self) -> None:
        self.lastid_file_name = 'lastid.txt'
        self.books_file_name = 'books.json'
        self.json_data = {}


        # выгрузим данные из json в словарь json_data и будем с ней работать в дальнейшем
        # если хотим внести какие то изменения в json файл, мы сначала меняем словарь json_data
        # потом ее синхранизируем с json файлом 
        # чтоб не лоадить ее при каждой операции
        # и для вывода у нас уже есть json_data с актуальними данными
        try:
            with open(self.books_file_name, 'r') as f:
                self.json_data = json.load(f)
        except:
            pass
        

   
    def gen_unique_id(self) -> int:
        last_id = 0

        with open(self.lastid_file_name, 'r') as f:
            lines = f.readlines()
            # находим id среди переводов строки и инкрементим
            for i in lines:
                if i != '\n':
                    last_id = int(i)+1
                    break

        # обновляем id в lastid файле
        with open(self.lastid_file_name, 'w') as f:
            f.write(str(last_id))

        return last_id


    # добавление книги
    def add(self, title : str, author: str, year: str) -> None:
        new_data = {
            'title' : title,
            'author' : author,
            'year' : year,
            'status' : 'в наличии',
        }

        json_data = {}

        new_id = self.gen_unique_id()
        self.json_data[new_id] = new_data

        with open(self.books_file_name, 'w') as f:
            json.dump(self.json_data, f, indent=4)
    
            
    # удаление книги по id
    def delete_by_id(self, book_id: str) -> None:
       
        try:
            self.json_data.pop(str(book_id))
        except KeyError:
            print('книги с таким id нет')
            return None

        with open(self.books_file_name, 'w') as f:
            json.dump(self.json_data, f, indent=4)


    def change_status(self, book_id: str, new_status: 'str') -> None:    
        try:
            self.json_data[str(book_id)]['status'] = new_status
        except KeyError:
            print('книги с таким id нет')
            return None

        with open(self.books_file_name, 'w') as f:
            json.dump(self.json_data, f, indent=4)




    def show_all(self) -> None:

        for key, item in self.json_data.items():
            print(key)
            for k, i in item.items():
                print(f'{k} : {i}') 
            print("\n\n\n")


    def show_by_field(self, field: str, value: str) -> None:
 

        if field == 'id':
            try:
                print(self.json_data[value])
            except KeyError:
                print('книги с таким id нет')
        
        else:
            try:
                for key, item in self.json_data.items():
                    if str(item[field]).lower() == value.lower():
                        print('\n\n\n') 
                        print(f'id : {key}')
                        for k in item:
                            print(f'{k} : {item[k]}')
            except KeyError:
                print('неправильно указали название поля')
            
            



# o = Library()
# # o.add('12', '2121', '1232')
# # o.delete_by_id('228')
# # o.change_status('224', "asdasadasdasdasd")
# # o.show_all()
# o.show_by_field('title', '13')
# # o.close()