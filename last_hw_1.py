"""
Получает текст от пользователя и
создаёт word-файл с этим текстом
"""
from docx import Document

def create_word(text: any ) -> None:
    """
    Создаёт word-файл
    """
    doc = Document()
    doc.add_paragraph(text)
    doc.save("output.docx")
    print("Word-файл успешно создан.")

if __name__ == "__main__":
    """
    Получает текст от пользователя
    """
    user_input = input("Введите текст для создания Word-файла: ")
    create_word(user_input)
