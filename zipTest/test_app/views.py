from django.http import JsonResponse
from django.shortcuts import render
import requests
from .forms import GitForm


def info_user(request):
    username = 'AntonBalmakov'
    token = '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'
    aunt_user = requests.get("https://api.github.com/users/", auth=(username, token)).json()

    if request.method == 'POST':
        form = GitForm(request.POST)
        form.is_valid()
        pulls = requests.get(f'https://api.github.com/search/issues?q=author:'
                             f'{form.cleaned_data["nickname"]}'
                             f'+ is:merged').json()  # пoртянка всех смердженных пул реквестов

        no_merge_pulls = requests.get(
            f'https://api.github.com/search/issues?q=user:'
            f'{form.cleaned_data["nickname"]}'
            f'+review:approved').json()  # не смерженые пул-реквэсты

        no_merge_pulls_url = []  # не смерженые пул-реквэсты url
        for n in no_merge_pulls['items']:
            no_merge_pulls_url.append(n['repository_url'])
        #print('No merge pulls- ', no_merge_pulls_url)

        repos_url = []  # Получение ссылок на репозитории
        for p in pulls['items']:
            repos_url.append(p['repository_url'])
        #print('Url_repositories-', repos_url)

        repos = []  # раскрытие репозиториев
        for i in pulls['items']:
            repo_json = requests.get(i['repository_url']).json()
            repos.append(repo_json)

        name_proj = []  # Название проектов
        for r in repos:
            name_proj.append(r['name'])
        #print('Projects- ', name_proj)

        stars_user = []  # Количество звезд проектов
        for stars in repos:
            stars_user.append(stars['stargazers_count'])
        #print('Stars- ', stars_user)

        html_url = []  # ссылка на проект на Гитхабе
        for html in repos:
            html_url.append(html['html_url'])
        #print('HTML- ', html_url)

        comments = []  # комментарии
        for comm in pulls['items']:
            comments.append(comm['comments'])
        #print('Comments- ', comments)

        context = {'repos_url': repos_url,
                   'repos': repos,
                   'name_proj': name_proj,
                   'stars_user': stars_user,
                   'html_url': html_url,
                   'comments': comments,
                   'no_merge_pulls_url': no_merge_pulls_url,
                   'pulls': pulls,
                   }

        return render(request, 'response_api.html', context)

    form = GitForm()
    return render(request, 'form_test.html', {'form': form})


