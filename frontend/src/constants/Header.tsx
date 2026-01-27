import { Link, Outlet, useNavigate } from "react-router-dom";

const Header = () => {
  const navigate = useNavigate();

  // دالة التعامل مع تغيير الفئة
  const handleCategoryChange = (e: { target: { value: any; }; }) => {
    const category = e.target.value;
    if (category) {
      // سينقلك لصفحة موحدة للفئات، مثلاً: /action
      navigate(`${category}`);
    }
  };

  return (
    <div className="Main-Container">
      <header className="Header" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '10px 20px' }}>
        <div className="Right-Side">
          <Link to="/" className="Logo-link" style={{ display: 'flex', alignItems: 'center', textDecoration: 'none' }}>
            <img src="/Website.png" alt="Logo" className="logo-img" style={{ width: '40px', marginLeft: '10px' }} />
            <h2 className="Brand-Name" style={{ color: '#fff', margin: 0 }}>Oda</h2>
          </Link>
        </div>

        <div className="Left-Side">
          <nav className="Nav-Links" style={{ display: 'flex', alignItems: 'center', gap: '20px' }}>
            
            {/* القائمة المنسدلة الذكية */}
            <div className="Select-Container" style={{ position: 'relative', width: '160px', direction: 'rtl' }}>
              <select 
                className="Custom-Select" 
                defaultValue=""
                onChange={handleCategoryChange}
                style={{
                  width: '100%',
                  padding: '8px 12px',
                  fontSize: '14px',
                  color: '#fff',
                  backgroundColor: 'rgba(255, 255, 255, 0.08)', // شفافية ناعمة
                  border: '1px solid rgba(255, 255, 255, 0.2)',
                  borderRadius: '20px', // حواف دائرية أكثر عصرية
                  appearance: 'none',
                  WebkitAppearance: 'none',
                  cursor: 'pointer',
                  outline: 'none',
                  transition: '0.3s ease',
                  textAlign: 'right'
                }}
                onFocus={(e) => {
                    e.target.style.borderColor = '#3498db';
                    e.target.style.backgroundColor = 'rgba(255, 255, 255, 0.15)';
                }}
                onBlur={(e) => {
                    e.target.style.borderColor = 'rgba(255, 255, 255, 0.2)';
                    e.target.style.backgroundColor = 'rgba(255, 255, 255, 0.08)';
                }}
              >
                <option value="" disabled style={{ backgroundColor: '#1a1a1a' }}>اختر الفئة</option>
                <option value="war" style={{ backgroundColor: '#1a1a1a' }}>حرب</option>
                <option value="sci-fi" style={{ backgroundColor: '#1a1a1a' }}>خيال علمي</option>
                <option value="action" style={{ backgroundColor: '#1a1a1a' }}>أكشن</option>
                <option value="fantasy" style={{ backgroundColor: '#1a1a1a' }}>الفانتازيا</option>
                <option value="mystery" style={{ backgroundColor: '#1a1a1a' }}>الجريمة والغموض</option>
                <option value="horror" style={{ backgroundColor: '#1a1a1a' }}>الرعب</option>
                <option value="history" style={{ backgroundColor: '#1a1a1a' }}>القصص التاريخية</option>
                <option value="heist" style={{ backgroundColor: '#1a1a1a' }}>سرقة</option>
                <option value="adventure" style={{ backgroundColor: '#1a1a1a' }}>المغامرات</option>
                <option value="romance" style={{ backgroundColor: '#1a1a1a' }}>رومانسية</option>
              </select>

              {/* سهم أيقوني صغير */}
              <span style={{
                position: 'absolute',
                left: '12px',
                top: '50%',
                transform: 'translateY(-50%)',
                color: '#fff',
                pointerEvents: 'none',
                fontSize: '10px',
                opacity: 0.7
              }}>▼</span>
            </div>

            <Link to="/login" className="Nav-Item" style={{ color: '#fff', textDecoration: 'none' }}>تسجيل الدخول</Link>
            <Link to="/register" className="Nav-Item" style={{ 
                color: '#fff', 
                textDecoration: 'none',
                backgroundColor: '#3498db', 
                padding: '8px 15px', 
                borderRadius: '20px' 
            }}>انشاء حساب</Link>
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