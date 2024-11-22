
import bookLibrary



class Menu:

    def __init__(self) -> None:
        self.library = bookLibrary.Library()
        self.options = {
            '1' : 'show all',
            '2' : 'filter',
            '3' : 'add', 
            '4' :'delete',
            '5' : 'change status'
        }


    def run_menu(self):

        try: 
            while True:
                for key, option in self.options.items():
                    print(f'{key}) {option}')

                choise = input(': ').strip()

                if choise == '1':
                    self.library.show_all()                

                elif choise == '2':
                    print(f"1) title")
                    print(f"2) author")
                    print(f"3) year")
                    field_c = input("field : ").strip()
                    
                    if field_c == '1':
                        field_value = input('title: ').strip().lower()
                        self.library.show_by_field(field='title', value=field_value)
                    elif field_c == '2':
                        field_value = input('author: ').strip().lower()
                        self.library.show_by_field(field='author', value=field_value)
                    elif field_c == '3':
                        field_value = input('year: ').strip().lower()
                        self.library.show_by_field(field='year', value=field_value)

                elif choise == '3':
                    title = input("title : ").strip()
                    author = input("author : ").strip()
                    year = input("year : ").strip()
                    self.library.add(title, author, year)

                elif choise == '4':
                    id_del = input('id : ').strip()
                    self.library.delete_by_id(id_del)
                
                elif choise == '5':
                    id_stat = input("id : ").strip()
                    print("1) в наличии\n2) выдана")
                    choise_stat = input("choise new status: ").strip()
                    if choise_stat == '1':
                        new_status = 'в наличии' 
                    elif choise_stat == '2':
                        new_status = 'выдана'
                    else:
                        continue

                    self.library.change_status(book_id=id_stat, new_status=new_status)

                print('\n\n')

        except KeyboardInterrupt:
            pass
                


m = Menu()
m.run_menu()
            