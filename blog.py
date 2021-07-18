from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt
from functools import wraps

#kullanıcı girişi decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
            if "logged_in" in session:
                return f(*args, **kwargs)
            else:
                flash("Bu sayfayı gormek için giriş yapın..","danger")
                return redirect(url_for("login"))    
    return decorated_function

app = Flask(__name__)
app.secret_key="tanerblog"

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "tanerblog"
app.config["MYSQL_CURSORCLASS"]= "DictCursor"

mysql = MySQL(app)

#kayıt formu
class RegisterForm(Form):
    name = StringField("Adınız",validators=[validators.Length(min=4,max=20),validators.DataRequired(message="İsminizi Girin")])
    username = StringField("Kullanıcı Adı",validators=[validators.Length(min=5,max=25),validators.DataRequired(message="Kullanıcı adınızı girin")])
    email = StringField("Email Adresi",validators=[validators.Length(min=12,max=48),validators.Email(message="Geçerli Email Adresi Girin")])
    password = PasswordField("Şifreniz",validators=[validators.DataRequired(message="Lütfen şifrenizi boş bırakmayın"),
        validators.EqualTo(fieldname="confirm",message="Şifreniz Uyuşmuyor..")
    ])
    confirm = PasswordField("Şifre Doğrula")

#kayıt olma işlemi
@app.route("/register",methods=["GET", "POST"])
def register():
    form = RegisterForm(request.form)
    
    if request.method=='POST' and form.validate():
        name = form.name.data
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt(form.password.data)

        cursor = mysql.connection.cursor() 
        
        sorgu ="Insert into users(name,email,username,password) VALUES(%s, %s, %s, %s)"
        cursor.execute(sorgu,(name,email,username,password))
        mysql.connection.commit()
        cursor.close()
        
        flash("Başarıyla Kayıt Oldunuz..","success")
        return redirect(url_for("login"))
    else:    
        return render_template("register.html",form=form)

#login formu
class LoginForm(Form):
    username = StringField("Kullanıcı Adı")
    password = PasswordField("Şifre")

#login işlemi
@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm(request.form)
    
    if request.method =="POST":
        username = form.username.data
        password_entered = form.password.data

        cursor = mysql.connection.cursor()
        sorgu = "Select * From users where username = %s"
        deger = cursor.execute(sorgu,(username,)) 
        
        if deger>0:
            data = cursor.fetchone()
            real_password = data["password"]
            if sha256_crypt.verify(password_entered,str(real_password)):
                app.logger.info('password match')
                flash("Giriş İşlemi Başarılı","success")

                session["logged_in"]=True
                session["username"]=username   

                return redirect(url_for("index"))
            else:
                flash("Yanlış şifre girdiniz!! ","dark")
                return redirect(url_for("login"))  
        else:
            flash("Böyle bir kullanıcı adı yok...!","danger")
            return redirect(url_for("login"))

    return render_template("login.html",form=form)

#logout işlemi
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


#index sayfasi
@app.route("/")
def index():
    return render_template("index.html")

#hakkımda sayafası
@app.route("/about")
def about():
    return render_template("hakkimda.html")

#kontrol paneli sayfasi
@app.route("/dasboard")
@login_required
def dasboard():
    cursor = mysql.connection.cursor()
    sorgu = "Select * From filmler where author = %s"
    deger = cursor.execute(sorgu,(session["username"],))

    if deger>0:
        filmler = cursor.fetchall()
        return render_template("dasboard.html",filmler=filmler)
    else:    
        return render_template("dasboard.html")



#yorum ekleme
@app.route("/comment",methods=["GET","POST"])
def addcomment(id):


    if request.method=="GET":
        return redirect(url_for("index"))
    else:
        comment_author = request.form.get("comment_author")

        comment_content = request.form.get("comment_content")
        
        cursor = mysql.connection.cursor()

        sorgu ="Insert into yorumlar (comment_author,comment_content) VALUES(%s,%s)"
        cursor.execute(sorgu,(comment_author,comment_content))
        
        mysql.connection.commit()
        cursor.close()

        flash("Oluşturduğun yorum eklendi..","success")
            
        return redirect(url_for("filmler"))

    return render_template("filmler.html",filmler=filmler,id=id)
    
    
###yorumlar sayfasi
@app.route("/comments")
def comment():
    
    cursor = mysql.connection.cursor()
    
    sorgu ="Select * from yorumlar"
    deger = cursor.execute(sorgu)

    if deger > 0:
        yorumlar = cursor.fetchall()
        return render_template("comments.html",comment=yorumlar)
    else :
        return render_template("comments.html") 

## yorumlar detay
@app.route("/comment/<string:id>")
def commentss(id):

    cursor = mysql.connection.cursor()
    
    sorgu ="Select * From yorumlar where id = %s"
    deger = cursor.execute(sorgu,(id,))
    
    if deger >0 :
        yorum = cursor.fetchone()
        return render_template("comment.html",yorum=yorum)
    else:    
        return render_template("comment.html")

#film form
class FilmForm(Form):
    title = StringField("Film Başlığı",validators=[validators.Length(min=3,max=85)])
    content = TextAreaField("Film İçerigi",validators=[validators.Length(min=10)])

#film ekleme
@app.route("/addfilm",methods=["GET","POST"])
def addfilm():
    form = FilmForm(request.form)
    
    if request.method=="POST" and form.validate():
        title = form.title.data
        content = form.content.data

        cursor = mysql.connection.cursor()

        sorgu ="Insert into filmler (title,author,content) VALUES(%s,%s,%s)"
        cursor.execute(sorgu,(title,session["username"],content))
        
        
        mysql.connection.commit()
        cursor.close()

        flash("Oluşturduğun film eklendi..","success")

        return redirect(url_for("dasboard"))

    return render_template("addfilm.html",form=form)

#filmler sayfası
@app.route("/filmler")
def filmler():
    cursor = mysql.connection.cursor()
    
    sorgu ="Select * From filmler"
    deger = cursor.execute(sorgu)

    
    if deger > 0:
        filmler = cursor.fetchall()
        return render_template("filmler.html",filmler=filmler)
    else :
        return render_template("filmler.html")     

#film detay sayfası
@app.route("/film/<string:id>")
def film(id):
    cursor = mysql.connection.cursor()
    
    sorgu ="Select * From filmler where id = %s"
    deger = cursor.execute(sorgu,(id,))
    
    if deger >0 :
        film = cursor.fetchone()
        return render_template("film.html",film=film)
    else:    
        return render_template("film.html")

#film silme
@app.route("/delete/<string:id>")
@login_required
def delete(id):
    cursor = mysql.connection.cursor()
    
    sorgu ="Select * from filmler where author = %s and id = %s"
    deger = cursor.execute(sorgu,(session["username"],id))

    if deger > 0:
        sorgu2="Delete from filmler where id = %s"
        cursor.execute(sorgu2,(id,))
        mysql.connection.commit()
        return redirect(url_for("dasboard"))
    else:
        flash("Bu filmi silme yetkiniz yoktur","warning") 
        return redirect(url_for("index"))

#film guncelleme
@app.route("/edit/<string:id>",methods=["GET","POST"])
@login_required
def guncelleme(id):

    if request.method=="GET":
        cursor = mysql.connection.cursor()
        
        sorgu = "Select * from filmler where id = %s and author = %s"
        sonuc = cursor.execute(sorgu,(id,session["username"]))

        if sonuc == 0:
            flash("Böyle bir film yok veya yetkiniz yok..!","danger")
            return redirect(url_for("index"))
        else:
            film = cursor.fetchone()
            
            form = FilmForm()
            form.title.data=film["title"]
            form.content.data=film["content"]
            return render_template("update.html",form=form)    
    else:
        #post request
        form = FilmForm(request.form)

        newtitle=form.title.data
        newcontent=form.content.data
        
        sorgu2="Update filmler Set title = %s, content = %s where id = %s"

        cursor=mysql.connection.cursor()
        cursor.execute(sorgu2,(newtitle,newcontent,id))
        mysql.connection.commit()

        flash("Film Güncellendi..","success")

        return redirect(url_for("dasboard"))

#film arama url 
@app.route("/search",methods=["GET","POST"])
def search():
    if request.method=="GET":
        return redirect(url_for("index"))
    else:
        keyword = request.form.get("keyword")

        cursor = mysql.connection.cursor()
        sorgu ="Select *from filmler where title like '%"+keyword+"%' "

        sonuc = cursor.execute(sorgu)

        if sonuc == 0:
            flash("Aranan kelimeye uygun film bulunmadı..","dark")
            return redirect(url_for("filmler"))
        else:
            filmler=cursor.fetchall()
            return render_template("filmler.html",filmler=filmler)

         

if __name__ == "__main__":
    app.run(debug=True)
    