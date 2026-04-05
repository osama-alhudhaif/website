const Partners = () => {
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
        <h1 style={{ color: '#007bff', fontSize: '2rem', margin: '0' }}>الشراكات</h1>
        <p style={{ color: '#636e72', fontSize: '0.9rem' }}>آخر تحديث: {new Date().toLocaleDateString('ar-SA')}</p>
      </header>

      <section>
        <p>
          في <strong>أودا</strong>، نؤمن بقوة التعاون والشراكات الاستراتيجية لتحقيق أهدافنا المشتركة في نشر المعرفة وتطوير عالم القراءة الرقمي.
        </p>
      </section>

      <div style={{ display: 'grid', gap: '25px', marginTop: '30px' }}>
        
        <section>
          <h2 style={{ color: '#2d3436', fontSize: '1.4rem' }}>رؤيتنا للشراكة</h2>
          <p>
            نسعى لبناء جسور تعاون مع المؤسسات والجهات التي تشاركنا نفس الشغف بالأدب والمعرفة. نؤمن أن الشراكات الناجحة تقوم على أساس الاحترام المتبادل والمنفعة المشتركة.
          </p>
        </section>

        <section>
          <h2 style={{ color: '#2d3436', fontSize: '1.4rem' }}>مجالات الشراكة</h2>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: '20px', marginTop: '20px' }}>
            <div style={{ backgroundColor: '#f8f9fa', padding: '20px', borderRadius: '8px', borderRight: '4px solid #007bff' }}>
              <h3 style={{ color: '#007bff', marginTop: '0' }}>📚 الناشرون</h3>
              <p>نرحب بالشراكة مع دور النشر لتوفير محتوى عالي الجودة ومنصات توزيع مبتكرة.</p>
            </div>
            <div style={{ backgroundColor: '#f8f9fa', padding: '20px', borderRadius: '8px', borderRight: '4px solid #007bff' }}>
              <h3 style={{ color: '#007bff', marginTop: '0' }}>🎓 المؤسسات التعليمية</h3>
              <p>نتعاون مع الجامعات والمدارس لتوفير حلول قراءة ذكية وتعليمية متقدمة.</p>
            </div>
            <div style={{ backgroundColor: '#f8f9fa', padding: '20px', borderRadius: '8px', borderRight: '4px solid #007bff' }}>
              <h3 style={{ color: '#007bff', marginTop: '0' }}>🏛️ المكتبات</h3>
              <p>ندعم المكتبات العامة والخاصة في التحول الرقمي وتوسيع قاعدة قرائها.</p>
            </div>
            <div style={{ backgroundColor: '#f8f9fa', padding: '20px', borderRadius: '8px', borderRight: '4px solid #007bff' }}>
              <h3 style={{ color: '#007bff', marginTop: '0' }}>💡 التقنيون</h3>
              <p>نفتح أبوابنا للشركات التقنية لتطوير حلول مبتكرة في مجال القراءة الذكية.</p>
            </div>
          </div>
        </section>

        <section>
          <h2 style={{ color: '#2d3436', fontSize: '1.4rem' }}>شركاؤنا الحاليون</h2>
          <p>
            نفخر بوجود شراكات استراتيجية مع عدد من المؤسسات الرائدة في مجال النشر والتعليم والتقنية. هذه الشراكات تساعدنا على تقديم خدمات أفضل لمستخدمينا وتوسيع نطاق تأثيرنا.
          </p>
        </section>

        <section>
          <h2 style={{ color: '#2d3436', fontSize: '1.4rem' }}>فوائد الشراكة مع أودا</h2>
          <ul style={{ paddingRight: '20px' }}>
            <li><strong>الوصول لجمهور واسع:</strong> الاستفادة من قاعدة مستخدمينا المتنامية في العالم العربي.</li>
            <li><strong>تقنيات متقدمة:</strong> الوصول إلى منصتنا التقنية وذكائنا الاصطناعي المبتكر.</li>
            <li><strong>دعم تسويقي:</strong> الترويج المتبادل للمنتجات والخدمات.</li>
            <li><strong>تحليلات وبيانات:</strong> الحصول على رؤى قيمة حول سلوك القراء والاتجاهات السوقية.</li>
            <li><strong>تطوير مشترك:</strong> فرص لتطوير منتجات وخدمات مبتكرة معاً.</li>
          </ul>
        </section>

        <section>
          <h2 style={{ color: '#2d3436', fontSize: '1.4rem' }}>كيف نبدأ الشراكة؟</h2>
          <p>
            إذا كنت مهتماً بالشراكة مع أودا، نرجو منك تزويدنا بالمعلومات التالية:
          </p>
          <ul style={{ paddingRight: '20px' }}>
            <li>معلومات عن مؤسستك ومجال عملها.</li>
            <li>نوع الشراكة المقترحة والأهداف المرجوة.</li>
            <li>الجمهور المستهدف وكيف يمكننا خدمته معاً.</li>
            <li>أي أفكار أو مقترحات إضافية للتعاون.</li>
          </ul>
        </section>

        <section style={{ backgroundColor: '#e8f4fd', padding: '25px', borderRadius: '8px', borderRight: '5px solid #007bff' }}>
          <h2 style={{ marginTop: '0', fontSize: '1.2rem', color: '#007bff' }}>انضم إلى عائلة أودا</h2>
          <p>
            نحن دائماً نبحث عن شركاء جدد يشاركوننا نفس الشغف بالقراءة والابتكار. دعنا نعمل معاً لإحداث فرق حقيقي في عالم القراءة الرقمي.
          </p>
        </section>

        <section style={{ backgroundColor: '#f8f9fa', padding: '20px', borderRadius: '8px', borderRight: '5px solid #007bff' }}>
          <h2 style={{ marginTop: '0', fontSize: '1.2rem' }}>تواصل معنا</h2>
          <p>لمناقشة فرص الشراكة، يرجى مراسلتنا مباشرة عبر:</p>
          <p>📧 <strong>partners@oda.com</strong></p>
          <p>🌐 <strong><a href="https://oda.story" style={{ color: '#007bff', textDecoration: 'underline' }}>oda.story</a></strong></p>
        </section>
      </div>

      <footer style={{ marginTop: '40px', textAlign: 'center', borderTop: '1px solid #eee', paddingTop: '20px', color: '#b2bec3' }}>
        <p>&copy; {new Date().getFullYear()} oda - أودا. جميع الحقوق محفوظة.</p>
      </footer>
    </div>
  );
};

export default Partners;
