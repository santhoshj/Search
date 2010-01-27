# Create your views here.

from django.http import HttpResponse
from search.s1.models import Bundle,Module,FileType,Files
from django.shortcuts import render_to_response
from django import forms
from django.utils import simplejson

def index(request):
    if request.GET:
        return HttpResponse("Search page")
    else:
        form = searchForm()
    return render_to_response('search/form.html', {'form' : form,})


def search(request):
    if request.GET:
        print request.GET, dir(request.GET)
        return HttpResponse("Search page")
    all_bundles = Bundle.objects.all()
    all_bundle_names = []
    for bundle in all_bundles:
        all_bundle_names.append(bundle.name)
    results = {}
    results['bundles'] = all_bundle_names
    return render_to_response('search/search.html', results)

def bundle_lookup(request):
    results = []
    if request.method == "GET":
        if request.GET.has_key(u'q'):
            value = request.GET[u'q']
            # Ignore queries shorter than length 3
            #if len(value) > 2:
            model_results = Bundle.objects.filter(name__icontains=value)
            results = [ (x.__unicode__(), x.id) for x in model_results ]
    json = simplejson.dumps(results)
    print "Results: ",results
    return HttpResponse(json, mimetype='application/json')

    
#    return HttpResponse("Nothing")


class searchForm(forms.Form):
    bundle = forms.CharField(max_length=50, label='Bundle', widget=forms.TextInput(attrs={'placeholder': 'Name of the bundle'}))
    # A custom empty label
    bundle1 = forms.ModelChoiceField(queryset=Bundle.objects.all(), empty_label="Any")

    bundle_pk = forms.IntegerField(widget=forms.HiddenInput())
    module = forms.CharField(max_length=50)
    version = forms.CharField(max_length=20)
    filetype = forms.CharField(max_length=20)
    
    class Media:
        js = ('jquery.js','jquery.bgiframe.min.js','jquery.ajaxQueue.js','thickbox-compressed.js','jquery.autocomplete.js')
        css = {
            'all' : ('jquery.autocomplete.css','thickbox.css')
            }
