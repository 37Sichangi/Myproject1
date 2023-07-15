from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView
from .models import Customer, Property, Transaction

# Create your views here.
# def myview(request):
# 	return render(request, "index.html")
class Home(CreateView):
    # form_class=CustomerForm
    model=Customer
    template_name="customer.html"
    fields="__all__"
    
class Customer(ListView):
    model=Customer
    template_name='cust.html'
 
def property_list(request):
    properties = Property.objects.all()
    return render(request, 'property_list.html', {'properties': properties})

def property_detail(request, property_id):
    property = get_object_or_404(Property, pk=property_id)
    return render(request, 'property_detail.html', {'property': property})

@login_required
def property_submit(request):
    if request.method == 'POST':
        # Handle the submitted form data and create a new property
        # Example code:
        title = request.POST['title']
        description = request.POST['description']
        price = request.POST['price']
        area = request.POST['area']
        bedrooms = request.POST['bedrooms']
        bathrooms = request.POST['bathrooms']
        location = request.POST['location']
        photo = request.FILES['photo']
        owner = request.user

        new_property = Property(
            title=title,
            description=description,
            price=price,
            area=area,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            location=location,
            photo=photo,
            owner=owner
        )
        new_property.save()

        return redirect('property_detail', property_id=new_property.id)

    return render(request, 'property_submit.html')
	