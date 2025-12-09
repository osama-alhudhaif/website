// start my website
function App() {
  return (
    <>
      <header>
        <div id="nameLogo">
          <h1>عوالمنا</h1>
          <img src="/Website.jpg" alt="Website logo" />
        </div>
        <div id="log">
          {/* Changed h6 to nav or div because h6 is for headers, not links */}
          <nav>
            <a href="/login">تسجيل الدخول</a>
            {' / '}
            <a href="/register">تسجيل حساب جديد</a>
          </nav>
        </div>
      </header>
      <main>
        <p>موقع عالمي لعرض القصص والروايات بكل اللغات مع توفير خدمة ترجمة فورية ودقيقة من وإلى أي لغة.</p>
      </main>
    </>
  );
}

export default App;