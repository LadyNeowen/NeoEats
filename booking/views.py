from django.shortcuts import render

def book_table(request):
    return render(request, "booking/book_table.html")