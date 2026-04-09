import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import { API_BASE_URL } from "../config/api";

const VerifyEmail = () => {
    const { uid, token } = useParams<{ uid: string; token: string }>();
    const [status, setStatus] = useState<"loading" | "success" | "error">("loading");
    const [message, setMessage] = useState("");

    useEffect(() => {
        fetch(`${API_BASE_URL}/accounts/verify-email/${uid}/${token}/`)
            .then(res => res.json())
            .then(data => {
                if (data.message) { setStatus("success"); setMessage(data.message); }
                else { setStatus("error"); setMessage(data.error || "حدث خطأ"); }
            })
            .catch(() => { setStatus("error"); setMessage("تعذر الاتصال بالخادم"); });
    }, [uid, token]);

    return (
        <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", minHeight: "60vh", direction: "rtl" }}>
            {status === "loading" && <p>جاري التحقق...</p>}
            {status === "success" && (
                <div style={{ textAlign: "center" }}>
                    <div style={{ fontSize: "50px" }}>✅</div>
                    <h2 style={{ color: "#34a853" }}>{message}</h2>
                    <Link to="/login" style={{ padding: "10px 24px", backgroundColor: "#1a73e8", color: "#fff", borderRadius: "6px", textDecoration: "none", display: "inline-block", marginTop: "16px" }}>
                        تسجيل الدخول
                    </Link>
                </div>
            )}
            {status === "error" && (
                <div style={{ textAlign: "center" }}>
                    <div style={{ fontSize: "50px" }}>❌</div>
                    <h2 style={{ color: "#ea4335" }}>{message}</h2>
                    <Link to="/register" style={{ color: "#1a73e8" }}>إنشاء حساب جديد</Link>
                </div>
            )}
        </div>
    );
};

export default VerifyEmail;
