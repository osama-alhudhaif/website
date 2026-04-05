const Terms = () => {
  return (
    <div 
      dir="rtl" 
      style={{ 
        maxWidth: '850px', 
        margin: '40px auto', 
        padding: '40px', 
        fontFamily: "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
        lineHeight: '1.8',
        color: '#2d3436',
        backgroundColor: '#fff',
        borderRadius: '12px',
        boxShadow: '0 4px 15px rgba(0,0,0,0.05)',
        textAlign: 'right'
      }}
    >
      <header style={{ borderBottom: '3px solid #007bff', marginBottom: '30px', paddingBottom: '10px' }}>
        <h1 style={{ color: '#007bff', fontSize: '2rem', margin: '0' }}>شروط الاستخدام</h1>
        <p style={{ color: '#636e72', fontSize: '0.9rem' }}>آخر تحديث: {new Date().toLocaleDateString('ar-SA')}</p>
      </header>

      <section>
        <p>
          مرحباً بك في <strong>موقع oda - أودا</strong>. باستخدامك لموقعنا، فإنك توافق على الالتزام بالشروط والأحكام الموضحة أدناه.
        </p>
      </section>

      <div style={{ display: 'grid', gap: '25px', marginTop: '30px' }}>
        
        <section>
          <h2 style={{ color: '#2d3436', fontSize: '1.4rem' }}>1. قبول الشروط</h2>
          <p>
            باستخدامك لموقع أودا، فإنك تقر بأنك قرأت وفهمت وقبلت هذه الشروط والأحكام. إذا كنت لا توافق على هذه الشروط، يرجى عدم استخدام موقعنا.
          </p>
        </section>

        <section>
          <h2 style={{ color: '#2d3436', fontSize: '1.4rem' }}>2. استخدام الموقع</h2>
          <p>
            يمنع استخدام موقع أودا لأي أغراض غير قانونية أو مخالفة للقوانين المحلية والدولية. يتعهد المستخدم بعدم:
          </p>
          <ul style={{ paddingRight: '20px' }}>
            <li>نشر محتوى مسيء أو عنصري أو مخالف للآداب العامة.</li>
            <li>محاولة الوصول غير المصرح به إلى أنظمة الموقع.</li>
            <li>استخدام الموقع لأغراض تجارية دون الحصول على موافقة كتابية منا.</li>
            <li>انتهاك حقوق الملكية الفكرية أو حقوق النشر.</li>
          </ul>
        </section>

        <section>
          <h2 style={{ color: '#2d3436', fontSize: '1.4rem' }}>3. الملكية الفكرية</h2>
          <p>
            جميع المحتويات المنشورة على موقع أودا، بما في ذلك النصوص والصور والشعارات والبرمجيات، هي ملكية محمية بموجب قوانين حقوق النشر والعلامات التجارية. يمنع نسخ أو توزيع أو استخدام أي محتوى دون الحصول على موافقة كتابية مسبقة.
            <br />
            <strong>مع العلم ان كل النسخ الاصلية هي ملكية خاصة بالكاتب فقط وفقط النسخ المترجمة هي ملكية أودا.</strong>
          </p>
        </section>

        <section>
          <h2 style={{ color: '#2d3436', fontSize: '1.4rem' }}>4. الخصوصية</h2>
          <p>
            نحن نلتزم بحماية خصوصيتك وبياناتك الشخصية. للمزيد من المعلومات، يرجى مراجعة <a href="/Privacy" style={{ color: '#007bff', textDecoration: 'underline' }}>سياسة الخصوصية</a> الخاصة بنا.
          </p>
        </section>

        <section>
          <h2 style={{ color: '#2d3436', fontSize: '1.4rem' }}>5. مسؤولية المستخدم</h2>
          <p>
            أنت مسؤول عن جميع الأنشطة التي تقوم بها من خلال حسابك على موقعنا. يتعين عليك الحفاظ على سرية معلومات تسجيل الدخول وإبلاغنا فوراً في حال وجود أي استخدام غير مصرح به.
          </p>
        </section>

        <section>
          <h2 style={{ color: '#2d3436', fontSize: '1.4rem' }}>6. تحديد المسؤولية</h2>
          <p>
            لا نتحمل مسؤولية أي أضرار مباشرة أو غير مباشرة تنشأ عن استخدامك للموقع أو عدم قدرتك على استخدامه. نعمل بجد لضمان دقة المحتوى، لكننا لا نضمن خلو الموقع من الأخطاء.
          </p>
        </section>

        <section>
          <h2 style={{ color: '#2d3436', fontSize: '1.4rem' }}>7. تعديل الشروط</h2>
          <p>
            نحتفظ بالحق في تعديل هذه الشروط والأحكام في أي وقت. سيتم نشر أي تغييرات على هذه الصفحة، ويعتبر استخدامك المستمر للموقع موافقة على الشروط المعدلة.
          </p>
        </section>

        <section style={{ backgroundColor: '#f8f9fa', padding: '20px', borderRadius: '8px', borderRight: '5px solid #007bff' }}>
          <h2 style={{ marginTop: '0', fontSize: '1.2rem' }}>تواصل معنا</h2>
          <p>لأي استفسار حول شروط الاستخدام، يمكنك مراسلتنا مباشرة عبر:</p>
          <p>📧 <strong>oda@oda.com</strong></p>
        </section>
      </div>

      <footer style={{ marginTop: '40px', textAlign: 'center', borderTop: '1px solid #eee', paddingTop: '20px', color: '#b2bec3' }}>
        <p>&copy; {new Date().getFullYear()} oda - أودا. جميع الحقوق محفوظة.</p>
      </footer>
    </div>
  );
};

export default Terms;
