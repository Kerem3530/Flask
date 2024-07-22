import random
from flask import Blueprint

views = Blueprint(__name__, "views")
havalıListe = ["Boşluksuzluk Boşlukluluktur", "1 + 1 = 11 Aksini İddia Eden Bilmem ne?", "Biliyor Muydun? Uzaylılar Uzaydan Gelmiştir.", "Hiç Komik Değil Ama Bu Şeyler Neyse...", "def İle Liste Oluşturulur <br>  - Ege", "Odak Modunda Çıkan Şeyler Beni Engelliyo Keşke Böyle Bi Özellik Olmasa..."]

havalıSayaç = 0

@views.route("/")
def home():
    global havalıSayaç
    havalıSayaç += 1
    return f"<h1>{random.choice(havalıListe)}</h1> <br><br><br> <a href='/havaliSayac'>Sayaç</a>"

@views.route("/havaliSayac")
def sayac():
    global havalıSayaç
    return f"<h1>{havalıSayaç}</h1> Kere Sayfayı Yeniledin ( önceki pencerede ) <br><br><br> <a href='/'>Önceki Sayfa</a>"
