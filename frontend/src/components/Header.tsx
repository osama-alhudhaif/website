import { Link } from 'react-router-dom';

interface HeaderProps {
  isLoggedIn: boolean;
  userName?: string;
}

// استلام الخصائص isLoggedIn و userName
function Header({ isLoggedIn, userName }: HeaderProps) {
  return (
    <header>
      {/* ... الشعار ... */}
      <div id="log">
        <nav>
          {isLoggedIn ? (
            // إذا كان المستخدم مسجل دخوله
            <>
              <span>مرحباً، {userName || 'مستخدم'}!</span>
              {' / '}
              <Link to="/logout">تسجيل الخروج</Link>
            </>
          ) : (
            // إذا لم يكن المستخدم مسجل دخوله (الحالة الحالية)
            <>
              <Link to="/login">تسجيل الدخول</Link>
              {' / '}
              <Link to="/register">تسجيل حساب جديد</Link>
            </>
          )}
        </nav>
      </div>
    </header>
  );
}

export default Header;