import { createBrowserRouter, RouterProvider, Link, Outlet } from 'react-router-dom';
import Home from './pages/Home';
import About from './pages/About';

// مكون الـ Layout لإضافة Navbar ثابت
const Layout = () => (
  <div className="Header">
    <div className="Logo">
      <h2>
      عوالمنا
      </h2>
      <p></p>
    <img src="./Website.jpg" alt="Logo" className="logo-img" />
    </div>
    <div>
    <nav style={{ padding: '10px', background: '#f4f4f4', marginBottom: '20px' }}>
      <Link to="/" style={{ marginRight: '15px' }}>الرئيسية</Link>
      \
      <Link to="/about">عن الموقع</Link>
    </nav>
    </div>
    <hr />
    <Outlet /> {/* هنا سيتم عرض محتوى الصفحة (Home أو About) */}
  </div>
);

const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />, // الـ Layout يحيط بكل الصفحات
    children: [
      { path: "/", element: <Home /> },
      { path: "/about", element: <About /> },
    ],
  },
]);

export default function App() {
  return <RouterProvider router={router} />;
}