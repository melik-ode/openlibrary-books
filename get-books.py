import csv
import requests


# این تابع کتابها رو از سایت OpenLibrary میگیره
def get_books(search_word, count=50):
    url = "https://openlibrary.org/search.json"
    params = {"q": search_word, "limit": count}
    
    response = requests.get(url, params=params)
    data = response.json()
    
    books = data["docs"]
    return books


# این تابع کتابهای قدیمی رو حذف میکنه
def remove_old_books(books):
    new_books = []
    
    for book in books:
        year = book.get("first_publish_year")
        
        if year is None:
            continue
        
        if year > 2000:
            new_books.append(book)
    
    return new_books


# این تابع کتابها رو توی فایل CSV ذخیره میکنه
def save_books(books):
    file = open("books.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(file)
    
    writer.writerow(["عنوان", "نویسنده", "سال"])
    
    for book in books:
        title = book.get("title", "نامشخص")
        
        authors = book.get("author_name", ["نامشخص"])
        author = ", ".join(authors)
        
        year = book.get("first_publish_year")
        
        writer.writerow([title, author, year])
    
    file.close()


# اینجا برنامه اصلی رو اجرا میکنیم
print("در حال دریافت کتابها...")
books = get_books("python programming", 50)
print(str(len(books)) + " کتاب دریافت شد")

new_books = remove_old_books(books)
print(str(len(new_books)) + " کتاب جدید پیدا شد")

save_books(new_books)
print("فایل books.csv ذخیره شد")