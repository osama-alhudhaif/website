import { useState, useEffect } from "react";

interface ErrorInfo {
  title: string;
  desc: string;
}

interface GlitchTextProps {
  text: string;
  active: boolean;
}

interface ErrorCardProps {
  code: number;
  info: ErrorInfo;
  selected: boolean;
  onClick: (code: number) => void;
}

const errors: Record<number, ErrorInfo> = {
  400: { title: "Bad Request",           desc: "الطلب الذي أرسلته غير صالح أو تالف." },
  401: { title: "Unauthorized",          desc: "يجب عليك تسجيل الدخول للوصول إلى هذه الصفحة." },
  403: { title: "Forbidden",             desc: "ليس لديك صلاحية للوصول إلى هذا المورد." },
  404: { title: "Not Found",             desc: "الصفحة التي تبحث عنها اختفت في الفضاء." },
  408: { title: "Request Timeout",       desc: "استغرق الطلب وقتاً أطول من المتوقع." },
  429: { title: "Too Many Requests",     desc: "لقد أرسلت طلبات كثيرة جداً. أرجو التمهل قليلاً." },
  500: { title: "Internal Server Error", desc: "حدث خطأ غير متوقع في الخادم. نعمل على إصلاحه." },
  502: { title: "Bad Gateway",           desc: "استجابة غير صالحة من الخادم المنتهي." },
  503: { title: "Service Unavailable",   desc: "الخدمة غير متاحة حالياً. يرجى المحاولة لاحقاً." },
  504: { title: "Gateway Timeout",       desc: "انتهت مهلة الاتصال بالخادم المنتهي." },
};

const glitchChars = "!@#$%^&*[]{}";

const scanlineStyle = `
  @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Bebas+Neue&display=swap');

  @keyframes scanline {
    0%   { transform: translateY(-100%); }
    100% { transform: translateY(100vh); }
  }
  @keyframes flicker {
    0%, 100% { opacity: 1; }
    92% { opacity: 1; } 93% { opacity: 0.8; }
    94% { opacity: 1; } 96% { opacity: 0.6; } 97% { opacity: 1; }
  }
  @keyframes blink {
    0%, 100% { opacity: 1; }
    50% { opacity: 0; }
  }
  @keyframes slideUp {
    from { transform: translateY(30px); opacity: 0; }
    to   { transform: translateY(0);    opacity: 1; }
  }
  @keyframes pulse {
    0%, 100% { box-shadow: 0 0 20px rgba(255,60,60,0.3); }
    50%       { box-shadow: 0 0 40px rgba(255,60,60,0.6), 0 0 80px rgba(255,60,60,0.2); }
  }
  .error-display { animation: slideUp 0.4s ease forwards, flicker 8s infinite; }
  .blink         { animation: blink 1s step-end infinite; }
  .pulse-glow    { animation: pulse 3s ease-in-out infinite; }
`;

const GlitchText: React.FC<GlitchTextProps> = ({ text, active }) => {
  const [display, setDisplay] = useState<string>(text);

  useEffect(() => {
    if (!active) { setDisplay(text); return; }
    let frame = 0;
    const interval = setInterval(() => {
      if (frame > 10) { setDisplay(text); clearInterval(interval); return; }
      setDisplay(
        text.split("").map((c: string, i: number) =>
          i < frame ? c : glitchChars[Math.floor(Math.random() * glitchChars.length)]
        ).join("")
      );
      frame++;
    }, 40);
    return () => clearInterval(interval);
  }, [active, text]);

  return <span>{display}</span>;
};

const ErrorCard: React.FC<ErrorCardProps> = ({ code, info, selected, onClick }) => {
  const [glitch, setGlitch] = useState<boolean>(false);

  const handleClick = (): void => {
    setGlitch(true);
    setTimeout(() => setGlitch(false), 500);
    onClick(code);
  };

  return (
    <button
      onClick={handleClick}
      style={{
        background:    selected ? "rgba(255,60,60,0.15)" : "rgba(255,255,255,0.03)",
        border:        selected ? "1px solid rgba(255,60,60,0.6)" : "1px solid rgba(255,255,255,0.08)",
        borderRadius:  "8px",
        padding:       "12px 16px",
        cursor:        "pointer",
        textAlign:     "left",
        transition:    "all 0.2s",
        color:         selected ? "#ff3c3c" : "#888",
        fontFamily:    "'Courier New', monospace",
        fontSize:      "13px",
        letterSpacing: "0.05em",
        width:         "100%",
      }}
    >
      <div style={{ fontSize: "18px", fontWeight: 700, marginBottom: "2px", color: selected ? "#ff3c3c" : "#555" }}>
        {code}
      </div>
      <GlitchText text={info.title} active={glitch} />
    </button>
  );
};

const ErrorPage: React.FC = () => {
  const [selected, setSelected] = useState<number>(500);
  const info: ErrorInfo = errors[selected];

  return (
    <>
      <style>{scanlineStyle}</style>

      <div style={{
        minHeight:     "100vh",
        background:    "#080808",
        color:         "#ccc",
        fontFamily:    "'Share Tech Mono', 'Courier New', monospace",
        display:       "flex",
        flexDirection: "column",
        position:      "relative",
        overflow:      "hidden",
      }}>

        {/* Scanline overlay */}
        <div style={{
          position:      "fixed",
          top: 0, left: 0, right: 0, bottom: 0,
          background:    "repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(0,0,0,0.15) 2px, rgba(0,0,0,0.15) 4px)",
          pointerEvents: "none",
          zIndex:        10,
        }} />
        <div style={{
          position:      "fixed",
          top: 0, left: 0, right: 0,
          height:        "2px",
          background:    "rgba(255,60,60,0.4)",
          animation:     "scanline 6s linear infinite",
          pointerEvents: "none",
          zIndex:        11,
        }} />

        {/* Header */}
        <div style={{
          borderBottom: "1px solid rgba(255,60,60,0.2)",
          padding:      "16px 32px",
          display:      "flex",
          alignItems:   "center",
          gap:          "12px",
        }}>
          <div style={{ width: 10, height: 10, borderRadius: "50%", background: "#ff3c3c", boxShadow: "0 0 8px #ff3c3c" }} />
          <div style={{ width: 10, height: 10, borderRadius: "50%", background: "#ff8c00", boxShadow: "0 0 8px #ff8c00" }} />
          <div style={{ width: 10, height: 10, borderRadius: "50%", background: "#4caf50", boxShadow: "0 0 8px #4caf50" }} />
          <span style={{ marginLeft: 16, color: "#444", fontSize: 12 }}>ERROR_SYSTEM_v2.1 — TERMINAL</span>
        </div>

        <div style={{ display: "flex", flex: 1 }}>

          {/* Sidebar */}
          <div style={{
            width:         220,
            borderRight:   "1px solid rgba(255,255,255,0.06)",
            padding:       "24px 16px",
            display:       "flex",
            flexDirection: "column",
            gap:           "8px",
          }}>
            <div style={{ color: "#444", fontSize: 11, letterSpacing: "0.15em", marginBottom: 8 }}>
              // HTTP ERRORS
            </div>
            {Object.entries(errors).map(([code, errInfo]: [string, ErrorInfo]) => (
              <ErrorCard
                key={code}
                code={Number(code)}
                info={errInfo}
                selected={selected === Number(code)}
                onClick={setSelected}
              />
            ))}
          </div>

          {/* Main display */}
          <div style={{ flex: 1, display: "flex", alignItems: "center", justifyContent: "center", padding: 48 }}>
            <div className="error-display" key={selected} style={{ maxWidth: 600, width: "100%", textAlign: "center" }}>

              {/* Big error code */}
              <div style={{
                fontFamily:           "'Bebas Neue', 'Courier New', monospace",
                fontSize:             "clamp(120px, 20vw, 200px)",
                lineHeight:           0.9,
                background:           "linear-gradient(180deg, #ff3c3c 0%, #8b0000 100%)",
                WebkitBackgroundClip: "text",
                WebkitTextFillColor:  "transparent",
                marginBottom:         8,
                filter:               "drop-shadow(0 0 30px rgba(255,60,60,0.4))",
              }}>
                {selected}
              </div>

              {/* Title */}
              <div style={{
                fontSize:      28,
                fontWeight:    700,
                color:         "#fff",
                letterSpacing: "0.1em",
                marginBottom:  16,
                textTransform: "uppercase",
              }}>
                {info.title}
              </div>

              {/* Terminal description */}
              <div style={{
                background:   "rgba(255,60,60,0.06)",
                border:       "1px solid rgba(255,60,60,0.15)",
                borderRadius: 4,
                padding:      "12px 20px",
                fontSize:     14,
                color:        "#999",
                marginBottom: 40,
                textAlign:    "left",
                direction:    "rtl",
              }}>
                <span style={{ color: "#ff3c3c" }}>ERROR:// </span>
                {info.desc}
                <span className="blink" style={{ color: "#ff3c3c" }}>▌</span>
              </div>

              {/* Divider */}
              <div style={{ display: "flex", alignItems: "center", gap: 16, marginBottom: 40 }}>
                <div style={{ flex: 1, height: 1, background: "rgba(255,60,60,0.2)" }} />
                <span style={{ color: "#333", fontSize: 11, letterSpacing: "0.2em" }}>ACTIONS</span>
                <div style={{ flex: 1, height: 1, background: "rgba(255,60,60,0.2)" }} />
              </div>

              {/* Buttons */}
              <div style={{ display: "flex", gap: 16, justifyContent: "center" }}>
                <a
                  href="/"
                  className="pulse-glow"
                  style={{
                    padding:        "12px 28px",
                    background:     "rgba(255,60,60,0.1)",
                    border:         "1px solid rgba(255,60,60,0.4)",
                    color:          "#ff3c3c",
                    textDecoration: "none",
                    borderRadius:   4,
                    fontSize:       13,
                    letterSpacing:  "0.1em",
                    textTransform:  "uppercase",
                    transition:     "all 0.2s",
                  }}
                >
                  ← الصفحة الرئيسية
                </a>
                <button
                  onClick={(): void => window.location.reload()}
                  style={{
                    padding:       "12px 28px",
                    background:    "transparent",
                    border:        "1px solid rgba(255,255,255,0.1)",
                    color:         "#555",
                    borderRadius:  4,
                    fontSize:      13,
                    letterSpacing: "0.1em",
                    textTransform: "uppercase",
                    cursor:        "pointer",
                    transition:    "all 0.2s",
                  }}
                >
                  ↺ إعادة المحاولة
                </button>
              </div>

              {/* Status bar */}
              <div style={{
                marginTop:      48,
                display:        "flex",
                justifyContent: "center",
                gap:            32,
                color:          "#2a2a2a",
                fontSize:       11,
                letterSpacing:  "0.1em",
              }}>
                <span>STATUS: {selected}</span>
                <span>|</span>
                <span>TYPE: HTTP_ERROR</span>
                <span>|</span>
                <span>LOG_ID: {Math.random().toString(36).substring(2, 10).toUpperCase()}</span>
              </div>

            </div>
          </div>

        </div>
      </div>
    </>
  );
};

export default ErrorPage;