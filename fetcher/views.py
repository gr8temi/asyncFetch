import requests
import asyncio
from django.http import JsonResponse


async def fetch_quote():
    response = requests.get("https://quotable.io/quotes?page=1")
    if response.status_code == 200:
        return response.json()
    return {}


async def fetch_user():
    response = requests.get("https://randomuser.me/api/")
    if response.status_code == 200:
        return response.json()
    return {}


def index(request):
    quotes = asyncio.run(fetch_quote())
    user = asyncio.run(fetch_user())

    return JsonResponse({"quotes": quotes, "user": user})
