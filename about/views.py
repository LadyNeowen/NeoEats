from django.shortcuts import render

def about(request):
    return render(request, "about/about.html")

def how_it_all_started(request):
    return render(request, "about/how_it_all_started.html")

def gallery(request):
    return render(request, "about/gallery.html")

def collaborations_with_farmers(request):
    return render(request, "about/collaborations_with_farmers.html")