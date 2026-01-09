const About = () => {
    return (
        <div style={{ maxWidth: '850px', margin: '0 auto', padding: '40px 20px', lineHeight: '1.8', textAlign: 'right', direction: 'rtl', color: '#333' }}>
            
            {/* الهيدر والتعريف بالاسم */}
            <header style={{ textAlign: 'center', marginBottom: '60px' }}>
                <h1 style={{ fontSize: '3.5rem', color: '#2c3e50', marginBottom: '10px', letterSpacing: '2px' }}>Oda</h1>
                <h2 style={{ fontWeight: '600', color: '#3498db', marginBottom: '20px' }}>أودا.. ذكاءٌ في الاختيار، وطيٌّ للاختصار.</h2>
                <div style={{ maxWidth: '600px', margin: '0 auto', fontStyle: 'italic', color: '#7f8c8d', borderRight: '4px solid #3498db', paddingRight: '15px' }}>
                    <p>
                        بين جدران "Oda" تكتنف المعاني؛ فهي <strong>الغرفة</strong> التي يأوي إليها الخيال، 
                        وهي <strong>الأُود</strong> (القصيدة الغنائية) التي تشدو بها الشعوب، وهي <strong>الأثر</strong> الذي لا يمحوه الزمن. 
                        إنها غرفة الأديب حيث يُشيّد عوالمه، ومنطلق القارئ نحو آفاق لا تحدها لغة.
                    </p>
                </div>
            </header>

            {/* من نحن */}
            <section style={{ marginBottom: '40px' }}>
                <h3 style={{ borderBottom: '2px solid #3498db', display: 'inline-block', paddingBottom: '5px', color: '#2c3e50' }}>من نحن</h3>
                <p>
                    <strong>Oda</strong> هو مشروع شغوف وُلد من قلب المكتبات، يهدف لدمج عراقة الكتاب الورقي بذكاء العصر الرقمي. 
                    بإشراف ورؤية <strong>أديب</strong>، نبتكر أدوات تُعيد صياغة علاقتنا بالقراءة، 
                    مسخرين الذكاء الاصطناعي ليكون جسراً آمناً يعبر به القارئ نحو كنوز الأدب العالمي.
                </p>
            </section>

            {/* الرسالة والرؤية في صف واحد (اختياري) */}
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '30px', marginBottom: '40px' }}>
                <section>
                    <h3 style={{ borderBottom: '2px solid #3498db', display: 'inline-block', paddingBottom: '5px', color: '#2c3e50' }}>الرسالة</h3>
                    <p>تحطيم قيود اللغة أمام الفكر الإنساني، وتقريب المسافات بين الثقافات عبر ترجمة ذكية تحفظ للنص هيبته وللمعنى روحه.</p>
                </section>
                <section>
                    <h3 style={{ borderBottom: '2px solid #3498db', display: 'inline-block', paddingBottom: '5px', color: '#2c3e50' }}>الرؤية</h3>
                    <p>أن يستعيد الأدب العالمي لغته الكونية، بحيث يقرأ كل إنسان قصص الشعوب بلغة قلبه (لغته الأم) دون عناء.</p>
                </section>
            </div>

            {/* قيمنا */}
            <section style={{ marginBottom: '40px' }}>
                <h3 style={{ borderBottom: '2px solid #3498db', display: 'inline-block', paddingBottom: '5px', color: '#2c3e50' }}>قيمنا</h3>
                <ul style={{ listStyleType: 'none', padding: 0 }}>
                    <li style={{ marginBottom: '12px' }}><strong>• الشغف الأدبي:</strong> نحن لا نتعامل مع نصوص، بل مع أرواح سُكبت في كلمات.</li>
                    <li style={{ marginBottom: '12px' }}><strong>• الأمانة الرقمية:</strong> نُطوّر الذكاء الاصطناعي ليخدم النص، لا لِيُجمده أو يُفقده جوهره.</li>
                    <li style={{ marginBottom: '12px' }}><strong>• الجسر الثقافي:</strong> نؤمن أن المعرفة حق مشاع، واللغة لا يجب أن تكون عائقاً.</li>
                </ul>
            </section>

            {/* فلسفتنا (بلمسة إنسانية) */}
            <section style={{ backgroundColor: '#fdfcfb', padding: '25px', borderRadius: '15px', border: '1px solid #eee' }}>
                <h3 style={{ color: '#e67e22', marginBottom: '15px' }}>فلسفة أودا</h3>
                <p style={{ margin: 0 }}>
                    في أودا، نؤمن بأن <strong>الحب</strong> هو المحرك الأول؛ الحب للكلمة، وللتاريخ، وللإنسان. 
                    نحن لا نترجم لننقل المعلومات فحسب، بل نترجم لنمنحك الحق في أن تعيش ألف حياة في حياة واحدة، 
                    وأن تقرأ حكايات الصين، وأشعار البرازيل، وفلسفة اليونان بلسانك العربي المبين.
                </p>
            </section>

        </div>
    )
}

export default About;