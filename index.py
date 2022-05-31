
from flask import Flask, redirect, render_template, request, url_for

app = Flask('__name__',template_folder='paginas')

listaDeUsuarios = []
listaDeUsuariosTiendas = []

@app.route('/')
def login():
    '''
        Renderiza la pantalla del login

        parametros:
            ninguno
        returns:
            render_template('login.html')
    
    '''

    return render_template('login.html')

@app.route('/login', methods=['POST','GET'])
def validacion():
    '''
        Valida el usuario y contrasenia

        parametros:
            ninguno
        returns:
            case True: render_template('principal.html')
            case False: render_template('login.html')
    
    '''

    if(request.method == 'POST'):
        usuario = request.form['usuario']
        contrasenia = request.form['contrasenia']
        if(usuario == 'prueba' and contrasenia == 'admin'):
            return redirect(url_for('principal'))
        else:
            return render_template('login.html')

@app.route('/principal')
def principal():
    return render_template('principal.html',listaUsuarios = listaDeUsuariosTiendas)



@app.route('/ingresar', methods=['POST','GET'])
def ingresar():
    '''
        Permite el ingreso de usuarios y tiendas a la lista

        parametros:
            ninguno
        returns:
            redirect página principal

    '''

    if(request.method == 'post'):
        usuario = request.form['usuario']
        tienda = request.form['tienda']
        estado = request.form['estado']
        listaDeUsuariosTiendas.append({'usuario': usuario , 'tienda': tienda, 'estado': estado})
        print(listaDeUsuariosTiendas)
    return redirect(url_for('principal'))
    
    

if __name__ == '__main__':
    app.run(debug=True)
