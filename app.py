from flask import Flask, make_response, render_template, request, redirect
import mysql.connector





mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        password='suas enha',
        database='formulario'

    )

app = Flask(__name__)
app.config['SECRET_KEY'] = 'CINCITY09'
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route('/dados', methods=['GET'])
def get_dados():
 
    mycursor=mydb.cursor()
    mycursor.execute("SELECT * FROM formulario.logins")
    meus_dados=mycursor.fetchall()

    dados=[]
    for dado in meus_dados:
        dados.append(
        {
        'id':dado[0],
        'plataforma':dado[1],
        'login':dado[2],
        'senha':dado[3]
        
  }
 )


    return make_response(
        render_template('registros.html', dados=dados))



@app.route('/')
def home():
    return render_template('entrada_registros.html')

@app.route("/entrada", methods=['POST', 'GET'])
def inserir():

    
    plataforma = request.form.get('plataforma')
    login = request.form.get('login')
    senha = request.form.get('senha')
    
    
    mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        password='Cincity09!',
        database='formulario'

    )
    if mydb.is_connected():
        mycursor=mydb.cursor()

        
    mycursor.execute(f"insert into logins values(default, '{plataforma}', '{login}', '{senha}')")
    mydb.commit()

   

    
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete():
    cursor = mydb.cursor()
    id = request.form['id']
    cursor.execute("DELETE FROM logins WHERE id=%s", (id,))
    mydb.commit()
    return redirect('/dados')

   

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
