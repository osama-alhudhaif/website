import { Routes, Route, useLocation, Link } from 'react-router-dom';
import './App.css';
import Header from './constants/Header';
import Footer from './constants/Footer';
import Login from './pages/login';
import Register from './pages/register';
import About from './constants/about';
import Body from './constants/body';
import Reading from './constants/Reading';
import AuthorProfile from './profel/AuthorProfile';
import MyProfile from './profel/MyProfile';
import Contact from './constants/Contact'; 
import Frivacy from './constants/Frivacy';
// import ErrorPage from './errors/AppErrorBoundary';

const App = () => {
  const location = useLocation();

  const isProfilePage = ['/profel/AuthorProfile', '/profel/MyProfile'].includes(location.pathname);

  return (
    <div className="app-wrapper">
      {isProfilePage ? (
        <header style={{ 
          padding: '10px 20px', 
          borderBottom: '1px solid #eee', 
          display: 'flex', 
          alignItems: 'center',
          direction: 'rtl' 
        }}>
          <Link to="/" style={{ textDecoration: 'none', display: 'flex', alignItems: 'center', gap: '10px' }}>
            <img src="/logo.png" alt="Logo" style={{ width: '40px', height: '40px' }} />
            <span style={{ fontSize: '1.2em', fontWeight: 'bold', color: '#333' }}>اسم الموقع</span>
          </Link>
        </header>
      ) : (
        <Header />
      )}

      <div className="app-container">
        <Routes>
          <Route path="/" element={<Body />} /> 
          <Route path="/category/:categoryName" element={<Body />} /> 
          <Route path="/About" element={<About />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/reading" element={<Reading />} />
          <Route path="/profel/AuthorProfile" element={<AuthorProfile />} />
          <Route path="/profel/MyProfile" element={<MyProfile />} />
          <Route path="/contact" element={<Contact />} />
          {/* <Route path="/" element={<ErrorPage />} /> */}
          
          {/* إضافة مسار سياسة الخصوصية هنا لتفعيل الرابط */}
          <Route path="/Frivacy" element={<Frivacy />} />
        </Routes>
      </div>

      <Footer />
    </div>
  );
};

export default App;