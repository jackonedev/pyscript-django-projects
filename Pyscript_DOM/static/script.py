# import json
from js import document, console

# from pyodide.http import pyfetch
# from pyodide import create_proxy



# pyscript application: es el punto 2.3 automatizado
def append_li(parentQueryStr, templateQueryStr, itemQueryStr, array, log=False):

    lista = document.querySelector(parentQueryStr)
    template = document.querySelector(templateQueryStr).content
    fragment = document.createDocumentFragment()
    if log: 
        console.log(lista); console.log(template); console.log(fragment)

    for item in array:
        template.querySelector(itemQueryStr).textContent = item
        clone = template.cloneNode(True)    
        fragment.appendChild(clone)

    lista.appendChild(fragment)


def main():

    arrayLista = ['item 1', 'item 2', 'item 3']
    parentQueryStr = '#lista'
    templateQueryStr = '#template-lista'
    itemQueryStr = '.list span'
    append_li(parentQueryStr, templateQueryStr, itemQueryStr, arrayLista, log=True)


main()


# 2.3) Utilizando <template>
# lista = document.querySelector('#lista')
# arrayLista = ['item 1', 'item 2', 'item 3']


# template = document.querySelector('#template-li').content
# fragment = document.createDocumentFragment()
# console.log(lista); console.log(template); console.log(fragment)

# for item in arrayLista:
#     template.querySelector('.list span').textContent = item
#     clone = template.cloneNode(True)    
#     fragment.appendChild(clone)

# lista.appendChild(fragment)


#2.2) es mas legible
# lista = document.querySelector('#lista')

# fragment = ''
# for item in arrayLista:
#     fragment += \
#         '<li class="list">'\
#             f'<b>Nombre: </b> <span class="text-danger">{item}</span>'\
#         '</li>'

# lista.innerHTML = fragment




# 2.1) es una opción muy potable por velocidad
# <li class="list">
#     <b>Nombre: </b> <span class="text-danger">descripción...</span>
# </li>

# lista = document.querySelector('#lista')
# fragment = document.createDocumentFragment()
# for item in arrayLista:
#     li = document.crateElement('li')
#     li.classList.add('list')
    
#     b = document.createElement('b')
#     b.textContent = 'Nombre: '
#     li.appendChild(b)

#     span = document.createElement('span')
#     span.classList.add("text-danger")
#     span.textContent = item
#     li.appendChild(span)

#     fragment.appendChild(li)

# lista.appendChild(fragment)