from django.db import models

# Create your models here.
class User(models.Model):
    userName = models.CharField(max_length=255)
    userNo = models.CharField(max_length=255)
class Cevaplar(models.Model):
    user_id = models.CharField(max_length=255)
    sinif = models.CharField(max_length=255)
    ortalama =models.CharField(max_length=255)
    katilim_derecesi =models.CharField(max_length=255)
    hitap_eden=models.CharField(max_length=255)
    hakim_misin=models.CharField(max_length=255)
    dusunur_musun=models.CharField(max_length=255)
    ing_duzey=models.CharField(max_length=255)




model_soru_secenek =[{
        "soru_metin": "Sınıfınız?",
        "secenek_metin": ["1.Sınıf", "2.Sınıf", "3.sınıf", "4.Sınıf"],
        "cevap":""
    },
    {
        "soru_metin": "Genel akademik ortalamanız?",
        "secenek_metin": ["2-2,5","2,5-3","3-3,5","3,5-4"],
        "cevap":""
    },
    {
        "soru_metin": "Veri biliminin temelleri dersine katılımınızı derecelendirir misiniz?(1'den 5'e kadar)",
        "secenek_metin": ["1","2","3","4","5"],
        "cevap":""
    },
    {
        "soru_metin": "Veri madenciliğinde kullanılan dillerden hangisi size daha çok hitap ediyor?",
        "secenek_metin": ["R dili","Python Dili","Java dili","MatLab dili","SAS dili"],
        "cevap":""
    },
    {
        "soru_metin": "Veri biliminin temelleri dersinde yararlanılan Python diline hakim misiniz?",
        "secenek_metin": ["Evet","Kısmen","Hayır"],
        "cevap":""
    },
    {
        "soru_metin": "Gelecekte veri madenciliği alanında çalışmayı düşünür müsünüz?",
        "secenek_metin":["Evet","Hayır"],
        "cevap":""
    },
    {
        "soru_metin": "İngilizce düzeyiniz nedir?",
        "secenek_metin": ["A1","A2","B1","B2","C1","C2"],
        "cevap":""
    }]