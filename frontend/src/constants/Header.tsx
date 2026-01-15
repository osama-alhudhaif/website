import { Link, Outlet } from "react-router-dom";

const Header = () => {
  return (
    <div className="Main-Container">
      <header className="Header">
        <div className="Right-Side">
          <Link to="/" className="Logo-link">
            {/* تم تصحيح المسار ليعمل بشكل صحيح من مجلد public */}
            <img src="/Website.png" alt="Logo" className="logo-img" />
            <h2 className="Brand-Name">Oda</h2>
          </Link>
        </div>

        <div className="Left-Side">
          {/* أضفنا تنسيق Flexbox لجعل العناصر متراصفة وبمسافات متساوية */}
<nav className="Nav-Links">
  {/* حاوية خاصة للقائمة المنسدلة */}
  <div className="Select-Container">
    <select className="Custom-Select">
      <option value="" disabled selected>اختر الفئة</option>
      <option value="war">حرب</option>
      <option value="sci-fi">خيال علمي</option>
      <option value="action">أكشن</option>
      <option value="fantasy">الفانتازيا</option>
      <option value="mystery">الجريمة والغموض</option>
      <option value="horror">الرعب</option>
      <option value="history">القصص التاريخية</option>
      <option value="heist">سرقة</option>
      <option value="adventure">المغامرات</option>
      <option value="romance">رومانسية</option>
    </select>
  </div>
  
  <Link to="/login" className="Nav-Item">تسجيل الدخول</Link>
  <Link to="/register" className="Nav-Item">انشاء حساب</Link>
</nav>
        </div>
      </header>

      {/* منطقة المحتوى المتغير */}
      <main className="Content-Area">
        <Outlet />
      </main>
    </div>
  );
};

export default Header;