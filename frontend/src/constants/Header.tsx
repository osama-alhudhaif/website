import { Link, Outlet } from "react-router-dom";

const Header = () => {
  return (
    <div className="Main-Container">
      <header className="Header">
        <div className="Right-Side">
          <Link to="/" className="Logo-link">
            <img src="./public/Website.png" alt="Logo" className="logo-img" />
            <h2 className="Brand-Name">عوالمنا</h2>
          </Link>
        </div>

        <div className="Left-Side">
          <nav className="Nav-Links">
            <Link to="/login">تسجيل الدخول</Link>
            <Link to="/register">انشاء حساب</Link>
          </nav>
        </div>
      </header>
      <div className="Header-Content">
        <p>مرحبا بك في عوالمنا</p>
      </div>

      <main className="Content-Area">
        <Outlet />
      </main>
    </div>
  );
};

export default Header;
