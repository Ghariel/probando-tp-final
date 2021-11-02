from django import views
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

from .forms import URLForm2
from .models import URLAlias, TestURLAlias
import nanoid

import json

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

"""
_NANO_DICT = "abcdefz-"

@method_decorator(csrf_exempt, name='dispatch')
class Api2(views.View):
    model=TestURLAlias
    def post(self, request):
        data=json.loads(request.body.decode("utf-8")   )
        print(f" data es {data} y es de tipo {type(data)}"   )
        url=data.get('url')
        print(f"url es {url} y es de tipo {type(url)}")
        
        
        Url=TestURLAlias(fullurl=url)
        alias=nanoid.generate(alphabet=_NANO_DICT, size=5)
        Url.alias=alias
        Url.save()

        response={"alias": alias}
        print(f"response es {response}")
        return JsonResponse(response, status=201)

"""


"""



def index(request):


    if request.method == "POST":
        # Se puede acceder a la informacion del POST de forma
        form = URLForm2(request.POST)
        if form.is_valid():
            fullurl = form.cleaned_data.get("fullurl")
            url = URLAlias(fullurl=fullurl)
            alias = nanoid.generate(size=5)
            url.alias=alias
            url.save()
            ctx  = {"title": "Bienvenido al url alias", "url": fullurl, "alias": alias}
            return render(request, "urlalias/registrado.html", ctx)
        else:
            return HttpResponse("El formulario es invalido") 
    
    form = URLForm2()

    ctx  = {"title": "Bienvenido al url alias", "form": form}
	

    return render(request, "urlalias/home.html", ctx)



//def resolve_alias(request, alias):
//    resultado = URLAlias.objects.get(alias=alias)
//    resultado.visitas += 1
//    resultado.save()
//
//    # return HttpResponse(f"La URL para el alias {alias} es {resultado.fullurl}")
//    return HttpResponseRedirect(resultado.fullurl) 

"""
imagen_1 = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠤⠒⠈⠉⠉⠉⠉⠒⠀⠀⠤⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠁⠀⠀⠀⠀⠀⠀⢀⣄⠀⠀⠀⠀⠑⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠰⠿⠿⠿⠣⣶⣿⡏⣶⣿⣿⠷⠶⠆⠀⠀⠘⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠠⠴⡅⠀⠀⠠⢶⣿⣿⣷⡄⣀⡀⡀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀
⠀⣰⡶⣦⠀⠀⠀⡰⠀⠀⠸⠟⢸⣿⣿⣷⡆⠢⣉⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢹⣧⣿⣇⠀⠀⡇⠀⢠⣷⣲⣺⣿⣿⣇⠤⣤⣿⣿⠀⢸⠀⣤⣶⠦⠀⠀⠀⠀
⠀⠀⠙⢿⣿⣦⡀⢇⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⡜⣾⣿⡃⠇⢀⣤⡀⠀
⠀⠀⠀⠀⠙⢿⣿⣮⡆⠀⠙⠿⣿⣿⣾⣿⡿⡿⠋⢀⠞⢀⣿⣿⣿⣿⣿⡟⠁⠀
⠀⠀⠀⠀⠀⠀⠛⢿⠇⣶⣤⣄⢀⣰⣷⣶⣿⠁⡰⢃⣴⣿⡿⢋⠏⠉⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠠⢾⣿⣿⣿⣞⠿⣿⣿⢿⢸⣷⣌⠛⠋⠀⠘⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠙⣿⣿⣿⣶⣶⣿⣯⣿⣿⣿⣆⠀⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣯⡙⢿⣿⣿⠟⡁⠰⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⡟⠈⢩⣥⣾⣷⠐⡌⠙⠃⠀"""

imagen_2 ="""
⣇⣿⠘⣿⣿⣿⡿⡿⣟⣟⢟⢟⢝⠵⡝⣿⡿⢂⣼⣿⣷⣌⠩⡫⡻⣝⠹⢿⣿⣷
⡆⣿⣆⠱⣝⡵⣝⢅⠙⣿⢕⢕⢕⢕⢝⣥⢒⠅⣿⣿⣿⡿⣳⣌⠪⡪⣡⢑⢝⣇
⡆⣿⣿⣦⠹⣳⣳⣕⢅⠈⢗⢕⢕⢕⢕⢕⢈⢆⠟⠋⠉⠁⠉⠉⠁⠈⠼⢐⢕⢽
⡗⢰⣶⣶⣦⣝⢝⢕⢕⠅⡆⢕⢕⢕⢕⢕⣴⠏⣠⡶⠛⡉⡉⡛⢶⣦⡀⠐⣕⢕
⡝⡄⢻⢟⣿⣿⣷⣕⣕⣅⣿⣔⣕⣵⣵⣿⣿⢠⣿⢠⣮⡈⣌⠨⠅⠹⣷⡀⢱⢕
⡝⡵⠟⠈⢀⣀⣀⡀⠉⢿⣿⣿⣿⣿⣿⣿⣿⣼⣿⢈⡋⠴⢿⡟⣡⡇⣿⡇⡀⢕
⡝⠁⣠⣾⠟⡉⡉⡉⠻⣦⣻⣿⣿⣿⣿⣿⣿⣿⣿⣧⠸⣿⣦⣥⣿⡇⡿⣰⢗⢄
⠁⢰⣿⡏⣴⣌⠈⣌⠡⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣬⣉⣉⣁⣄⢖⢕⢕⢕
⡀⢻⣿⡇⢙⠁⠴⢿⡟⣡⡆⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣵⣵⣿
⡻⣄⣻⣿⣌⠘⢿⣷⣥⣿⠇⣿⣿⣿⣿⣿⣿⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣷⢄⠻⣿⣟⠿⠦⠍⠉⣡⣾⣿⣿⣿⣿⣿⣿⢸⣿⣦⠙⣿⣿⣿⣿⣿⣿⣿⣿⠟
⡕⡑⣑⣈⣻⢗⢟⢞⢝⣻⣿⣿⣿⣿⣿⣿⣿⠸⣿⠿⠃⣿⣿⣿⣿⣿⣿⡿⠁⣠
⡝⡵⡈⢟⢕⢕⢕⢕⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⣿⣿⠿⠋⣀⣈⠙
⡝⡵⡕⡀⠑⠳⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⢉⡠⡲⡫⡪⡪⡣"""

imagen_3 = """
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣀⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣴⣿⣿⠿⣫⣥⣄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⠄⠄⠄⠾⢿⢟⣵⣾⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⣰⡿⣀⣤⣴⣾⣿⡇⠙⠛⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⣠⣾⣿⣿⣿⣿⣿⣿⣿⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⣴⣿⣿⠿⠛⠉⢩⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⣀⣀⡀⠄⠄⠄⠄
⠄⠄⠄⠄⠈⠛⠉⠄⠄⠄⠄⢸⣿⣿⡇⠄⠄⠄⠄⠄⠄⢀⣼⡿⣫⣾⠆⠄⠄⠄
⠄⠄⠄⠄⢀⣶⣶⣶⣶⣶⣶⣿⣿⣿⠇⠄⠄⠄⣠⣎⣠⣴⣶⠎⠛⠁⠄⠄⠄⠄
⠄⠄⠄⠄⣾⣿⣿⣿⣿⠿⠿⠟⠛⠋⠄⠄⢀⣼⣿⠿⠛⣿⡟⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠛⠉⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⠉⠄⠄⢸⣿⡇⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣼⣿⣿⣿⡿⠿⠃⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠋⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄"""

imagen_4 = """
⠻⣦⡈⠛⢿⡌⢆⢂⠹⣿⣧⡄⡄⠹⡄⢆⡟⢄⠉⢟⣮⣷⢄⠐⢤⡤⢤⣬⣭⣭
⣷⣤⠙⣶⣦⠙⡌⢻⠂⠘⣿⣷⢹⠄⢳⠘⣿⡟⣿⡄⢳⡆⢳⠛⢢⠈⠉⠛⠛⠛
⢿⣿⣷⣀⠈⠓⠌⠂⠘⢆⠈⢙⣎⢣⠘⡆⢣⡛⣿⡇⢀⡙⠚⠶⠶⠿⠷⠶⠒⠒
⣾⠿⣿⣿⣦⣄⣁⣀⣠⡀⠡⠄⠳⡛⢆⠱⠈⢧⣿⡇⠸⠟⠉⠐⠠⠄⠄⠄⣼⣿
⣿⣷⣬⣉⣛⣛⠛⠿⠿⣧⣷⣦⣄⠘⢿⡆⠡⠘⣀⡇⢠⣶⣷⣮⣤⣤⣴⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⢿⡀⠄⠉⡇⢸⣿⣿⣿⣉⣉⣉⣉⣉⣰
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⣦⡙⠄⠄⠁⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⡙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠁⣿⣿⣷⣌⠄⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣦⣀⡨⣝⡻⠿⣻⣿⣧⣄⠄⠄⣿⣿⣿⣿⣿⣦⡀⢻⣿⣿⣿⣿⣿⡿⠿⣿
⣿⣿⣿⣿⡇⢿⡛⢿⣿⣿⣿⣿⣧⠘⣿⣛⣻⣿⣿⣿⣿⣤⡿⢿⠿⣛⡃⠄⣸⣿
⡹⣿⣿⣿⣿⣼⣷⣶⣝⢿⣿⣿⣿⣧⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⣿⢇⣈⣼⣿⣿
⣿⣜⢿⣭⢻⣿⣿⣿⣯⢧⠙⢻⠛⣛⣛⠛⠛⠿⠿⠟⣛⣥⣶⣼⢏⣾⣿⣿⣿⣿
⣿⣿⣎⠿⣇⢻⣿⣿⣿⡌⢷⣆⢭⣓⣒⣒⣛⣣⣶⠞⣵⣿⣿⣿⡿⣱⣾⡟⣵⣿
⣿⣿⣿⣤⣻⡘⣿⣿⣿⣷⡜⢻⣮⣛⣛⣟⣫⡿⣛⣴⣿⣿⣿⣿⢃⣿⣿⣷⣿⣿
⣿⣿⣿⣿⣷⣣⢹⣿⣿⣿⣿⣯⡙⠛⠛⠛⢛⣺⣿⣿⣿⣿⣿⠇⣼⢫⣵⣿⣿⣿"""

@method_decorator(csrf_exempt, name='dispatch')
class Api(views.View):
    model=TestURLAlias
    def post(self, request):
        data=json.loads(request.body.decode("utf-8")   )
        print(f" data es {data} y es de tipo {type(data)}"   )
        url=data.get('url')
        print(f"url es {url} y es de tipo {type(url)}")
        
        try:#evito guardar varias veces el mismo link
            link = url
            obj = TestURLAlias.objects.get(fullurl=link)
            alias_parcial = (obj.alias)
            print(imagen_1)
            print("          LINK REPETIDO")
            #print(f"alias asignado: {obj.alias}")
        except:

            Url=TestURLAlias(fullurl=url)
            alias_r = nanoid.generate(size=7)#nanoid
            #alias_r = "dZKrFN7"#prueba de de alias repetido
            
            while True:#con esto pretendo evitar que se guarden alias iguales
               
                try: 
                    alias_enc = TestURLAlias.objects.get(alias = alias_r)
                    alias_r = nanoid.generate(size=7)#nanoid
                    print(imagen_3)
                    print(f"          ALIAS REPETIDO: {alias_enc.alias}")
                except:
                    alias_parcial = alias_r
                    break

            Url.alias=alias_parcial
            Url.save()
            print(imagen_2)
            print("          LINK NUEVO")
        alias = f"http://localhost:8000/{alias_parcial}"#para usar en localhost
        #alias = f"http://www.Dominio/{alias_parcial}"#para usar en servidor en la nube

        response={"alias": alias}
        print(f"response es {response}")
        return JsonResponse(response, status=201)

def redir(request, pk):#redirecciona al enlace original request,
    
    try:#tiene una funcion de contar visitas basica

        te_encontre = TestURLAlias.objects.get(alias=pk)
        print(f"\nFue visitado {te_encontre.visitas} veces")
        contador = te_encontre.visitas
        te_encontre.visitas = contador + 1
        te_encontre.save()
        redireccionar = te_encontre.fullurl
        print(f"\nFue visitado {te_encontre.visitas} veces")
        print(imagen_4)

    except:#en caso de no encontrar el link en la base de datos se podria poner otra pagina con un mensaje en plan "URL no encontrado"
        #de momento lo envio al home
        redireccionar = "http://localhost:8000/"
        #redireccionar = f"http://www.Dominio/"#para usar en servidor en la nube
        print(imagen_3)
        print("          PANICO.jpg\n")

    return redirect(redireccionar)

