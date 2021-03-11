from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Product, Category, Size
from cart.forms import CartAddProductForm
from django.db.models import Q
from lookbook.models import Collection
from django.core.paginator import Paginator


class HomePageView(ListView):
    model = Product
    template_name = 'home.html'
    def get_ordering(self):
        ordering = self.request.GET.get('orderby')
        print(ordering)
        return ordering
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['sizes'] = Size.objects.all()
        context['categories'] = Category.objects.all()
        return context

        # self.size = get_object_or_404(Size, size=self.request.GET.get('filtrby'))
        # return Product.objects.filter(sizes=self.size)


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    collection = Collection.objects.all()
    # filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        paginator = Paginator(products, 10)
        page_number = request.GET.get('page')  
        page = paginator.get_page(page_number)
    return render(request,
                  'product/list.html',
                  {'category': category,
                   'categories': categories,
                   'page': page, 
                   'paginator': paginator})


def product_detail(request, product_id):
    product = get_object_or_404(Product,
                                id=product_id,)
    cart_product_form = CartAddProductForm()
    sizes_for_product = Size.objects.filter(clothe=product_id)
    return render(request,
                  'product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form,
                   'sizes_for_product': sizes_for_product,
                   })


class SearchResultView(ListView):
    model = Product
    template_name = 'search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('search')
        return Product.objects.filter(Q(product_name__icontains=query))

class CategoriesView(ListView):
    model = Category
    template_name = 'category.html'