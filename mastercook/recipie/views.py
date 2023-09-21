
from .forms import ProfileForm, recipieForm, user  # Import your ProfileForm or relevant form for updating profiles

from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.http import Http404, HttpResponse





from rest_framework import generics, request, status

from .models import Recipe, Profile
from .serializer import recipieSerializer, profileSerializer
import requests

from django.urls import reverse

from .decorators import custom_login_required

# @custom_login_required
def my_view(request):
    # Your view logic here
    return render(request, 'login.html')


class Listrecipie(generics.ListCreateAPIView):
    serializer_class = recipieSerializer
    queryset =Recipe.objects.all()

    def list(self,request,*args,**kwargs):
        queryset = self.get_queryset()
        serializer = recipieSerializer(queryset,many=True)
        return Response(serializer.data)

class searchrecipie(generics.ListCreateAPIView):
    serializer_class = recipieSerializer
    queryset = Recipe.objects.all()

    def list(self, request, *args, **kwargs):
        # Get the search query parameter from the request
        search_query = request.query_params.get('search', None)

        # If a search query is provided, filter the queryset by recipe name
        if search_query:
            queryset = self.get_queryset().filter(name__icontains=search_query)
        else:
            queryset = self.get_queryset()

        serializer = recipieSerializer(queryset, many=True)
        return Response(serializer.data)

class RecipeCreate(generics.CreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = recipieSerializer

    # No need to specify queryset here

    def perform_create(self, serializer):
        serializer.save()

class DetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = recipieSerializer
    queryset = Recipe.objects.all()

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class RecipeUpdateView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = recipieSerializer
    queryset = Recipe.objects.all()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class RecipeDeleteView(generics.DestroyAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Recipe.objects.all()
    serializer_class = recipieSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            instance.delete()
            return HttpResponse("Recipe deleted successfully.", status=204)
        except Exception as e:
            return HttpResponse(f"Recipe cannot be deleted: {str(e)}", status=400)


def list(request):
    response = requests.get('http://127.0.0.1:8000/recipie/list_recipie/')
    data = response.json()
    return render(request,'list.html',{'data':data})


def home(request):
    response = requests.get('http://127.0.0.1:8000/user/loginAPI/')
    data = response.json()
    return render(request,'home.html',{'data':data})


def Detail(request, pk):
    try:
        # Make an internal API request to your DRF endpoint
        response = DetailView.as_view()(request, pk=pk)

        # Check if the response is successful
        if response.status_code == 404:
            return render(request, 'error.html', {'error_message': 'Item not found'})

        data = response.data
        return render(request, 'Detail.html', {'data': data})
    except Exception as e:
        # Handle other exceptions if needed
        return render(request, 'error.html', {'error_message': str(e)})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe  # Import your Recipe model
 # Import your RecipeForm


def create_recipe(request):
    if request.method == 'POST':
        form = recipieForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user  # Assign the currently logged-in user to the recipe
            recipe.save()
            return redirect('list')  # Redirect to a success page or any desired URL
    else:
        form = recipieForm()

    return render(request, 'recipiecreate.html', {'form': form})

def update_recipie(request, pk):
    try:
        # Retrieve the profile object by primary key (pk)
        recipe = Recipe.objects.get(pk=pk)

        if request.method == 'POST':
            # If the request method is POST, process the form data
            form = recipieForm(request.POST, instance=recipe)
            if form.is_valid():
                form.save()
                return redirect('list')  # Redirect to the profile detail page
        else:
            # If the request method is GET, render the form with the current profile data
            form = recipieForm(instance=recipe)

        return render(request, 'recipiecreate.html', {'form': form, 'profile': recipe})
    except Profile.DoesNotExist:
        return render(request, 'error.html', {'error_message': 'Profile not found'})
    except Exception as e:
        # Handle other exceptions if needed
        return render(request, 'error.html', {'error_message': str(e)})






class profileCreate(generics.CreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = profileSerializer

    # No need to specify queryset here

    def perform_create(self, serializer):
        serializer.save()

class profileDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = profileSerializer
    queryset = Profile.objects.all()

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class profileUpdateView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = profileSerializer
    queryset = Profile.objects.all()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class profileDeleteView(generics.DestroyAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = profileSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            instance.delete()
            return HttpResponse("Recipe deleted successfully.", status=204)
        except Exception as e:
            return HttpResponse(f"Recipe cannot be deleted: {str(e)}", status=400)

def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            # Assign the current user to the profile
            profile.save()
            return redirect(reverse('profileDetail', args=[profile.id]))  # Redirect to a success page or any desired URL
    else:
        form = ProfileForm()

    return render(request, 'profilecreate.html', {'form': form})




def Detailprofile(request, pk):
    try:
        # Make an internal API request to your DRF endpoint
        response = profileDetailView.as_view()(request, pk=pk)

        # Check if the response is successful
        if response.status_code == 404:
            return render(request, 'error.html', {'error_message': 'Item not found'})

        data = response.data
        return render(request, 'profiledetail.html', {'data': data})
    except Exception as e:
        # Handle other exceptions if needed
        return render(request, 'error.html', {'error_message': str(e)})


def update_profile(request, pk):
    try:
        # Retrieve the profile object by primary key (pk)
        profile = Profile.objects.get(pk=pk)

        if request.method == 'POST':
            # If the request method is POST, process the form data
            form = ProfileForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                return redirect('list')  # Redirect to the profile detail page
        else:
            # If the request method is GET, render the form with the current profile data
            form = ProfileForm(instance=profile)

        return render(request, 'profilecreate.html', {'form': form, 'profile': profile})
    except Profile.DoesNotExist:
        return render(request, 'error.html', {'error_message': 'Profile not found'})
    except Exception as e:
        # Handle other exceptions if needed
        return render(request, 'error.html', {'error_message': str(e)})



def delete_profile(request, pk):
    try:
        # Retrieve the profile object by primary key (pk)
        profile = Profile.objects.get(pk=pk)

        if request.method == 'POST':
            # If the request method is POST, delete the profile
            profile.delete()
            return redirect('list')  # Redirect to the profile list page after deletion

        return render(request, 'deleteprofile.html', {'profile': profile})
    except Profile.DoesNotExist:
        raise Http404("Profile does not exist")  # Raise a 404 exception if the profile doesn't exist
    except Exception as e:
        # Handle other exceptions if needed
        return render(request, 'error.html', {'error_message': str(e)})


class data(generics.ListCreateAPIView):
    serializer_class = profileSerializer
    queryset =Profile.objects.all()




def Userid(request):
    response = requests.get('http://127.0.0.1:8000/recipie/DATA/')
    data = response.json()
    return render(request,'user.html',{'data':data})





def delete_recipie(request, pk):
    try:
        # Retrieve the profile object by primary key (pk)
       recipie = Recipe.objects.get(pk=pk)

       if request.method == 'POST':
            # If the request method is POST, delete the profile
            recipie.delete()
            return redirect('list')  # Redirect to the profile list page after deletion

       return render(request, 'deleterecipie.html', {'recipie': recipie})
    except Recipe.DoesNotExist:
        raise Http404("recipie does not exist")  # Raise a 404 exception if the profile doesn't exist
    except Exception as e:
        # Handle other exceptions if needed
        return render(request, 'error.html', {'error_message': str(e)})

