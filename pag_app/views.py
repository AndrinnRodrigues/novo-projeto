from django.shortcuts import render, redirect
from pag_app.models import Pessoa

# Create your views here.
def home(request):
    data = Pessoa.objects.all()
    return render(request,"pag_app/home.html", context={"dados":data})


def salvar(request):
    if request.POST:
        if request.POST.get("nome"):
            Pessoa.objects.create(nome=request.POST.get("nome"))
    return redirect(home)


def deletar(request,id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect(pag_deletar)


def atualizar(request,id):
    pessoa = Pessoa.objects.get(id=id)
    if request.POST:
        if request.POST.get("nome"):
            pessoa.nome = request.POST.get("nome")
            pessoa.save()
            return redirect(pag_atualizar)
        
    return render(request,"pag_app/atualizar_dados.html", context={"dados":pessoa})


def pesquisar(request):
    if request.POST:
        nome = request.POST.get("nome")
        pessoa = Pessoa.objects.filter(nome__icontains=nome)
        
    else:
        pessoa = Pessoa.objects.all()
     
    return render(request, "pag_app/pesquisar.html", context={"dados":pessoa})   


def pag_deletar(request):
    if request.POST:
        nome = request.POST.get("nome")
        pessoa = Pessoa.objects.filter(nome__icontains=nome)
    else:
        pessoa = Pessoa.objects.all()
        
    return render(request, "pag_app/deletar.html", context={"dados":pessoa})   
    

def pag_atualizar(request):  
    if request.POST:
        nome = request.POST.get("nome")
        pessoa = Pessoa.objects.filter(nome__icontains=nome)
    else:
        pessoa = Pessoa.objects.all()
        
    return render(request, "pag_app/atualizar.html", context={"dados":pessoa})  

def pag_criar(request):
    nome= ""
    data_nascimento = ""
    email = ""
    pais = ""
    
    if request.POST:
        nome = request.POST.get("nome")
        data_nascimento = request.POST.get("data_nascimento")
        email = request.POST.get("email")
        pais = request.POST.get("pais")
        
        if nome:
            pessoa = Pessoa.objects.create(nome=nome,
                data_nascimento=data_nascimento,
                email=email,
                pais=pais)
            
        return render(request, "pag_app/criar.html", context={"nome":pessoa.nome, "id":pessoa.id})
            
    return render(request, "pag_app/criar.html", context={"nome": nome, "data_nascimento": data_nascimento, "email": email, "pais": pais})

def home_2(request):
    pessoa = Pessoa.objects.all().order_by('-id')[:10]
    
    return render(request, "pag_app/home.html", context={"dados":pessoa})   
   




