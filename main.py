import flet as ft 
from db import main_db

def main(page: ft.Page):
    page.title = 'Spisok Pokupok'
    page.theme_mode = ft.ThemeMode.LIGHT

    spisok_list = ft.Column(spacing=10)

    def load_spisok():
        spisok_list.controls.clear()
        for spisok_id, spisok_text in main_db.get_spisok():
            spisok_list.controls.append(create_spisok_row(spisok_id=spisok_id, spisok_text=spisok_text))
        page.update()


    def create_spisok_row(spisok_id, spisok_text, completed=False):
        spisok_field = ft.TextField(value=spisok_text, read_only=True, expand=True)

        checkbox = ft.Checkbox(value=bool(completed), on_change=None)


        def save_spisok(_):
            main_db.update_spisok(spisok_id=spisok_id, new_spisok=spisok_field.value)
            spisok_field.read_only = True
            spisok_field.update()
            page.update()

        save_button = ft.IconButton(icon=ft.Icons.SAVE_ALT_ROUNDED, on_click=save_spisok)

        def delete_spisok(_):
            main_db.delete_spisok(spisok_id)
            load_spisok()
        
        delete_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=delete_spisok, icon_color=ft.Colors.RED)

        return ft.Row([checkbox, spisok_field, save_button, delete_button])

    def add_spisok(_):
        if spisok_input.value:
            spisok = spisok_input.value
            spisok_id = main_db.add_spisok(spisok)
            spisok_list.controls.append(create_spisok_row(spisok_id=spisok_id, spisok_text=spisok))

            spisok_input.value = ''
            page.update()

    spisok_input = ft.TextField(label='vvedite nazvaniye tovara', expand=True)
    add_button = ft.IconButton(icon=ft.Icons.ADD, tooltip='Добавить задачу', on_click=add_spisok)

    page.add(ft.Row([spisok_input, add_button]), spisok_list)
    load_spisok()


if __name__ == '__main__':
    main_db.init_db()
    ft.app(target=main)