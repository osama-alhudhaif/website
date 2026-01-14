import { Routes, Route } from 'react-router-dom';
import './App.css';
import Header from './constants/Header';
import Footer from './constants/Footer';
import Login from './pages/login';
import Register from './pages/register';
import About from './constants/about';
import Body from './constants/body';
import Reading from './constants/reading';

const App = () => {
  return (
    <div className="app-wrapper">
      <Header />
      <div className="app-container">
        <Routes>
          <Route path="/About" element={<About />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/reading" element={<Reading />} />
        </Routes>
      </div>
      <Body />
      <Footer />
    </div>
  );
};

export default App;