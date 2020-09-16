from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import  Company,Teams,Gameweekwinner, Winner
from django.contrib.auth.models import User

class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        # company=Company.objects.filter(id=1)
        company=get_object_or_404(Company, id=1)
        gwwinner=Gameweekwinner.objects.all()
        winner=Winner.objects.all()

        args={
            'company':company,
            'gwwinner':gwwinner,
            'winner':winner
        }
        return render(request,self.template_name,args)

class TeamView(TemplateView):
    template_name='teams.html'

    def get(self,request):
        winner=Winner.objects.all()
        company=get_object_or_404(Company, id=1)
        teams=Teams.objects.all()
        args={
            'company':company,
            'teams':teams,
            'winner':winner
        }
        return render(request,self.template_name,args)

class AboutView(TemplateView):
    template_name='about.html'
    
    def get(self,request):
        company=get_object_or_404(Company, id=1)

        args={
            'company':company
        }
        return render(request,self.template_name,args)

class RewardsView(TemplateView):
    template_name='rewards.html'

    def get(self,request):
        company=get_object_or_404(Company, id=1)

        args={
            'company':company
        }
        return render(request,self.template_name,args)

class BlogsView(TemplateView):
    template_name='blog.html'

    def get(self,request):
        args={

        }
        return render(request,self.template_name,args)

class BlogsingleView(TemplateView):
    template_name='single.html'

    def get(self,request):
        args={

        }
        return render(request,self.template_name,args)


class ContactView(TemplateView):
    template_name='contact.html'

    def get(self,request):
        company=get_object_or_404(Company, id=1)

        args={
            'company':company
        }
        return render(request,self.template_name,args)