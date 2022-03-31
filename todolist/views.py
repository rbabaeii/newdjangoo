from django.shortcuts import redirect, render
from django.views import View
from .models import Data , Categories
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.
@method_decorator(login_required(login_url="/users/u/" ), name="dispatch")
class landing_page(View):
    def get(self , request):
        print(request.user)
        print("*****")
        print("=======")
        data = Data.objects.filter(user = request.user)
        Category = Categories.objects.all()
        return render(request , "todolist/index.html" , {"todos": data , "categories" : Category })
    def post(self , request):
        if "taskAdd" in request.POST:
            description = request.POST['description']
            dueDate = str(request.POST['date'])
            category = request.POST['category_select']
            data = Data(description = description ,dueDate = dueDate , category = Categories.objects.get(name = category) , user = request.user)
            data.save()
            return redirect('/')
        elif "taskDelete" in request.POST:
            for k in request.POST:
                try:
                    data = Data.objects.get(id = k , user = request.user)
                    data.delete()
                    return redirect("/")
                except:
                    continue

class Update(View):
    def get(self , request , todo_id):
        todos = Data.objects.get( id = todo_id , user = request.user)
        category = Categories.objects.all()
        return render(request , "todolist/todo.html" , {"todo":todos , 'categories' : category})
    def post(self , request , todo_id):
            title = request.POST['description']
            due_date = str(request.POST['date'])
            categories = request.POST['category_select']
            todo = Data.objects.get(id = todo_id)
            todo.description = title
            todo.dueDate = due_date
            todo.category = Categories.objects.get(name = categories)
            todo.save()
            return redirect("/")
