from django.views.generic import CreateView
from django.shortcuts import redirect

from .models import Author
from .forms import AuthorForm, BookFormSet


class AddAuthorView(CreateView):
    # template_name = 'create_author.html'
    template_name = 'index.html'
    form_class = AuthorForm

    def get_context_data(self, **kwargs):
        context = super(AddAuthorView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = BookFormSet(self.request.POST)
        else:
            context['formset'] = BookFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            # assuming your model has ``get_absolute_url`` defined.
            return redirect(self.object.get_absolute_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

# def manage_books(request, author_id):
#     author = Author.objects.get(pk=author_id)
#     BookInlineFormSet = inlineformset_factory(Author, Book)
#     if request.method == "POST":
#         formset = BookInlineFormSet(
#             request.POST, request.FILES, instance=author)
#         if formset.is_valid():
#             formset.save()
#             return HttpResponseRedirect(author.get_absolute_url())
#         else:
#             formset = BookInlineFormSet(instance=author)
#         return render_to_response("manage_books.html", {
#             "formset": formset,
#         })
