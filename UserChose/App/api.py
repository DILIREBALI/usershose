from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from App.models import User, Chose
from App.serializers import ChoseSerializer, ChoseidSerializer


class getusershoes(View):
    def get(self,request):
        userid = request.GET.get('userid')
        user = User.objects.get(pk=userid)
        chose = user.chose_set
        choses = ChoseSerializer(chose, many=True)

        data = {
            'username': user.username,
            'shoses':choses.data
        }
        return JsonResponse(data=data, safe=False)


class updateusershoes(View):
    def post(self,request):
        phone = int(request.POST.get('phone'))
        name = request.POST.get('name')
        shoses = request.POST.get('shoes')
        print(shoses,type(shoses))
        user, _ = User.objects.get_or_create({'username':name, 'userphone':phone})
        for shose in shoses :
            Chose.color = shose[0]
            Chose.size = shose[1]
            Chose.user_id = user.id
            Chose.save()

        shoesid = Chose.objects.filter(user_id=user.id).only(id)
        data = {
            "success": 'true',
            "messsage": "ok",
            "result": {
                "userid":user.id ,
                "shoesid":ChoseidSerializer(shoesid, many=True).data
            }
        }
        return JsonResponse(data=data, safe=False)
