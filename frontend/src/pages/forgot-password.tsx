import { useState } from "react";
import { Link } from "react-router-dom";
import { API_BASE_URL } from "../config/api";

const ForgotPassword = () => {
    const [email, setEmail] = useState("");
    const [loading, setLoading] = useState(false);
    const [message, setMessage] = useState("");
    const [error, setError] = useState("");

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setLoading(true); setMessage(""); setError("");
        const res = await fetch(`${API_BASE_URL}/accounts/password-reset/`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email }),
        }).catch(() => null);
        setLoading(false);
        if (!res) { setError("تعذر الاتصال بالخادم"); return; }
        const data = await res.json();
        if (data.message) setMessage(data.message);
        else setError(data.error || "حدث خطأ");
    };

    return (
        <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", minHeight: "70vh", direction: "rtl" }}>
            <div style={{ width: "100%", maxWidth: "400px", padding: "30px" }}>
                <h2>استعادة كلمة المرور</h2>
                <p style={{ color: "#666" }}>أدخل بريدك الإلكتروني وسنرسل لك رابط الاستعادة.</p>
                {message && <div style={{ padding: "10px", backgroundColor: "#e6f4ea", color: "#34a853", borderRadius: "6px", marginBottom: "16px" }}>{message}</div>}
                {error && <div style={{ padding: "10px", backgroundColor: "#fce8e6", color: "#ea4335", borderRadius: "6px", marginBottom: "16px" }}>{error}</div>}
                <form onSubmit={handleSubmit}>
                    <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="البريد الإلكتروني" required
                        style={{ width: "100%", padding: "10px", borderRadius: "6px", border: "1px solid #ddd", marginBottom: "12px", fontSize: "14px" }} />
                    <button type="submit" disabled={loading}
                        style={{ width: "100%", padding: "12px", backgroundColor: "#1a73e8", color: "#fff", border: "none", borderRadius: "6px", cursor: "pointer", fontSize: "15px" }}>
                        {loading ? "جاري الإرسال..." : "إرسال رابط الاستعادة"}
                    </button>
                </form>
                <div style={{ marginTop: "16px", textAlign: "center" }}>
                    <Link to="/login" style={{ color: "#1a73e8" }}>العودة لتسجيل الدخول</Link>
                </div>
            </div>
        </div>
    );
};

export default ForgotPassword;
