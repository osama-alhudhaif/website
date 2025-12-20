import { Routes, Route } from 'react-router-dom'; // أضفنا Routes و Route
import './App.css';
import Header from './constants/Header';
import Footer from './constants/Footer';
import Login from './pages/login';    // تأكد من استيراد الصفحات
import Register from './pages/register';
import Home from './pages/About';     // أو أي صفحة رئيسية أخرى

const App = () => (
  <>
    <Header />
    <div className="app-container">
      <Routes>
        {/* هنا نحدد أي صفحة تظهر عند كل رابط */}
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
      </Routes>
    </div>
    <Footer />
  </>
);

export default App;