from django.shortcuts import render
from django.http import HttpResponse
from . import models


# тут только "логика" - функции для обработки и возврат данных


def index(request):
    # return HttpResponse("Это чистая индекс страница")
    context = {

    }
    return render(request, 'app_second/pages/index.html', context)


def func(description, name="Apple"):
    pass


def home(request):
    context = {

    }
    return render(request, 'app_second/pages/home.html', context)


def login(request):
    context = {

    }
    return render(request, 'app_second/pages/login.html', context)


def about(request):
    context = {

    }
    return render(request, 'app_second/pages/about.html', context)


def origin_home(request):
    context = {

    }
    return render(request, 'app_second/pages/origin_home.html', context)


def todo_detail(request, todo_id):
    print(request)
    if request.method == "GET":
        print("это GET запрос")
    if request.method == "POST":
        print("это POST запрос")
    if request.method == "PUT":
        print("это PUT запрос")
    if request.method == "DELETE":
        print("это DELETE запрос")

    # print("request.method: ", request.method)
    # print("request.path: ", request.path)
    # print("request.headers: ", request.headers)
    # print("request.META: ", )

    # пробегаемся по ключам словаря
    # for key, value in request.META.keys():

    # пробегаемся по значениям словаря
    # for key, value in request.META.values():

    # пробегаемся по парам: ключ-значение
    # for key, value in request.META.items():
    #     print(f"{key}: {value}")
    # print("request.data: ", request.data)
    # print("request.GET: ", request.GET)

    is_completed = False
    if is_completed:
        pass
    else:
        pass

    list = [1, 2, 3]
    for i in list:
        index = list.index(i)
        # print(i)
        pass

    obj = models.Task.objects.get(id=todo_id)

    context = {
        "todo": obj
    }

    return render(request, 'app_second/pages/DetailTodo.html', context)


def todo_list(request):
    print(request)
    if request.method == "GET":
        print("это GET запрос")
    if request.method == "POST":
        print("это POST запрос")
    if request.method == "PUT":
        print("это PUT запрос")
    if request.method == "DELETE":
        print("это DELETE запрос")

    # print("request.method: ", request.method)
    # print("request.path: ", request.path)
    # print("request.headers: ", request.headers)
    # print("request.META: ", )

    # пробегаемся по ключам словаря
    # for key, value in request.META.keys():

    # пробегаемся по значениям словаря
    # for key, value in request.META.values():

    # пробегаемся по парам: ключ-значение
    # for key, value in request.META.items():
    #     print(f"{key}: {value}")
    # print("request.data: ", request.data)
    # print("request.GET: ", request.GET)

    is_completed = False
    if is_completed:
        pass
    else:
        pass

    list = [1, 2, 3]
    for i in list:
        index = list.index(i)
        # print(i)
        pass

    obj = models.Task.objects.all()

    print(f"obj: {obj}")
    print(f"obj count: {obj.count()}")

    context = {"list": obj}

    return render(request, 'app_second/pages/todo_list.html', context)


def todo_create(request):
    print("todo_create")
    if request.method == "POST":
        print("это POST запрос")

        # вызывается Exception (исключение)
        # title = request.POST["title"]
        title1 = request.POST.get("title", "заголовок по умолчанию")
        description1 = request.POST.get("description", "описание по умолчанию")

        obj = models.Task.objects.create(
            title=title1,
            description=description1
        )
        obj.save()


        # приём и обработка данных
    context = {}
    return render(request, 'app_second/pages/CreateTodo.html', context)


# def idea_view(request, idea_int):

# detail = {
#     "title": "Выгулять собаку"
#     "description": "Нужно обязательно не забыть выгулять сегодня собаку",
#     "time": "2022-10-05",
#     "is_completed": False
# }
#
# list = {
#     "1": {
#         "title": "Выгулять собаку 1"
#         "description": "Нужно обязательно не забыть выгулять сегодня собаку",
#         "time": "2022-10-05",
#         "is_completed": False
#     },
#     "2": {
#         "title": "Купить еды"
#         "description": "Нужно обязательно купить еды",
#         "time": "2022-10-08",
#         "is_completed": True
#     },
#     "3": {
#         "title": "Купить собаке еды"
#         "description": "Нужно обязательно купить собаке еды",
#         "time": "2022-10-12",
#         "is_completed": False
#     }
# }
#     idea = IdeaTestModel.objects.get(id=idea_int)
#     comments = IdeaTestCommentModel.objects.filter(idea_foreign_key_field=idea)
#     page = PaginationClass.paginate(request=request, objects=comments, num_page=5)
#     response = 0
#     context = {
#         'response': response,
#         'idea': idea,
#         'page': page,
#     }
#     return render(request, 'idea/idea_view.html', context)
#
#
# def idea_create(request):
#     response = 0
#     category = IdeaTestModel.get_all_category()
#     if request.method == 'POST':
#         author = UserModel.objects.get(user=request.user)
#         name_char_field = request.POST.get("name_char_field")
#         category_slug_field = request.POST.get("category_slug_field")
#         short_description_char_field = request.POST.get("short_description_char_field")
#         full_description_text_field = request.POST.get("full_description_text_field")
#         avatar_image_field = request.FILES.get("avatar_image_field")
#         addiction_file_field = request.FILES.get("addiction_file_field")
#         IdeaTestModel.objects.create(
#             author=author,
#             name_char_field=name_char_field,
#             category_slug_field=category_slug_field,
#             short_description_char_field=short_description_char_field,
#             full_description_text_field=full_description_text_field,
#             avatar_image_field=avatar_image_field,
#             addiction_file_field=addiction_file_field,
#             is_visible=False,
#         )
#
#         response = 1
#     context = {
#         'response': response,
#         'category': category,
#     }
#     return render(request, 'idea/idea_create.html', context)
#
#
# def idea_list(request, category_slug='All'):
#     categoryes = IdeaTestModel.get_all_category()
#     num_page = 5
#     if category_slug == 'idea_change_visibility':
#         ideas = IdeaTestModel.objects.filter(is_visible=False)
#     elif category_slug.lower() != 'all':
#         ideas = IdeaTestModel.objects.filter(category_slug_field=category_slug, is_visible=True)
#     else:
#         ideas = IdeaTestModel.objects.filter(is_visible=True)
#     if request.method == 'POST':
#         search_char_field = request.POST.get("search_char_field")
#         if search_char_field:
#             ideas = ideas.filter(name_char_field__icontains=search_char_field)
#         num_page = 100
#     page = PaginationClass.paginate(request=request, objects=ideas, num_page=num_page)
#     response = 0
#     context = {
#         'response': response,
#         'page': page,
#         'categoryes': categoryes,
#     }
#     return render(request, 'idea/idea_list.html', context)