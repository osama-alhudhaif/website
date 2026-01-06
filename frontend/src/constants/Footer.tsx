import "./Footer.css";

const Footer = () => {
  return (
    <footer className="Footer">
      <div className="Footer-Content">
        
        {/* قسم معلومات مشروع عوالمنا */}
        <div className="Footer-Section">
          <h3 className="Footer-Title">عوالمنا</h3>
          <p className="Footer-Description">
            نبتكر في <strong>عوالمنا</strong> لتطوير أجهزة 
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
          <hr className="Footer-Divider" />
          <p className="Rights">
            &copy; {new Date().getFullYear()} <strong>عوالمنا</strong>. جميع الحقوق محفوظة. 
            تم التطوير بواسطة <strong>أديب</strong>.
          </p>
      </div>
      </div>
    </footer>
  );
};

export default Footer;