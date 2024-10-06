from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# View to render the home page and handle user login
def home(request):
    # Retrieve all records from the database
    records = Record.objects.all()
    
    # Check if the request method is POST (user attempting to log in)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # Log in the user
            messages.success(request, "You Have Been Logged In")
            return redirect('home') # Redirect to home page after successful login
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('home') # Redirect back to login page if login fails
    else:
        return render(request, 'home.html', {'records':records})


# View to log out the user
def logout_user(request):
    logout(request) # Log out the user
    messages.success(request, "You Have Been Logged Out")
    return redirect('home') # Redirect to login page after logout


# View to handle user registration
def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST) # Instantiate the form with POST data
        if form.is_valid():
            form.save() # Save the new user
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user) # Log in the user
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home') # Redirect to home page after registration
    else:
        form = SignUpForm() # If not POST, create a blank form
        return render(request, 'register.html', {'form':form})
    
    # In case of invalid form submission, return the registration page with the form
    return render(request, 'register.html', {'form':form})


# View to display a specific customer record
def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look up records by ID
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
         messages.success(request, "You Must Be Logged In To View That Page...")
         return redirect('home')  # Redirect to login page if user is not authenticated


# View to delete a specific record
def delete_record(request, pk):
    if request.user.is_authenticated:
        #Look up records by ID
        delete_it = Record.objects.get(id=pk)
        delete_it.delete() # Delete the record
        messages.success(request, "Record Deleted Successfully!")
        return redirect('home') # Redirect to home page after deletion
    else:
        messages.success(request, "You Must Be Logged In To Delete Records...")
        return redirect('home') # Redirect to login page if user is not authenticated
    

# View to add a new record
def add_record(request):
    form = AddRecordForm(request.POST or None) # Instantiate the form with POST data
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save() # Save the new record
                messages.success(request, "Record Added Successfully!")
                return redirect('home') # Redirect to home page after adding record
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "You Must Be Logged In To Add Records...")
        return redirect('home') # Redirect to login page if user is not authenticated
    

# View to update an existing record
def update_record(request, pk):
     if request.user.is_authenticated:
         # Look up records by ID
         current_record = Record.objects.get(id=pk)
         form = AddRecordForm(request.POST or None, instance=current_record) # Instantiate form with current record
         if form.is_valid():
            form.save() # Save the updated record
            messages.success(request, "Record Has Been Updated Successfully!")
            return redirect('home') # Redirect to home page after updating record
         return render(request, 'update_record.html', {'form':form})
     else:
        messages.success(request, "You Must Be Logged In To Update Records...")
        return redirect('home') # Redirect to login page if user is not authenticated





