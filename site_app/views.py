from http.client import HTTPResponse

from django.shortcuts import render


def main_view(request) -> HTTPResponse:
    if request.method == 'GET':

        return render(request, 'site_app/index.html')


def test_url(request) -> HTTPResponse:
    if request.method == 'GET':

        return render(request, 'site_app/index.html')

