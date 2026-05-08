import { Link, Outlet, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import { useTranslation } from "react-i18next";
import { API_BASE_URL, getToken, getUsername, clearAuth } from "../config/api";
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
  const { t, i18n } = useTranslation();
  const [unreadCount, setUnreadCount] = useState(0);
  const token = getToken();
  const isRTL = i18n.language === 'ar' || i18n.language.startsWith('ar');

  useEffect(() => {
    if (!token) return;
    const fetchUnread = () => {
      fetch(`${API_BASE_URL}/accounts/notifications/unread-count/`, {
        headers: { Authorization: `Token ${token}` },
      })
        .then(r => r.ok ? r.json() : null)
        .then(data => { if (data) setUnreadCount(data.unread_count || 0); })
        .catch(() => {});
    };
    fetchUnread();
    const interval = setInterval(fetchUnread, 60000);
    return () => clearInterval(interval);
  }, [token]);

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
    clearAuth();
    window.location.href = '/';
  };

  const switchLanguage = () => {
    const next = i18n.language.startsWith('ar') ? 'en' : 'ar';
    i18n.changeLanguage(next);
  };

  return (
    <div className="Main-Container">
      <header className="Header" style={{ direction: isRTL ? 'rtl' : 'ltr' }}>
        <div className="Right-Side">
          <Link to="/" className="Logo-link">
            <img src="/Website.png" alt="Logo" className="logo-img" />
            <h2 className="Brand-Name">{t('common.appName')}</h2>
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
                <option value="" disabled>{t('header.chooseCategory')}</option>
                <option value="war">{t('categories.war')}</option>
                <option value="sci-fi">{t('categories.sci-fi')}</option>
                <option value="action">{t('categories.action')}</option>
                <option value="fantasy">{t('categories.fantasy')}</option>
                <option value="mystery">{t('categories.mystery')}</option>
                <option value="horror">{t('categories.horror')}</option>
                <option value="history">{t('categories.history')}</option>
                <option value="heist">{t('categories.heist')}</option>
                <option value="adventure">{t('categories.adventure')}</option>
                <option value="romance">{t('categories.romance')}</option>
              </select>
              <span className="Select-Arrow">▼</span>
            </div>

            {/* زر تبديل اللغة */}
            <button
              onClick={switchLanguage}
              style={{
                background: 'none', border: '1px solid #ccc', borderRadius: '6px',
                padding: '4px 10px', cursor: 'pointer', fontSize: '13px',
                color: 'inherit',
              }}
            >
              {isRTL ? 'EN' : 'ع'}
            </button>

            {token ? (
              <>
                <Link to="/notifications" style={{ position: 'relative', textDecoration: 'none', display: 'flex', alignItems: 'center' }}>
                  <span style={{ fontSize: '20px' }}>🔔</span>
                  {unreadCount > 0 && (
                    <span style={{
                      position: 'absolute', top: '-6px', left: '-6px',
                      backgroundColor: '#e74c3c', color: '#fff',
                      borderRadius: '50%', width: '18px', height: '18px',
                      fontSize: '11px', display: 'flex', alignItems: 'center', justifyContent: 'center',
                      fontWeight: '700',
                    }}>
                      {unreadCount > 9 ? '9+' : unreadCount}
                    </span>
                  )}
                </Link>
                <div className="User-Menu-Container">
                  <span className="User-Name" onClick={toggleMenu}>
                    {getUsername() || t('header.myAccount')} ▼
                  </span>
                  <div id="user-menu" className="user-menu" style={{ display: 'none' }}>
                    <Link to="/profile/me" style={menuItemStyle}>👤 {t('header.myAccount')}</Link>
                    <Link to="/notifications" style={menuItemStyle}>🔔 {t('header.notifications')} {unreadCount > 0 && `(${unreadCount})`}</Link>
                    <Link to="/settings" style={menuItemStyle}>⚙️ {t('header.settings')}</Link>
                    <div style={menuItemStyle} onClick={toggleDarkMode}>🌙 {t('header.appearance')}</div>
                    <div style={{ ...menuItemStyle, color: '#e74c3c' }} onClick={handleLogout}>🚪 {t('header.logout')}</div>
                  </div>
                </div>
              </>
            ) : (
              <>
                <Link to="/login" className="Nav-Item">{t('header.login')}</Link>
                <Link to="/register" className="Nav-Item Register-Btn">{t('header.register')}</Link>
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
