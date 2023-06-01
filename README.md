Flask Blog Uygulaması
Bu, Flask ile geliştirilmiş bir blog uygulamasıdır. Uygulama, kullanıcıların kayıt olmasını, giriş yapmasını, blog yazıları eklemesini, güncellemesini ve silmesini sağlar. Ayrıca kullanıcılar arama yapabilir ve diğer blog yazılarını görüntüleyebilir.

Kurulum
Flask yüklü değilse, Flask'ı yükleyin:
Copy code
pip install Flask
Flask-MySQLdb yüklü değilse, Flask-MySQLdb'yi yükleyin:
Copy code
pip install flask-mysqldb
Passlib yüklü değilse, Passlib'ı yükleyin:
Copy code
pip install passlib
Uygulamayı Başlatma
Flask blog uygulamasını çalıştırmak için terminalde uygulamanın bulunduğu dizine gidin.

Aşağıdaki komutu çalıştırarak uygulamayı başlatın:

Copy code
python app.py
Tarayıcınızda http://localhost:5000 adresine giderek blog uygulamasını kullanabilirsiniz.
Kullanıcı Kaydı
Kullanıcı kaydı yapmak için http://localhost:5000/register adresine gidin.
Ad, kullanıcı adı, e-posta ve şifre bilgilerini girin.
"Kayıt Ol" düğmesine tıklayarak kaydı tamamlayın.
Kullanıcı Girişi
Kullanıcı girişi yapmak için http://localhost:5000/login adresine gidin.
Kullanıcı adı ve şifre bilgilerinizi girin.
"Giriş Yap" düğmesine tıklayarak girişi tamamlayın.
Blog Yazısı Ekleme
Giriş yaptıktan sonra http://localhost:5000/addfilm adresine gidin.
Film başlığı ve içeriğini girin.
"Film Ekle" düğmesine tıklayarak blog yazısını ekleyin.
Blog Yazısı Güncelleme
Giriş yaptıktan sonra kendi blog yazılarınızı http://localhost:5000/dashboard adresinden görüntüleyebilirsiniz.
İstediğiniz blog yazısını düzenlemek için "Düzenle" düğmesine tıklayın.
Film başlığı ve içeriğini güncelleyin.
"Güncelle" düğmesine tıklayarak değişiklikleri kaydedin.
Blog Yazısı Silme
Giriş yaptıktan sonra kendi blog yazılarınızı http://localhost:5000/dashboard adresinden görüntüleyebilirsiniz.
Silmek istediğiniz blog yazısının yanındaki "Sil" düğmesine tıklayın.
Blog yazısı silinecektir.
Blog Yazısı Arama
Ana sayfada (http://localhost:5000) sağ üst köşede bir arama çubuğu bulunur.
Aramak istediğiniz kelimeyi girin ve "Ara" düğmesine tıklayın.
Arama sonuçları gösterilecektir.
Çıkış Yapma
Çıkış yapmak için http://localhost:5000/logout adresine gidin.
Bu yönergelerle Flask blog uygulamasını başlatabilir ve kullanabilirsiniz.
