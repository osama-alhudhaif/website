import "./Footer.css";
import { Link } from "react-router-dom";
import { useTranslation } from "react-i18next";

const Footer = () => {
  const { t } = useTranslation();
  return (
    <footer className="Footer">
      <div className="Footer-Content">
        <div className="Footer-Section">
          <h3 className="Footer-Title">{t('common.appName')}</h3>
          <p className="Footer-Description">{t('footer.description')}</p>
        </div>

        <div className="Footer-Section">
          <h3 className="Footer-Title">{t('footer.help')}</h3>
          <ul className="Footer-Links">
            <li style={{ display: 'flex', gap: '20px' }}>
              <Link to="/About">{t('footer.about')}</Link>
              <Link to="/Contact">{t('footer.contact')}</Link>
            </li>
            <li style={{ display: 'flex', gap: '20px' }}>
              <Link to="/Privacy">{t('footer.privacy')}</Link>
              <Link to="/Terms">{t('footer.terms')}</Link>
            </li>
            <li><Link to="/Partners">{t('footer.partners')}</Link></li>
          </ul>
        </div>

        <div className="Footer-Bottom">
          <p className="Rights">
            &copy; {new Date().getFullYear()} <strong>{t('common.appName')}</strong>. {t('footer.rights')}.
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;