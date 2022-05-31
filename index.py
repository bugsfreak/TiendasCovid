
from flask import Flask, render_template, request, url_for

app = Flask('__name__',template_folder='paginas')


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
def principal():
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
            return render_template('principal.html')
        else:
            return render_template('login.html')

    
    

if __name__ == '__main__':
    app.run(debug=True)
