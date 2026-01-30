import "./Footer.css";

const Footer = () => {
  return (
    <footer className="Footer">
      <div className="Footer-Content">
        
        {/* قسم معلومات مشروع Oda */}
        <div className="Footer-Section">
          <h3 className="Footer-Title">Oda</h3>
          <p className="Footer-Description">
            نبتكر في <strong>Oda</strong> لتطوير أجهزة 
            <span className="product-name"> كتابنا</span> و 
            <span className="product-name"> ورقنا</span> 
            بذكاء المدرب الرقمي <strong>أديب</strong>.
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
        
        <div className="Footer-Bottom">
          <p className="Rights">
            &copy; {new Date().getFullYear()} <strong>Oda</strong>. جميع الحقوق محفوظة. 
          </p>
      </div>
      </div>
    </footer>
  );
};

export default Footer;