from js import document
import json
from pyodide.http import pyfetch
from pyodide import create_proxy


async def make_request(url, method, body=None, headers=None):
    default_headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/json'
    }
    
    if headers:
        default_headers.update(headers)

    response = await pyfetch(
        url=url,
        method=method,
        body=body,
        headers=default_headers
    )

    return await response.json()


async def get_number_on_click(e):
    data = await make_request(url='/', method='GET')
    ul = document.getElementById('left')
    # ul = document.querySelector('#left')
    li = document.createElement('li')
    li.innerHTML = data['number']

    li.addEventListener('click', create_proxy(send_number_on_click))

    ul.appendChild(li)


async def send_number_on_click(e):
    number = e.target.innerHTML

    csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value
    body = json.dumps({'number': number})
    headers = {'X-CSRFToken': csrf}

    data = await make_request(url='/', method='POST', body=body, headers=headers)

    ul = document.getElementById('right')
    li = document.createElement('li')
    li.innerHTML = data['data']

    ul.appendChild(li)


def main():
    button = document.getElementById('button')
    button.addEventListener("click", create_proxy(get_number_on_click))

main()