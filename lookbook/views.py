from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, DetailView
from .models import Collection, Slide_of_collection


class LookbookView(ListView):
    model=Collection
    template_name = 'lookbook.html'
    # def get_queryset(self):
    #     queryset = Slide_of_collection.objects.filter(collection__id=self.request.Get.get('collection'))
    #     return query

def show_lookbook(request, collection_id):
    collections = Collection.objects.all()
    slides_of_collection = Slide_of_collection.objects.all()
    collection = get_object_or_404(Collection, id=collection_id)
    slides = slides_of_collection.filter(collection=collection)
    return render(request,
                  'detail_lookbook.html',
                  {'slides': slides,
                   'collection': collection,
                   'collections': collections,})


class ShowSlideView(DetailView):
    model = Slide_of_collection
    

