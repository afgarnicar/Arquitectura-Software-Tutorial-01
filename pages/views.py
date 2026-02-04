from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from matplotlib.style import context
from django.views import View
from django import forms
from django.http import HttpResponseRedirect


# Create your views here.
class homePageView(TemplateView):
    template_name = 'pages/home.html'
    
class AboutPageView(TemplateView): 
    template_name = 'pages/about.html' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page ...",
            "author": "Developed by: Andrés Garnica",
            })
        return context
    
class ContactPageView(TemplateView):
    template_name = 'pages/contact.html' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Contact us - Online Store",
            "subtitle": "Contact us",
            "description": "This is a contact page ...",
            "author": "Developed by: Andrés Garnica",
            "email": "info@onlinestore.com",
            "phone": "+57 (4) 123-4567",
            "address": "Carrera 49 #7-50, Medellín, Antioquia, Colombia",
            })
        return context

class Product: 
    products = [
        {"id":"1", "name":"TV", "description":"Best TV", "price": 1000}, 
        {"id":"2", "name":"iPhone", "description":"Best iPhone", "price": 1200}, 
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast", "price": 100}, 
        {"id":"4", "name":"Glasses", "description":"Best Glasses", "price": 50} ]
    
class ProductIndexView(View):
    template_name = 'pages/products/index.html'
    
    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.products
        viewData["product_price"] = Product.products
        
        return render(request, self.template_name, viewData)
    
class ProductShowView(View): 
    template_name = 'pages/products/show.html'


    def get(self, request, id):
        try:
            product_id = int(id) - 1
            if product_id < 0 or product_id >= len(Product.products):
                return HttpResponseRedirect('/')
            
            viewData = {}
            product = Product.products[product_id]
            viewData["title"] = product["name"] + " - Online Store"
            viewData["subtitle"] = product["name"] + " - Product information"
            viewData["product"] = product
            viewData["product_price"] = product["price"]
            return render(request, self.template_name, viewData)
        except:
            return HttpResponseRedirect('/')

class ProductForm(forms.Form): 
    name = forms.CharField(required=True) 
    price = forms.FloatField(required=True)
    
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise forms.ValidationError("Price must be greater than zero")
        return price
    
class ProductCreateView(View):
    template_name = 'pages/products/create.html'
    
    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] = form
        return render(request, self.template_name, viewData)
    
    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            viewData = {}
            viewData["title"] = "Success - Online Store"
            viewData["subtitle"] = "Product Created"
            viewData["message"] = "Product created"
            return render(request, 'pages/products/success.html', viewData)
        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
            return render(request, self.template_name, viewData)
        