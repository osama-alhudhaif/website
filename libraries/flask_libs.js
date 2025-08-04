// js_libs.js

// تهيئة i18next
i18next.init({
  lng: 'en', // أو dynamical حسب اللغة
  resources: {
    en: { translation: { "key": "Hello World" } },
    ar: { translation: { "key": "مرحبا بالعالم" } }
  }
});

// تهيئة AOS (إذا مشترك)
AOS.init();

// تهيئة Plyr (صوت تغيير الصفحة)
const player = new Plyr('#player', {
  // خيارات
});
