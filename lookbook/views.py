# from django.shortcuts import render
# from django.views.generic import ListView
# from .models import Collection, Slide_of_collection


# # class LookbookView(ListView):
# #     model=Collection
# #     template_name = 'lookbook.html'
# #     def get_queryset(self):
# #         queryset = Slide_of_collection.objects.filter(collection__name=self.request.Get.get('collection'))
# #         return query


# def show_lookbook(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     products = Product.objects.all()
#     collection = Collection.objects.all()
#     # filter(available=True)
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = products.filter(category=category)
#     return render(request,
#                   'product/list.html',
#                   {'category': category,
#                    'categories': categories,
#                    'products': products,
#                    'collection': collection,})lo