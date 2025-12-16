import { Link } from 'react-router-dom';

const Home = () => {
  return (
    <div style={{ padding: '20px' }}>
      <h1>هذه الصفحة الرئيسية 🏠</h1>
      <Link to="/about">انتقل لصفحة About</Link>
    </div>
  );
};

export default Home; // تأكد من وجود هذا السطر