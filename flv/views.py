#! coding:utf-8

from django.views.generic.list import ListView

class FilterableListView(ListView):


    def filter_queryset(self, kwargs):
        if self.model is not None:
            self.queryset = self.model._default_manager.filter(**kwargs)

    def get_queryset(self):
        kwargs = self.request.GET.dict()
        if kwargs:
            self.filter_queryset(kwargs)
        return super(FilterableListView, self).get_queryset()
