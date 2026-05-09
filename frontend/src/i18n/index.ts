import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import LanguageDetector from 'i18next-browser-languagedetector';
import ar from './ar.json';
import en from './en.json';
import fr from './fr.json';
import de from './de.json';
import es from './es.json';
import tr from './tr.json';
import zh from './zh.json';
import ru from './ru.json';
import ja from './ja.json';
import pt from './pt.json';
import it from './it.json';
import ko from './ko.json';
import nl from './nl.json';
import pl from './pl.json';
import uk from './uk.json';
import id from './id.json';
import hi from './hi.json';

i18n
  .use(LanguageDetector)
  .use(initReactI18next)
  .init({
    resources: {
      ar: { translation: ar },
      en: { translation: en },
      fr: { translation: fr },
      de: { translation: de },
      es: { translation: es },
      tr: { translation: tr },
      zh: { translation: zh },
      ru: { translation: ru },
      ja: { translation: ja },
      pt: { translation: pt },
      it: { translation: it },
      ko: { translation: ko },
      nl: { translation: nl },
      pl: { translation: pl },
      uk: { translation: uk },
      id: { translation: id },
      hi: { translation: hi },
    },
    // اكتشاف لغة المتصفح تلقائياً، مع الرجوع للعربية كافتراضي
    fallbackLng: 'ar',
    supportedLngs: ['ar', 'en', 'fr', 'de', 'es', 'tr', 'zh', 'ru', 'ja', 'pt', 'it', 'ko', 'nl', 'pl', 'uk', 'id', 'hi'],
    detection: {
      order: ['localStorage', 'navigator'],
      caches: ['localStorage'],
      lookupLocalStorage: 'oda_language',
    },
    interpolation: {
      escapeValue: false,
    },
  });

export default i18n;
