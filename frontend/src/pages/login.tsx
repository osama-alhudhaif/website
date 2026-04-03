import { useState, useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";

// Helper functions للكوكيز
const setPermanentCookie = (name: string, value: string) => {
    // Set cookie to expire in 10 years (effectively permanent)
    const expires = new Date(Date.now() + 10 * 365 * 864e5).toUTCString();
    document.cookie = `${name}=${encodeURIComponent(value)}; expires=${expires}; path=/`;
};

const getCookie = (name: string): string | null => {
    return document.cookie
        .split("; ")
        .find((row) => row.startsWith(`${name}=`))
        ?.split("=")[1]
        ? decodeURIComponent(document.cookie.split("; ").find((row) => row.startsWith(`${name}=`))!.split("=")[1])
        : null;
};

const deleteCookie = (name: string) => {
    document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/`;
};

// style

const Login = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [rememberMe, setRememberMe] = useState(false);
    const [error, setError] = useState("");
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();

    // تحقق من وجود توكن محفوظ عند تحميل الصفحة
    useEffect(() => {
        const savedToken = getCookie("token");
        if (savedToken) {
            localStorage.setItem("token", savedToken);
            navigate("/");
        }
    }, [navigate]);

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setError("");
        setLoading(true);

        try {
            const response = await fetch("http://localhost:8000/api/v1/accounts/login/", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ username, password }),
            });

            const data = await response.json();

            if (response.ok) {
                localStorage.setItem("token", data.token);
                localStorage.setItem("username", data.user.username);

                // إذا اختار "تذكرني" → خزّن التوكن بشكل دائم (10 سنوات)
                if (rememberMe) {
                    setPermanentCookie("token", data.token);
                    setPermanentCookie("username", data.user.username);
                } else {
                    // امسح أي كوكيز قديمة إذا ما اختار تذكرني
                    deleteCookie("token");
                    deleteCookie("username");
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
                <input
                    type="text"
                    id="username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    required
                />
                <br />
                <label htmlFor="password">كلمة المرور</label>
                <input
                    type="password"
                    id="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                />
                <br />

                {/* زر تذكرني */}
                <label htmlFor="rememberMe" style={{ display: "flex", alignItems: "center", gap: "6px", cursor: "pointer" }}>
                    <input
                        type="checkbox"
                        id="rememberMe"
                        checked={rememberMe}
                        onChange={(e) => setRememberMe(e.target.checked)}
                    />
                    تذكرني
                </label>
                <br />

                <button type="submit" disabled={loading}>
                    {loading ? "جاري التحميل..." : "تسجيل الدخول"}
                </button>
                <div style={{ marginTop: "10px" }}>
                    <Link to="/register">إنشاء حساب</Link>
                </div>
            </form>
        </div>
    );
};

export default Login;