import pywhatkit as kit
try:
    pywhatkit.sendwhatmsg("+905323991703","Bu bir deneme mesajıdır.",18,41)
    print("Gönderme başarılı.")
except:
    print("Beklenmeyen bir hata oluştu")
