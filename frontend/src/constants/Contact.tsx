const Contact = () => {
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
        <h1 style={{ color: '#007bff', fontSize: '2rem', margin: '0' }}>تواصل معنا</h1>
        <p style={{ color: '#636e72', fontSize: '0.9rem' }}>نحن هنا لمساعدتك والاستماع إلى اقتراحاتك</p>
      </header>

      <section style={{ marginBottom: '30px' }}>
        <p>
          في <strong>أودا</strong>، نقدر تواصلك معنا ونسعى دائماً لتقديم أفضل تجربة ممكنة. سواء كنت لديك استفسار أو اقتراح أو تحتاج إلى مساعدة، فريقنا جاهز للرد عليك.
        </p>
      </section>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '30px', marginBottom: '40px' }}>
        
        <div style={{ backgroundColor: '#f8f9fa', padding: '25px', borderRadius: '8px', borderRight: '4px solid #007bff' }}>
          <h3 style={{ color: '#007bff', marginTop: '0', marginBottom: '15px' }}>📧 البريد الإلكتروني</h3>
          <p style={{ margin: '0 0 10px 0' }}>للتواصل العام والاستفسارات:</p>
          <p style={{ margin: '0', fontWeight: 'bold', fontSize: '1.1rem' }}>info@oda.com</p>
        </div>
      </div>

      <section style={{ marginBottom: '30px' }}>
        <h2 style={{ color: '#2d3436', fontSize: '1.4rem', marginBottom: '20px' }}>أقسام التواصل</h2>
        <div style={{ display: 'grid', gap: '20px' }}>
          <div style={{ padding: '20px', backgroundColor: '#fff', borderRadius: '8px', border: '1px solid #e9ecef' }}>
            <h3 style={{ color: '#007bff', marginTop: '0', marginBottom: '10px' }}>🎓 الدعم الفني</h3>
            <p style={{ margin: '0 0 10px 0' }}>للمساعدة في المشاكل التقنية والاستفسارات حول استخدام المنصة:</p>
            <p style={{ margin: '0', fontWeight: 'bold' }}>support@oda.com</p>
          </div>
          
          <div style={{ padding: '20px', backgroundColor: '#fff', borderRadius: '8px', border: '1px solid #e9ecef' }}>
            <h3 style={{ color: '#007bff', marginTop: '0', marginBottom: '10px' }}>🤝 الشراكات والتعاون</h3>
            <p style={{ margin: '0 0 10px 0' }}>للاستفسارات حول الشراكات والتعاون المؤسسي:</p>
            <p style={{ margin: '0', fontWeight: 'bold' }}>partners@oda.com</p>
          </div>
          
          <div style={{ padding: '20px', backgroundColor: '#fff', borderRadius: '8px', border: '1px solid #e9ecef' }}>
            <h3 style={{ color: '#007bff', marginTop: '0', marginBottom: '10px' }}>📰 الإعلام والصحافة</h3>
            <p style={{ margin: '0 0 10px 0' }}>للاستفسارات الإعلامية وطلبات المقابلات:</p>
            <p style={{ margin: '0', fontWeight: 'bold' }}>media@oda.com</p>
          </div>
        </div>
      </section>

      <section style={{ backgroundColor: '#f8f9fa', padding: '25px', borderRadius: '8px', borderRight: '5px solid #007bff' }}>
        <h2 style={{ marginTop: '0', fontSize: '1.2rem', color: '#007bff' }}>تابعنا على وسائل التواصل الاجتماعي</h2>
        <p style={{ marginBottom: '15px' }}>ابق على اطلاع بآخر الأخبار والتحديثات:</p>
        <div style={{ display: 'flex', gap: '15px', flexWrap: 'wrap' }}>
          <span style={{ backgroundColor: '#007bff', color: 'white', padding: '8px 16px', borderRadius: '20px', fontSize: '0.9rem' }}>X (تويتر)</span>
          <span style={{ backgroundColor: '#007bff', color: 'white', padding: '8px 16px', borderRadius: '20px', fontSize: '0.9rem' }}>فيسبوك</span>
          <span style={{ backgroundColor: '#007bff', color: 'white', padding: '8px 16px', borderRadius: '20px', fontSize: '0.9rem' }}>انستغرام</span>
          <span style={{ backgroundColor: '#007bff', color: 'white', padding: '8px 16px', borderRadius: '20px', fontSize: '0.9rem' }}>لينكدإن</span>
        </div>
      </section>

      <footer style={{ marginTop: '40px', textAlign: 'center', borderTop: '1px solid #eee', paddingTop: '20px', color: '#b2bec3' }}>
        <p>&copy; {new Date().getFullYear()} oda - أودا. جميع الحقوق محفوظة.</p>
      </footer>
    </div>
  );
};

export default Contact;
