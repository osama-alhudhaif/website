const Frivacy = () => {
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
        <h1 style={{ color: '#007bff', fontSize: '2rem', margin: '0' }}>سياسة الخصوصية</h1>
        <p style={{ color: '#636e72', fontSize: '0.9rem' }}>آخر تحديث: {new Date().toLocaleDateString('ar-SA')}</p>
      </header>

      <section>
        <p>
          مرحباً بك في <strong>موقع oda - أودا</strong>. نحن نولي خصوصيتك أهمية بالغة، وتوضح هذه الصفحة التزامنا بحماية بياناتك وكيفية التعامل معها.
        </p>
      </section>

      <div style={{ display: 'grid', gap: '25px', marginTop: '30px' }}>
        
        <section>
          <h2 style={{ color: '#2d3436', fontSize: '1.4rem' }}>1. جمع المعلومات</h2>
          <p>
            نحن لا نقوم بجمع بيانات تعريف شخصية (مثل الاسم أو العنوان) إلا إذا قمت بتزويدنا بها طواعية عبر نماذج التواصل أو التسجيل. ومع ذلك، قد نقوم بجمع معلومات تقنية غير شخصية مثل:
          </p>
          <ul style={{ paddingRight: '20px' }}>
            <li>نوع المتصفح ونظام التشغيل.</li>
            <li>العنوان المجهول للبروتوكول (IP Address).</li>
            <li>الصفحات التي تمت زيارتها ووقت البقاء فيها.</li>
          </ul>
        </section>

        <section>
          <h2 style={{ color: '#2d3436', fontSize: '1.4rem' }}>2. ملفات تعريف الارتباط والتخزين المحلي</h2>
          <p>
            نستخدم ملفات <strong>Cookies</strong> وتقنيات <strong>Local Storage</strong> لتحسين أداء الموقع، مثل حفظ تفضيلاتك أو الحفاظ على جلسة تسجيل الدخول الخاصة بك، مما يغنيك عن إدخال بياناتك في كل مرة.
          </p>
        </section>

        <section>
          <h2 style={{ color: '#2d3436', fontSize: '1.4rem' }}>3. حماية البيانات</h2>
          <p>
            نحن نطبق معايير أمنية صارمة لمنع الوصول غير المصرح به إلى بياناتك. يتم تشفير كافة البيانات المتبادلة بين جهازك وخوادمنا عبر بروتوكول <strong>HTTPS</strong> الآمن.
          </p>
        </section>

        <section>
          <h2 style={{ color: '#2d3436', fontSize: '1.4rem' }}>4. حقوق المستخدم</h2>
          <p>بموجب قوانين حماية البيانات، لديك الحق في:</p>
          <ul style={{ paddingRight: '20px' }}>
            <li>الوصول إلى بياناتك التي نملكها.</li>
            <li>طلب تصحيح أو حذف بياناتك من سجلاتنا.</li>
            <li>الاعتراض على معالجة بياناتك لأغراض تسويقية.</li>
          </ul>
        </section>

        <section>
          <h2 style={{ color: '#2d3436', fontSize: '1.4rem' }}>5. روابط الأطراف الثالثة</h2>
          <p>
            قد يحتوي موقعنا على روابط لمواقع أخرى (مثل X أو منصات التواصل). نحن لسنا مسؤولين عن ممارسات الخصوصية الخاصة بتلك المواقع، وننصحك بقراءة سياسة الخصوصية لكل موقع تزوره.
          </p>
        </section>

        <section style={{ backgroundColor: '#f8f9fa', padding: '20px', borderRadius: '8px', borderRight: '5px solid #007bff' }}>
          <h2 style={{ marginTop: '0', fontSize: '1.2rem' }}>تواصل معنا</h2>
          <p>لأي استفسار يتعلق بخصوصيتك، يمكنك مراسلتنا مباشرة عبر:</p>
          <p>📧 <strong>oda@oda.com</strong></p>
        </section>
      </div>

      <footer style={{ marginTop: '40px', textAlign: 'center', borderTop: '1px solid #eee', paddingTop: '20px', color: '#b2bec3' }}>
        <p>&copy; {new Date().getFullYear()} oda - أودا. جميع الحقوق محفوظة.</p>
      </footer>
    </div>
  );
};

export default Frivacy;