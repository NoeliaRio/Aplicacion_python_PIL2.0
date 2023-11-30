from django.views.generic import ListView

class FilteredListView(ListView):
    filterset_class = None

    def get_queryset(self, child_queryset=None):
        """
        """
        # Get the queryset however you usually would.  For example:
        if child_queryset:
            queryset = child_queryset
        else:
            queryset = super().get_queryset()
        # Then use the query parameters and the queryset to
        # instantiate a filterset and save it as an attribute
        # on the view instance for later.
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        # incluir filtrado por POST
        if 'action' in self.request.POST:
            if self.request.POST['action'] == 'searchdata':
                self.filterset = self.filterset_class(self.request.POST, queryset=queryset)
        # Return the filtered queryset
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the filterset to the template - it provides the form.
        context['filterset'] = self.filterset
        return context