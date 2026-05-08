// اللغات التي تكتب من اليمين إلى اليسار
const RTL = new Set([
  'ar', // عربي
  'he', // عبري
  'fa', // فارسي
  'ur', // أردو
  'ps', // بشتو
  'sd', // سندي
  'ug', // أويغوري
  'yi', // يديشية
  'dv', // ديفهي
  'ks', // كشميري
  'ku', // كردي (بعض اللهجات)
  'arc', // آرامية
  'ckb', // كردي سوراني
]);

export function isRTL(lang: string): boolean {
  const code = lang.split('-')[0].toLowerCase();
  return RTL.has(code);
}

export function getDir(lang: string): 'rtl' | 'ltr' {
  return isRTL(lang) ? 'rtl' : 'ltr';
}
