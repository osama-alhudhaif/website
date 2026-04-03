import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";

const Login = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();

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
        <div>
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