from cgitb import text
from multiprocessing import context
from pickle import NONE
from django.shortcuts import render,get_object_or_404, redirect
from django.http import Http404
from requests import post
from .models import Product

from .forms import PostForm, ProductForm
from .forms import LoginForm
from .forms import RegistrationForm
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
from  .models import Post
# Create your views here.



#pdf imports
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# importing the necessary libraries
from django.http import HttpResponse
from django.views.generic import View
from .process import html_to_pdf 
from django.template.loader import render_to_string

#Creating a class based view
class GeneratePdf(View):
     def get(self, request, my_id):
       
        data = Post.objects.filter(id=my_id).first()
        print(data)
        open('templates/temp.html', "w").write(render_to_string('products/pdf.html', {'data': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         # rendering the template
       # return FileResponse(pdf,as_attachment=True, filename='venue.pdf')
        return HttpResponse(pdf, content_type='application/pdf')


def home_view(request):
    print(request.user)
    return render(request,"products/home.html",{})

@login_required(login_url="/login")
def preview_post(request, my_id):
     posts = Post.objects.get(id= my_id)
     print(posts)
     if request.method == "DELETE":
          post_id = request.POST.get("post-id")
     return render(request,"products/preview_post.html",{"posts":posts})

@login_required(login_url="/login")
def all_post(request):
     posts = Post.objects.all()
     
     if request.method == "POST":
          post_id = request.POST.get("post-id")
          edit_id = request.POST.get("edit-id")
          if post_id:
               post = Post.objects.filter(id=post_id).first()
               if post and post.author == request.user:
                    post.delete()
          elif edit_id:
               return redirect(f'/edit-post/{edit_id}')
               
     return render(request,"products/all_post.html",{"posts":posts})


def edit_post(request,my_id):
     obj = get_object_or_404(Post,id=my_id)

     form = PostForm(request.POST or None, instance=obj)
     if form.is_valid():
          form.save()
          return redirect("/all-post")
     return render(request, "products/edit_post.html",{'form': form})


def sign_up(request):
     if request.method == 'POST':
          form = RegistrationForm(request.POST)
          if form.is_valid():
               user = form.save()
               login(request,user)
               return redirect('/home')
     else:
          form = RegistrationForm()
     return render(request,'registration/sign_up.html',{'form':form})

@login_required(login_url="/login")
def create_post(request):
     if request.method == "POST":
          form = PostForm(request.POST)
          if form.is_valid():
               post = form.save(commit=False)
               post.author = request.user
               print(post)
               post.save()
               return redirect("/all-post")
     else:
          form = PostForm()

     return render(request, 'products/create_post.html',{"form":form})


#Generate a PDF File Venue list
# def post_pdf(request,my_id):
#      buf = io.BytesIO()
#      c = canvas.Canvas(buf, pagesize=letter, bottomup= 0)

#      textobj = c.beginText()
#      textobj.setTextOrigin(inch , inch)
#      textobj.setFont("Helvetica", 14)
#      lines = Post.objects.all().values()
     

#      # for line in lines:
#      #      textobj.textLine(line)
#      textobj.textLine(lines)
#      c.drawText(textobj)
#      c.showPage()
#      c.save()
#      buf.seek(0)

#      return FileResponse(buf,as_attachment=True, filename='venue.pdf')





# def doc_view(request,*args, **kwargs):
#      my_context = {
#           'my_text':'Welcome to the documentation',
#           'my_number':123,
#           'my_list':[123,23,443,22]
#      }
#      return render(request,"documentation.html",my_context)

# def login_view(request):
#     my_form = LoginForm()
#     if request.method == 'POST':
#        my_form = LoginForm(request.POST)
#        if my_form.is_valid():
#           #now the data is good
#           queryset = Product.objects.all().values()
#           for e in queryset:
#                print(e)
#                if my_form.cleaned_data['email_address'] == e['email_address']:
#                     print(e['email_address'])
#                     token = e['id']
#                     print(token)
#                     return redirect(f'../preview/{token}')
               
          

#     context = {
#           'form' : my_form
#      }
#     return render(request,'login.html',context)


# def faq_view(request,*args, **kwargs):
#      return render(request,"faq.html",{})


# def dashboard(request,*args, **kwargs):
#       return render(request,"dashboard.html",{})

# def contact(request,*args, **kwargs):
#       return render(request,"contact.html",{})


# def product_detail_view(request):
#      obj = Product.objects.get(id=1)
#      # context = {
#      #      'header':obj.header,
#      #      'website_name':obj.website_name
#      # }
#      context = {
#           'object': obj
#      }
#      return render(request,"services/detail.html",context)


# def product_form_view(request):
#      my_form = RegistrationForm()
#      if request.method == 'POST':
#        my_form = RegistrationForm(request.POST)
#        if my_form.is_valid():
#           #now the data is good
#           print(my_form.cleaned_data)
#           # Product.objects.create(**my_form.cleaned_data)
#        else:
#           print(my_form.errors)
#      context = {
#           'form' : my_form
#      }
#      return render(request,'registration/sign_up.html',context)


# def product_edit_from_view(request,my_id):
#      obj = get_object_or_404(Product,id=my_id)

#      form = ProductForm(request.POST or None, instance=obj)
#      if form.is_valid():
#           form.save()
#      context = {
#           'form':form
#      }
#      return render(request, "products/edit.html",context)

# def product_preview(request,my_id):
#      querySet = get_object_or_404(Product,id=my_id)
#      print(querySet)
#      context= {
#           "object_preview": querySet
#      }
#      return render(request, "services/preview_page.html",context)
