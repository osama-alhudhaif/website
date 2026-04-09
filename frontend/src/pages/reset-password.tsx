import { useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { API_BASE_URL } from "../config/api";

const ResetPassword = () => {
    const { uid, token } = useParams<{ uid: string; token: string }>();
    const navigate = useNavigate();
    const [password, setPassword] = useState("");
    const [confirm, setConfirm] = useState("");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        if (password !== confirm) { setError("كلمتا المرور غير متطابقتين"); return; }
        if (password.length < 8) { setError("كلمة المرور يجب أن تكون 8 أحرف على الأقل"); return; }
        setLoading(true); setError("");
        const res = await fetch(`${API_BASE_URL}/accounts/password-reset/confirm/${uid}/${token}/`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ new_password: password }),
        }).catch(() => null);
        setLoading(false);
        if (!res) { setError("تعذر الاتصال بالخادم"); return; }
        const data = await res.json();
        if (data.message) navigate("/login");
        else setError(data.error || "حدث خطأ");
    };

    return (
        <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", minHeight: "70vh", direction: "rtl" }}>
            <div style={{ width: "100%", maxWidth: "400px", padding: "30px" }}>
                <h2>تعيين كلمة مرور جديدة</h2>
                {error && <div style={{ padding: "10px", backgroundColor: "#fce8e6", color: "#ea4335", borderRadius: "6px", marginBottom: "16px" }}>{error}</div>}
                <form onSubmit={handleSubmit}>
                    <label style={{ display: "block", marginBottom: "6px" }}>كلمة المرور الجديدة</label>
                    <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required
                        style={{ width: "100%", padding: "10px", borderRadius: "6px", border: "1px solid #ddd", marginBottom: "12px" }} />
                    <label style={{ display: "block", marginBottom: "6px" }}>تأكيد كلمة المرور</label>
                    <input type="password" value={confirm} onChange={(e) => setConfirm(e.target.value)} required
                        style={{ width: "100%", padding: "10px", borderRadius: "6px", border: "1px solid #ddd", marginBottom: "16px" }} />
                    <button type="submit" disabled={loading}
                        style={{ width: "100%", padding: "12px", backgroundColor: "#1a73e8", color: "#fff", border: "none", borderRadius: "6px", cursor: "pointer", fontSize: "15px" }}>
                        {loading ? "جاري الحفظ..." : "حفظ كلمة المرور"}
                    </button>
                </form>
            </div>
        </div>
    );
};

export default ResetPassword;
