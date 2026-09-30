# openlibrary-books
Get 50 books from OpenLibrary API and filter them
# OpenLibrary Books Task

اسکریپت پایتونی که ۵۰ کتاب از API عمومی OpenLibrary دریافت میکنه،
کتابهای منتشرشده بعد از سال ۲۰۰۰ رو فیلتر میکنه و در فایل CSV ذخیره میکنه.

## پیشنیازها

- Python 3.11+
- کتابخانه requests

## نصب

pip install requests

## اجرا

python get-books.py

## خروجی

فایل books.csv با سه ستون ساخته میشه:
- عنوان
- نویسنده
- سال

## ساختار پروژه

- get-books.py — اسکریپت اصلی
- books.csv — خروجی
- README.md — همین فایل
