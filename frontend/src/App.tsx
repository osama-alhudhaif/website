import { Routes, Route, useLocation, Link } from 'react-router-dom';
import './App.css';
import Header from './constants/Header';
import Footer from './constants/Footer';
import Login from './pages/login';
import Register from './pages/register';
import UploadStory from './pages/upload-story';
import About from './constants/about';
import Body from './constants/body';
import Reading from './constants/Reading';
import AuthorProfile from './profile/AuthorProfile';
import MyProfile from './profile/MyProfile';
import EditProfile from './profile/EditProfile';
import Contact from './constants/Contact';
import Privacy from './constants/Privacy';
import Terms from './constants/Terms';
import Partners from './constants/Partners';
import ErrorPage from './errors/AppErrorBoundary';
import VerifyEmail from './pages/verify-email';
import ForgotPassword from './pages/forgot-password';
import ResetPassword from './pages/reset-password';

const App = () => {
  const location = useLocation();

  const isProfilePage = ['/profile/me', '/profile/edit'].includes(location.pathname)
    || location.pathname.startsWith('/profile/author/');

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
            <img src="/Website.png" alt="Logo" style={{ width: '40px', height: '40px' }} />
            <span style={{ fontSize: '1.2em', fontWeight: 'bold', color: '#333' }}>أودا</span>
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
          <Route path="/upload-story" element={<UploadStory />} />
          <Route path="/reading/:id" element={<Reading />} />
          <Route path="/profile/me" element={<MyProfile />} />
          <Route path="/profile/edit" element={<EditProfile />} />
          <Route path="/profile/author/:authorId" element={<AuthorProfile />} />
          <Route path="/verify-email/:uid/:token" element={<VerifyEmail />} />
          <Route path="/forgot-password" element={<ForgotPassword />} />
          <Route path="/reset-password/:uid/:token" element={<ResetPassword />} />
          <Route path="/Contact" element={<Contact />} />
          <Route path="/errors" element={<ErrorPage />} />
          <Route path="/Privacy" element={<Privacy />} />
          <Route path="/Terms" element={<Terms />} />
          <Route path="/Partners" element={<Partners />} />
        </Routes>
      </div>

      <Footer />
    </div>
  );
};

export default App;
