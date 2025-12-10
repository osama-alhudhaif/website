import React from 'react';
import { Link } from 'react-router-dom';

function Header() {
  return (
    <header>
      <div id="nameLogo">
        <h1>عوالمنا</h1>
        <img src="/Website.jpg" alt="شعار موقع عوالمنا" />
      </div>
      <div id="log">
        <nav>
          <Link to="/login">تسجيل الدخول</Link>
          {' / '}
          <Link to="/register">تسجيل حساب جديد</Link>
        </nav>
      </div>
    </header>
  );
}

export default Header;