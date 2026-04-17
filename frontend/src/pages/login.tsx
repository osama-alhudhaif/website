import { useState, useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";
import { API_BASE_URL } from "../config/api";

// الإصدار 2 و 4: إزالة تخزين التوكن في cookies غير آمنة من طرف العميل
// التوكن يُخزَّن في sessionStorage عند عدم تفعيل "تذكرني"، وفي localStorage عند تفعيله
// لا يجب تعيين cookies تحتوي على التوكن من JavaScript لأنها لا تدعم HttpOnly

const Login = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [rememberMe, setRememberMe] = useState(false);
    const [error, setError] = useState("");
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();

    useEffect(() => {
        // التحقق من وجود توكن محفوظ في أحد المخزنين
        const savedToken = localStorage.getItem("token") || sessionStorage.getItem("token");
        if (savedToken) { navigate("/"); }
    }, [navigate]);

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setError(""); setLoading(true);
        try {
            const response = await fetch(`${API_BASE_URL}/accounts/login/`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ username, password }),
            });
            const data = await response.json();
            if (response.ok) {
                if (rememberMe) {
                    // الإصدار 2: تخزين التوكن في localStorage عند اختيار "تذكرني"
                    localStorage.setItem("token", data.token);
                    localStorage.setItem("username", data.user.username);
                } else {
                    // الإصدار 2: تخزين التوكن في sessionStorage (يُمسح عند إغلاق المتصفح)
                    sessionStorage.setItem("token", data.token);
                    sessionStorage.setItem("username", data.user.username);
                }
                navigate("/");
            } else {
                setError(data.detail || "خطأ في اسم المستخدم أو كلمة المرور");
            }
        } catch {
            setError("تعذر الاتصال بالخادم");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div style={{ display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center", height: "100vh" }}>
            <h1>تسجيل الدخول</h1>
            {error && <p style={{ color: "red" }}>{error}</p>}
            <form onSubmit={handleSubmit}>
                <label htmlFor="username">اسم المستخدم</label>
                <input type="text" id="username" value={username} onChange={(e) => setUsername(e.target.value)} required /><br />
                <label htmlFor="password">كلمة المرور</label>
                <input type="password" id="password" value={password} onChange={(e) => setPassword(e.target.value)} required /><br />
                <label htmlFor="rememberMe" style={{ display: "flex", alignItems: "center", gap: "6px", cursor: "pointer" }}>
                    <input type="checkbox" id="rememberMe" checked={rememberMe} onChange={(e) => setRememberMe(e.target.checked)} />
                    تذكرني
                </label><br />
                <button type="submit" disabled={loading}>{loading ? "جاري التحميل..." : "تسجيل الدخول"}</button>
                <div style={{ marginTop: "10px", display: "flex", justifyContent: "space-between" }}>
                    <Link to="/register">إنشاء حساب</Link>
                    <Link to="/forgot-password">نسيت كلمة المرور؟</Link>
                </div>
            </form>
        </div>
    );
};

export default Login;
