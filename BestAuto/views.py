from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.forms import modelformset_factory
from .models import Products, Contact, ProductsImage
from .models import ProductsImage

from .forms import ProductsImageForm, ProductsForm
from extra_views import CreateWithInlinesView, InlineFormSetFactory
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Products
    fields = ['pname', 'pcategory', 'pprice', 'pdescription', 'pimage', 'pdate_posted', 'poffer']


    def form_valid(self, form):
        return super().form_valid(form)



class ProductUpdateView(LoginRequiredMixin,  UpdateView):
    model = Products
    fields = ['pname', 'pcategory', 'pprice', 'pdescription', 'pimage', 'pdate_posted', 'poffer']

    def form_valid(self, form):
        return super().form_valid(form)

#$$$$$$$$$$$$$$$$$$$$$$$

# class ProductImagesDeleteView(LoginRequiredMixin, DeleteView):
#     model = ProductsImage
#     success_url = '/'
#     #template_name = 'BestAuto/products_form.html'
#     slug_field = 'pk'
#
#     def get_context_data(self, **kwargs):
#         context = super(ProductImagesDeleteView, self).get_context_data(**kwargs)
#         pioriginal = self.kwargs.get('pioriginal')
#         context['pk'] = Products.objects.filter(pname=pioriginal).get('pk')
#         return context


class ProductImagesCreateView(LoginRequiredMixin, CreateView):
    model = ProductsImage
    fields = ['pioriginal', 'piimages']
    template_name = 'BestAuto/products_form.html'

    def form_valid(self, form):
        return super().form_valid(form)


#$$$$$$$$$$$$$$$$$$$$$$$

#
#
class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Products
    success_url = '/'
#




#================================

class IndividualProductsListView(DetailView):
    model = Products ###
    template_name = 'BestAuto/products_individual.html'  # <app>/<model>_<viewtype>.html
    slug_field = 'pk'

    def get_context_data(self, **kwargs):
        context = super(IndividualProductsListView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['images'] = ProductsImage.objects.filter(pioriginal=pk)
        context['id_used'] = pk
        # other code
        return context




# def index(request):
#     return render(request, 'BestAuto/index.html')


class IndexListView(ListView):
    model = Products
    template_name = 'BestAuto/index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'products'
    ordering = ['-pdate_posted']

    def get_context_data(self, **kwargs):
        context = super(IndexListView, self).get_context_data(**kwargs)
        context.update({
            'products': Products.objects.filter(poffer=True),
        })
        return context







def about(request):
    return render(request, 'BestAuto/about.html')


def contact(request):
  if (request.method == 'POST'):
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')

    contact = Contact(name=name, email=email, subject=subject, message=message)
    contact.save()
    messages.success(request, f'Thank you very much! We will contact you as soon as possible!')
    return redirect('products-view')
  return render(request, 'BestAuto/contact.html')






class ProductListView(ListView):
    model = Products
    template_name = 'BestAuto/products.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'products'
    ordering = ['-pdate_posted']
    paginate_by = 3




class SearchView(ListView):
    model = Products
    template_name = 'BestAuto/products_search.html'
    context_object_name = 'products'
    ordering = ['-pdate_posted']

    def get_queryset(self):
        products = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        print(query)
        if query:
            products = Products.objects.filter(pname__startswith=query)

        else:
            products = Products.objects.all()
        return products



