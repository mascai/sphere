# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Club, Event, Comment
from model.forms import UserForm, UserProfileForm, CommentForm, EventFilterForm, ClubFilterForm, RegisterForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Count
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.http import JsonResponse
import json


@login_required
def home(request):
    return render(request, 'model/post_list.html')

class SignUpView(CreateView):
    template_name = 'model/signup.html'
    form_class = UserCreationForm

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)




def change_rating(request):
    # ajax POST request
    thread_id = request.POST['thread_id'] #in URL
    delta = int(request.POST['delta'])
    t = Club.objects.get(id=thread_id)
    t.likes += delta
    t.save()

    return HttpResponse(json.dumps({
        'new_rating': t.likes,
        }), mimetype='application/json') 


@login_required
def like_category(request):

    cat_id = None
    if request.method == 'GET':
        cat_id = request.GET['club_id']

    likes = 0
    if cat_id:
        cat = Club.objects.get(id=int(cat_id))
        if cat:
            likes = cat.likes + 1
            cat.likes =  likes
            cat.save()

    return HttpResponse(likes)

def post_list(request):
    posts = Club.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'model/post_list.html', {'posts': posts})

#вывод списка клубов
def club_list(request):
    posts = Club.objects.filter(created_date__lte=timezone.now()).order_by('published_date').annotate(cnt_comments=Count('comment'))
    #club_comment_cnt = Club.objects.annotate(cnt_comments=Count('comment'))
    #club_comment_cnt[0].cnt_comments
    form = ClubFilterForm(request.GET)
    if form.is_valid():
        if form.cleaned_data["club_title"]:
            posts = posts.filter(title__contains=form.cleaned_data["club_title"])
            
    return render(request, 'model/club_list.html', {'posts': posts, 'form': form})
#вывод списка соревнований
def event_list(request):
    events = Event.objects.filter(event_date__lte=timezone.now()).order_by('event_date')
    form = EventFilterForm(request.GET)
    if form.is_valid():
        if form.cleaned_data["event_title"]:
            events = events.filter(title=form.cleaned_data["event_title"])
    return render(request, 'model/event_list.html', {'events': events, 'form': form })

def club_detail(request, club_id):
    post = get_object_or_404(Club, id=club_id) #если объект найден, то вернет id в перем post
    
    #comments = Comment.objects.get(post.title)
    comments = Comment.objects.select_related("author").filter(club=club_id)
    if request.method == 'POST':
        #form = CommentForm(request.POST)
        form = CommentForm(request.POST or None, initial={
        "club": post #default club name in form
        })
        #form.author = request.user
        if form.is_valid():
            #form = form.save(commit=False)
            form.instance.author = request.user
            #form.author = request.user
            form.published_date = timezone.now()
            form.save()
            return redirect("http://127.0.0.1:8000/"+unicode(club_id))
            #form = CommentForm()
    else:
        form = CommentForm(initial={
        "club": post #default club name in form
        })
    return render(request, "model/club_detail.html", {'post': post, 'form': form, 'comments': comments })






def register(request):

    # Логическое значение указывающее шаблону прошла ли регистрация успешно.
    # В начале ему присвоено значение False. Код изменяет значение на True, если регистрация прошла успешно.
    registered = False

    # Если это HTTP POST, мы заинтересованы в обработке данных формы.
    if request.method == 'POST':
        # Попытка извлечь необработанную информацию из формы.
        # Заметьте, что мы используем UserForm и UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # Если в две формы введены правильные данные...
        if user_form.is_valid() and profile_form.is_valid():
            # Сохранение данных формы с информацией о пользователе в базу данных.
            user = user_form.save()

            # Теперь мы хэшируем пароль с помощью метода set_password.
            # После хэширования мы можем обновить объект "пользователь".
            user.set_password(user.password)
            user.save()

            # Теперь разберемся с экземпляром UserProfile.
            # Поскольку мы должны сами назначить атрибут пользователя, необходимо приравнять commit=False.
            # Это отложит сохранение модели, чтобы избежать проблем целостности.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Предоставил ли пользователь изображение для профиля?
            # Если да, необходимо извлечь его из формы и поместить в модель UserProfile.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Теперь мы сохраним экземпляр модели UserProfile.
            profile.save()

            # Обновляем нашу переменную, чтобы указать, что регистрация прошла успешно.
            registered = True

        # Неправильная формы или формы - ошибки или ещё какая-нибудь проблема?
        # Вывести проблемы в терминал.
        # Они будут также показаны пользователю.
        else:
            print user_form.errors, profile_form.errors

    # Не HTTP POST запрос, следователь мы выводим нашу форму, используя два экземпляра ModelForm.
    # Эти формы будут не заполненными и готовы к вводу данных от пользователя.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Выводим шаблон в зависимости от контекста.
    return render(request,
            'model/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )


def user_login(request):

    # Если запрос HTTP POST, пытаемся извлечь нужную информацию.
    if request.method == 'POST':
        # Получаем имя пользователя и пароль, вводимые пользователем.
        # Эта информация извлекается из формы входа в систему.
                # Мы используем request.POST.get('<имя переменной>') вместо request.POST['<имя переменной>'],
                # потому что request.POST.get('<имя переменной>') вернет None, если значения не существует,
                # тогда как request.POST['<variable>'] создаст исключение, связанное с отсутствем значения с таким ключом
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Используйте Django, чтобы проверить является ли правильным
        # сочетание имя пользователя/пароль - если да, то возвращается объект User.
        user = authenticate(username=username, password=password)

        # Если мы получили объект User, то данные верны.
        # Если получено None (так Python представляет отсутствие значения), то пользователь
        # с такими учетными данными не был найден.
        if user:
            # Аккаунт активен? Он может быть отключен.
            if user.is_active:
                # Если учетные данные верны и аккаунт активен, мы можем позволить пользователю войти в систему.
                # Мы возвращаем его обратно на главную страницу.
                login(request, user)
                return HttpResponseRedirect('/admin/')
            else:
                # Использовался не активный аккуант - запретить вход!
                return HttpResponse("Your account is disabled.")
        else:
            # Были введены неверные данные для входа. Из-за этого вход в систему не возможен.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # Запрос не HTTP POST, поэтому выводим форму для входа в систему.
    # В этом случае скорее всего использовался HTTP GET запрос.
    else:
        # Ни одна переменная контекста не передается в систему шаблонов, следовательно, используется
        # объект пустого словаря...
        return render(request, 'model/login.html', {})



# Используйте декоратор login_required(), чтобы гарантировать, что только авторизированные пользователи смогут получить доступ к этому представлению.
@login_required
def user_logout(request):
    # Поскольку мы знаем, что только вошедшие в систему пользователи имеют доступ к этому представлению, можно осуществить выход из системы
    logout(request)

    # Перенаправляем пользователя обратно на главную страницу.
    return HttpResponseRedirect('http://127.0.0.1:3000/')



