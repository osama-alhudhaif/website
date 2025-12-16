import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import MainContent from './components/MainContent';
import Footer from './components/Footer';
import About from './components/About';
import './App.css'; // استيراد CSS

const username = "سالم"; // مثال على بيانات

const App: React.FC = () => {
  return (
    <div className="Router">
    <Router>
      <div className="page-container" dir="rtl">
        <Header userName={username} isLoggedIn={false} />
        <Routes>
          <Route path="/" element={<MainContent />} />
          <Route path="/about" element={<About />} />
        </Routes>
        <Footer />
      </div>
    </Router>
    </div>
  );
};

export default App;
