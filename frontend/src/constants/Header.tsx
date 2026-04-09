import { Link, Outlet, useNavigate } from "react-router-dom";
import './Header.css';

const menuItemStyle: React.CSSProperties = {
    display: 'block',
    padding: '10px 16px',
    color: '#fff',
    textDecoration: 'none',
    cursor: 'pointer',
    fontSize: '14px',
};

const Header = () => {
  const navigate = useNavigate();

  const handleCategoryChange = (e: { target: { value: any; }; }) => {
    const category = e.target.value;
    if (category) {
      navigate(`/category/${category}`);
    }
  };

  const toggleMenu = () => {
    const menu = document.getElementById('user-menu');
    if (menu) menu.style.display = menu.style.display === 'none' ? 'block' : 'none';
  };

  const toggleDarkMode = () => {
    const isDark = document.body.style.backgroundColor === 'rgb(18, 18, 18)';
    document.body.style.backgroundColor = isDark ? '' : '#121212';
    document.body.style.color = isDark ? '' : '#fff';
  };

  const handleLogout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('username');
    window.location.href = '/';
  };

  return (
    <div className="Main-Container">
      <header className="Header">
        <div className="Right-Side">
          <Link to="/" className="Logo-link">
            <img src="/Website.png" alt="Logo" className="logo-img" />
            <h2 className="Brand-Name">أودا</h2>
          </Link>
        </div>

        <div className="Left-Side">
          <nav className="Nav-Links">
            
            <div className="Select-Container">
              <select 
                className="Custom-Select" 
                defaultValue=""
                onChange={handleCategoryChange}
              >
                <option value="" disabled>اختر الفئة</option>
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
              <span className="Select-Arrow">▼</span>
            </div>

            {localStorage.getItem('token') ? (
              <div className="User-Menu-Container">
                <span className="User-Name" onClick={toggleMenu}>
                  {localStorage.getItem('username') || 'حسابي'} ▼
                </span>
                <div id="user-menu" className="user-menu" style={{ display: 'none' }}>
                  <Link to="/profile/me" style={menuItemStyle}>👤 حسابي</Link>
                  <Link to="/settings" style={menuItemStyle}>⚙️ الإعدادات</Link>
                  <div style={menuItemStyle} onClick={toggleDarkMode}>🌙 المظهر</div>
                  <div style={{ ...menuItemStyle, color: '#e74c3c' }} onClick={handleLogout}>🚪 تسجيل خروج</div>
                </div>
              </div>
            ) : (
              <>
                <Link to="/login" className="Nav-Item">تسجيل الدخول</Link>
                <Link to="/register" className="Nav-Item Register-Btn">انشاء حساب</Link>
              </>
            )}

          </nav>
        </div>
      </header>

      <main className="Content-Area">
        <Outlet />
      </main>
    </div>
  );
};

export default Header;