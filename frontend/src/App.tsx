import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import MainContent from './components/MainContent';
import Footer from './components/Footer';
import './App.css'; // استيراد CSS

const App: React.FC = () => {
  return (
    <Router>
      <div className="page-container" dir="rtl"> {/* دعم RTL للعربية */}
        <Header />
        <Routes>
          <Route path="/" element={<MainContent />} />
          {/* يمكن إضافة المزيد من الروابط هنا، مثل <Route path="/login" element={<Login />} /> */}
        </Routes>
        <Footer />
      </div>
    </Router>
  );
};

export default App;