#! coding:utf-8

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView


class FilterableListView(ListView):

    non_searchable_fields = []

    def filter_queryset(self, kwargs):
        if self.model is not None:
            self.queryset = self.model._default_manager.filter(**kwargs)

    def get_queryset(self):
        kwargs = self.request.GET.dict()
            
        self.non_searchable_fields.append('page')

        for field in self.non_searchable_fields:
            try:
                kwargs.pop(field)
            except KeyError:
                pass

        if kwargs:
            self.filter_queryset(kwargs)

        return super(FilterableListView, self).get_queryset()

    def paginate(self, page_size=10, queryset=None):
        if not queryset:
            queryset = self.get_queryset()

        page = self.request.GET.get('page', 1)
       	paginator = Paginator(queryset, page_size)
    
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)

        return queryset
