import requests
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

SUPPORTED_LANGUAGES = {
    'ar': 'العربية',
    'en': 'الإنجليزية',
    'fr': 'الفرنسية',
    'de': 'الألمانية',
    'es': 'الإسبانية',
    'it': 'الإيطالية',
    'pt': 'البرتغالية',
    'ru': 'الروسية',
    'zh': 'الصينية',
    'ja': 'اليابانية',
    'ko': 'الكورية',
    'tr': 'التركية',
    'fa': 'الفارسية',
    'ur': 'الأردية',
    'hi': 'الهندية',
}


class TranslateTextAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        text = request.data.get('text', '').strip()
        source_lang = request.data.get('source_lang', 'ar')
        target_lang = request.data.get('target_lang', 'en')

        if not text:
            return Response({'error': 'يرجى إدخال النص المراد ترجمته'}, status=status.HTTP_400_BAD_REQUEST)

        if len(text) > 5000:
            return Response({'error': 'النص طويل جداً (الحد الأقصى 5000 حرف)'}, status=status.HTTP_400_BAD_REQUEST)

        if source_lang == target_lang:
            return Response({'translated_text': text, 'source_lang': source_lang, 'target_lang': target_lang})

        try:
            actual_source = 'ar' if source_lang == 'auto' else source_lang
            response = requests.get(
                'https://api.mymemory.translated.net/get',
                params={
                    'q': text,
                    'langpair': f"{actual_source}|{target_lang}",
                    'de': getattr(settings, 'ODA_SUPPORT_EMAIL', 'support@oda.com'),
                },
                timeout=10,
            )
            data = response.json()

            if data.get('responseStatus') == 200:
                return Response({
                    'translated_text': data['responseData']['translatedText'],
                    'source_lang': actual_source,
                    'target_lang': target_lang,
                })
            return Response(
                {'error': 'فشلت الترجمة، حاول مرة أخرى'},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )
        except requests.RequestException:
            return Response(
                {'error': 'خدمة الترجمة غير متاحة حالياً'},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )


class SupportedLanguagesAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response(SUPPORTED_LANGUAGES)
