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

OLLAMA_URL = 'http://192.168.1.5:11434/api/generate'
OLLAMA_MODEL = 'qwen2.5-coder:32b'


def _translate_with_ollama(text, source_lang, target_lang):
    source_name = SUPPORTED_LANGUAGES.get(source_lang, source_lang)
    target_name = SUPPORTED_LANGUAGES.get(target_lang, target_lang)
    prompt = (
        f"You are a literary translator. Translate the following text from {source_name} to {target_name}. "
        f"Preserve the literary style, tone, and artistic nuance. Return ONLY the translated text, no explanations.\n\n"
        f"Text:\n{text}"
    )
    response = requests.post(
        OLLAMA_URL,
        json={'model': OLLAMA_MODEL, 'prompt': prompt, 'stream': False},
        timeout=60,
    )
    response.raise_for_status()
    return response.json()['response'].strip()


def _translate_with_mymemory(text, source_lang, target_lang):
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
        return data['responseData']['translatedText']
    raise ValueError('MyMemory translation failed')


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

        actual_source = 'ar' if source_lang == 'auto' else source_lang

        try:
            translated = _translate_with_ollama(text, actual_source, target_lang)
            return Response({
                'translated_text': translated,
                'source_lang': actual_source,
                'target_lang': target_lang,
            })
        except requests.ConnectionError:
            pass
        except Exception:
            pass

        try:
            translated = _translate_with_mymemory(text, actual_source, target_lang)
            return Response({
                'translated_text': translated,
                'source_lang': actual_source,
                'target_lang': target_lang,
            })
        except Exception:
            return Response(
                {'error': 'خدمة الترجمة غير متاحة حالياً'},
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )


class SupportedLanguagesAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response(SUPPORTED_LANGUAGES)
