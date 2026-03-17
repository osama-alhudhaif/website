import "./Footer.css";
import { Link } from "react-router-dom";

const Footer = () => {
  return (
    <footer className="Footer">
      <div className="Footer-Content">
        <div className="Footer-Section">
          <h3 className="Footer-Title">Oda</h3>
          <p className="Footer-Description">
            نبتكر في <strong>Oda</strong> لتطوير أجهزة
            <span className="product-name"> كتابنا</span> و
            <span className="product-name"> ورقنا</span>
            بذكاء المدرب الرقمي <strong>أديب</strong>.
          </p>
        </div>

        <div className="Footer-Section">
          <h3 className="Footer-Title">المساعدة</h3>
          <ul className="Footer-Links">
            <li><Link to="/About">من نحن</Link></li>
            <li><Link to="/Contact">تواصل معنا</Link></li>
            <li><Link to="/Frivacy">سياسة الخصوصية</Link></li>
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