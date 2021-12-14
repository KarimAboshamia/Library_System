from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from datetime import datetime,date
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseBadRequest
from .models import Profile
import json
from .models import Book,Borrowed
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from .forms import *
from django.shortcuts import redirect


from django import template
  
register = template.Library()
  
@register.filter()
def low(value):
    return value.lower()

@login_required(login_url='welcome')
def home(request):
    if request.is_ajax():
        type = request.GET['type']
        author = request.GET['author']
        ISBN = request.GET['ISBN']
        pub = request.GET['publication_year']
        bookObj = Book.objects.all()
        if type != "":
            bookObj= bookObj.filter(type= type)
            print(bookObj[2].ISBN)
            print(bookObj[3].ISBN)
        if author != "":
            bookObj= bookObj.filter(author_name= author)
            print("author")
        if ISBN != "":
            bookObj= bookObj.filter(ISBN=ISBN)
            print("ISBN")
        if pub != "":
            bookObj= bookObj.filter(publication_year=pub)
            print("Pub")
        return JsonResponse({'books':list(bookObj.values())}, status=200)
    borrowings  = Borrowed.objects.all()
    for i in borrowings:
        if  i.DateReturn <= date.today():
            i.bookId.counter +=1
            i.bookId.save()
            i.delete()
    books = Book.objects.filter(counter__gt=0)
    return render(request, 'home.html', {'books':books})
    
@login_required(login_url='welcome')
def admin_Interface(request):
    if request.user.is_superuser:
        borrowings  = Borrowed.objects.all()
        for i in borrowings:
            if  i.DateReturn <= date.today():
                i.bookId.counter +=1
                i.bookId.save()
                i.delete()
        books = Book.objects.filter(counter__gt=0)
        book_Author = Book.objects.all().values('author_name').distinct()
        book_Type = Book.objects.all().values('type').distinct()
        book_Date = Book.objects.all().values('publication_year').distinct()
        return render(request, 'admin_Interface.html', {'books': books,'book_Author': book_Author, 'book_Type':book_Type, 'book_Date':book_Date})
    else:
        return redirect('user_Interface')
    

@login_required(login_url='welcome')
def user_Interface(request):
    borrowings  = Borrowed.objects.all()
    for i in borrowings:
        if  i.DateReturn <= date.today():
            i.bookId.counter +=1
            i.bookId.save()
            i.delete()
    books = Book.objects.filter(counter__gt=0)
    book_Author = Book.objects.all().values('author_name').distinct()
    book_Type = Book.objects.all().values('type').distinct()
    book_Date = Book.objects.all().values('publication_year').distinct()
    return render(request, 'user_Interface.html', {'books': books,'book_Author': book_Author, 'book_Type':book_Type, 'book_Date':book_Date})
    #Borrowed books

def welcome(request):
    if request.method == "POST":
        flagName = request.POST.get('name')
        if flagName:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            ID = request.POST.get('ID')
            college = request.POST.get('college')
            password = request.POST.get('password')
            data = Profile(name=name,email=email,password=make_password(password),college=college,ID=ID,phone=phone)
            data.save()
            return render(request, 'welcome.html')
        else:
            email = request.POST.get('email')
            password = request.POST.get('password')
            user  =  authenticate(request,username=email,password=password)
            
            if user is not None:
                login(request,user)
                if user.is_superuser:
                    return redirect("admin_Interface")
                else:
                    return redirect("user_Interface")
            print("user is nulll")
            return render(request,'welcome.html',{'val':"wrong email or password"})
            # for i in range(len(User_List)):
            #     if profile_List[i].email == email and profile_List[i].password == password:
            #         print('Hello,World')
            #         return render(request, 'welcome.html') 
            
    return render(request, 'welcome.html')

def logoutUser(request):
	logout(request)
	return redirect('welcome')

def profile(request):
    return render(request, 'profile.html', {'user':model_to_dict(request.user)})

def addbook(request):
    if request.user.is_superuser:
        flag=0
        bookObj=  Book.objects.all()
        if request.method == 'POST':
            form= BookForm(request.POST, request.FILES)
            if form.is_valid():
                for book in bookObj:
                    if book.ISBN==form.cleaned_data.get("ISBN"):
                        book.counter+=1
                        book.save()
                        flag=1
                        break
                if flag==0:
                    form.save()
                    return redirect('addbook')            
        else:
            form= BookForm()
        return render(request, 'addbook.html', {'form': form})
    else:
        return redirect('user_Interface')

def profile_update(request):
    if request.method == 'POST':
        form= UpdateProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form=UpdateProfileForm(instance=request.user)

    return render(request, 'profile_update.html', {'form': form})



def book_update(request, pk):
    if request.user.is_superuser:
        bookId = Book.objects.get(id=pk)
        if request.method == 'POST':
            form= BookForm(request.POST, request.FILES, instance= bookId)
            if form.is_valid():
                form.save()
                return redirect('admin_Interface')
        else:
            form=BookForm(instance= bookId)

        return render(request, 'book_update.html', {'form': form})
    else:
        return redirect('user_Interface')

@login_required(login_url='welcome')
def borrowBook(request):
    if request.method == 'POST':
        # print(request.body)
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        neededBook = Book.objects.filter(pk=body["bookId"])[0]
        obj = Borrowed.objects.filter(userEmail=request.user,bookId = neededBook)
        # print(obj)
        print(len(obj), neededBook.counter , obj )
        if len(obj) == 0:
            if neededBook.counter > 0:
                neededBook.counter -=1 
                neededBook.save()
                borrowing = Borrowed.objects.create(userEmail=request.user,bookId =neededBook)
                borrowing.save()
                return JsonResponse({'message':"borrowed successfully"})

        else :
            return JsonResponse({"message":"already borrowed that book"})


@login_required(login_url='welcome')
def user_books(request):
    if request.user.is_superuser:
        return redirect('admin_Interface')
    else:
        borrowings  = Borrowed.objects.all()
        for i in borrowings:
            if  i.DateReturn <= date.today():
                i.bookId.counter +=1
                i.bookId.save()
                i.delete()
                
        userBooks = Borrowed.objects.filter(userEmail=request.user)
        
        noBooks = len(userBooks) == 0
        return render(request,'user_books.html',{'userBooks': userBooks, 'noBooks':noBooks})

@login_required(login_url='welcome')
def returnBook(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    neededBook = Book.objects.filter(pk=body["bookId"])[0]
    obj = Borrowed.objects.filter(userEmail=request.user,bookId = neededBook)[0]
    obj.bookId.counter +=1
    obj.bookId.save()
    obj.delete()
    return JsonResponse({'message':'returned the book successfully'})


@login_required(login_url='welcome')
def extendBook(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    neededBook = Book.objects.filter(pk=body["bookId"])[0]
    obj = Borrowed.objects.filter(userEmail=request.user,bookId = neededBook)[0]
    # if ()
    if obj.extended == False:
        obj.extended =  True
        obj.DateReturn = obj.DateReturn  + timedelta(days=7) 
        obj.save()
        return JsonResponse({'message':'extended the return date successfully','newDate': obj.DateReturn.strftime("%b, %d %Y")})
    else:
        return JsonResponse({'message':'you have already extended the return date'})

