REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 1
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Online Course Platform",
    "DESCRIPTION": """\
### **Online Course Platform**  
Bu **o‘qituvchilar** va **o‘quvchilar** uchun mo‘ljallangan **raqamli ta’lim platformasi**.  

- 📚 O‘qituvchilar kurslar yaratib, video va materiallarni yuklaydi.  
- 🎓 O‘quvchilar esa kurslarni sotib olib o‘rganishi mumkin.  
- 🔗 **Django Rest Framework (DRF)** asosida ishlab chiqilgan.  
- 🌍 Frontend yoki mobil ilovalar bilan **integratsiya qilish** mumkin.
""",
    "VERSION": "1.0.0",
}
