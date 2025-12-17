import { Outlet } from 'react-router-dom';
import './App.css';
import Header from './constants/Header';
import Footer from './constants/Footer';

const App = () => (
  <>
    <Header />
    <div className="app-container">
      <Outlet />
    </div>
    <Footer />
  </>
);

export default App;

