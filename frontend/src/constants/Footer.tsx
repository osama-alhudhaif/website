const Footer = () => {
  return (
    <footer className="Footer">
      <div className="Footer-Content">
        {/* قسم معلومات مشروع عوالمنا */}
        <div className="Footer-Section">
          <h3 className="Footer-Title">عوالمنا</h3>
          <p>
            نبتكر في <strong>عالمنا</strong> لتطوير أجهزة 
            <strong> كتابنا </strong> و <strong> ورقنا </strong> 
            بذكاء <strong> أديب </strong>.
          </p>
        </div>

        {/* قسم روابط المساعدة */}
        <div className="Footer-Section">
          <h3 className="Footer-Title">المساعدة</h3>
          <ul className="Footer-Links">
            <li><a href="/about">من نحن</a></li>
            <li><a href="/contact">تواصل معنا</a></li>
            <li><a href="/privacy">سياسة الخصوصية</a></li>
          </ul>
        </div>

        {/* قسم التواصل السريع */}
        <div className="Footer-Section">
          <h3 className="Footer-Title">تواصل</h3>
          <p>awalimuna@awalimuna.com</p>
        </div>
      </div>

      <div className="Footer-Bottom">
        <p className="Rights">
          &copy; 2025 عوالمنا. جميع الحقوق محفوظة. تم التطوير بواسطة <strong>أديب</strong>.
        </p>
      </div>
    </footer>
  );
};

export default Footer;