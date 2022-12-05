import pyodide
from js import document, console


#proxy_function = lambda e: console.log('me diste click')
def proxy_btnAumentar(e):
    global suma
    console.log('click en Aumentar')
    span = document.getElementById('span')
    suma += 1
    span.textContent = suma
    

def proxy_btnDisminuir(e):
    global suma
    console.log('click en Disminuir')
    span = document.getElementById('span')
    suma -= 1
    span.textContent = suma
    

def proxy_container(e):
    # console.log(e.target)
    if e.target.classList.contains('btn-info'):
        proxy_btnAumentar(e)
    elif e.target.classList.contains('btn-danger'):
        proxy_btnDisminuir(e)
    e.stopPropagation()
    console.log('click en container')

def proxy_body(e):
    console.log('click en body')

def proxy_btnDark(e):
    console.log('click en btnDark')
    e.stopPropagation()

def proxy_bgSuccess(e):
    console.log('click en bgSuccess')
    e.stopPropagation()


def main():
    global suma
    suma = 0
    btnAumentar = document.querySelector('.btn-info')
    btnDisminuir = document.querySelector('.btn-danger')
    container = document.querySelector('.container')

    container.addEventListener('click', pyodide.create_proxy(proxy_container))
    # btnAumentar.addEventListener('click', pyodide.create_proxy(proxy_btnAumentar))
    # btnDisminuir.addEventListener('click', pyodide.create_proxy(proxy_btnDisminuir))

    # stop propagation
    btnDark = document.querySelector('.btn-dark')
    bgSuccess = document.querySelector('.bg-success')

    document.body.addEventListener('click', pyodide.create_proxy(proxy_body))
    
    btnDark.addEventListener('click', pyodide.create_proxy(proxy_btnDark))
    bgSuccess.addEventListener('click', pyodide.create_proxy(proxy_bgSuccess))
    
main()