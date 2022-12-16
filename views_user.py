from flask import render_template, request, redirect, session, flash, url_for
from jogoteca import app
from models import Usuarios
from helpers import FormularioUsuario
from flask_bcrypt import check_password_hash

@app.route('/login')
def login():
    """Rota do login"""
    proxima = request.args.get('proxima')
    form = FormularioUsuario()
    return render_template('login.html', proxima=proxima, form=form)


@app.route('/autenticar', methods=['POST',])
def autenticar():
    """Autentica dados do login"""
    form = FormularioUsuario(request.form)
    usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first()
    senha = check_password_hash(usuario.senha, form.senha.data)
    if usuario and senha:
        session['usuario_logado'] = usuario.nickname
        flash(usuario.nickname + ', você foi logado com sucesso!', )
        proxima_pagina = request.form['proxima']
        return redirect(proxima_pagina)
    else:
        flash('Falha ao efetuar login')
        return redirect(url_for('login'))


    """ SEM BCRYPT
    if usuario:
        if form.senha.data == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ', você foi logado com sucesso!', )
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Falha ao efetuar login')
        return redirect(url_for('login'))
    """

    """ SEM WTFORMS
    usuario = Usuarios.query.filter_by(nickname=request.form['usuario']).first()
    if usuario:
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ', você foi logado com sucesso!', )
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Falha ao efetuar login')
        return redirect(url_for('login'))
    """

@app.route('/logout')
def logout():
    """Efetua o logout do usuário"""
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso')
    return redirect(url_for('index'))