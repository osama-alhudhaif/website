import { useState, useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useTranslation } from "react-i18next";
import { API_BASE_URL } from "../config/api";

const Login = () => {
    const { t } = useTranslation();
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [rememberMe, setRememberMe] = useState(false);
    const [error, setError] = useState("");
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();

    useEffect(() => {
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
                    localStorage.setItem("token", data.token);
                    localStorage.setItem("username", data.user.username);
                    localStorage.setItem("user_id", String(data.user.id));
                } else {
                    sessionStorage.setItem("token", data.token);
                    sessionStorage.setItem("username", data.user.username);
                    sessionStorage.setItem("user_id", String(data.user.id));
                }
                navigate("/");
            } else {
                setError(data.detail || t('login.invalidCredentials'));
            }
        } catch {
            setError(t('common.serverError'));
        } finally {
            setLoading(false);
        }
    };

    return (
        <div style={{ display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center", height: "100vh" }}>
            <h1>{t('login.title')}</h1>
            {error && <p style={{ color: "red" }}>{error}</p>}
            <form onSubmit={handleSubmit}>
                <label htmlFor="username">{t('login.username')}</label>
                <input type="text" id="username" value={username} onChange={(e) => setUsername(e.target.value)} required /><br />
                <label htmlFor="password">{t('login.password')}</label>
                <input type="password" id="password" value={password} onChange={(e) => setPassword(e.target.value)} required /><br />
                <label htmlFor="rememberMe" style={{ display: "flex", alignItems: "center", gap: "6px", cursor: "pointer" }}>
                    <input type="checkbox" id="rememberMe" checked={rememberMe} onChange={(e) => setRememberMe(e.target.checked)} />
                    {t('login.rememberMe')}
                </label><br />
                <button type="submit" disabled={loading}>
                    {loading ? t('common.loading') : t('login.submit')}
                </button>
                <div style={{ marginTop: "10px", display: "flex", justifyContent: "space-between" }}>
                    <Link to="/register">{t('login.register')}</Link>
                    <Link to="/forgot-password">{t('login.forgotPassword')}</Link>
                </div>
            </form>
        </div>
    );
};

export default Login;
