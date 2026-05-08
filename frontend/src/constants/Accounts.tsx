import { type FC, useState, useEffect } from "react";
import { useNavigate, Link } from "react-router-dom";
import { useTranslation } from "react-i18next";
import { API_BASE_URL, getToken, clearAuth } from "../config/api";

interface UserAccount {
    id: number;
    username: string;
    email: string;
    first_name: string;
    last_name: string;
    role: string;
    phone: string;
    country: string;
    gender: string;
    date_of_birth: string;
    dark_mode_enabled: boolean;
    date_joined: string;
}

type Tab = "info" | "password" | "preferences";

const Accounts: FC = () => {
    const navigate = useNavigate();
    const { t, i18n } = useTranslation();
    const isRTL = i18n.language === 'ar' || i18n.language.startsWith('ar');
    const [user, setUser] = useState<UserAccount | null>(null);
    const [loading, setLoading] = useState(true);
    const [activeTab, setActiveTab] = useState<Tab>("info");

    const [pwForm, setPwForm] = useState({ current_password: "", new_password: "", confirm_password: "" });
    const [pwLoading, setPwLoading] = useState(false);
    const [pwSuccess, setPwSuccess] = useState("");
    const [pwError, setPwError] = useState("");

    const [darkMode, setDarkMode] = useState(false);
    const [prefSaving, setPrefSaving] = useState(false);
    const [prefMessage, setPrefMessage] = useState("");

    useEffect(() => {
        const token = getToken();
        if (!token) { navigate("/login"); return; }
        fetch(`${API_BASE_URL}/accounts/me/`, {
            headers: { Authorization: `Token ${token}` },
        })
            .then(r => {
                if (r.status === 401) { localStorage.removeItem("token"); navigate("/login"); return null; }
                return r.json();
            })
            .then(data => {
                if (!data) return;
                setUser(data);
                setDarkMode(data.dark_mode_enabled ?? false);
            })
            .catch(() => navigate("/login"))
            .finally(() => setLoading(false));
    }, [navigate]);

    const handlePasswordChange = (e: React.ChangeEvent<HTMLInputElement>) =>
        setPwForm({ ...pwForm, [e.target.name]: e.target.value });

    const handlePasswordSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setPwSuccess(""); setPwError("");
        if (pwForm.new_password !== pwForm.confirm_password) {
            setPwError(isRTL ? "كلمتا المرور الجديدتان غير متطابقتين" : "Passwords do not match");
            return;
        }
        setPwLoading(true);
        const token = getToken();
        const res = await fetch(`${API_BASE_URL}/accounts/change-password/`, {
            method: "POST",
            headers: { Authorization: `Token ${token}`, "Content-Type": "application/json" },
            body: JSON.stringify({ current_password: pwForm.current_password, new_password: pwForm.new_password }),
        }).catch(() => null);
        setPwLoading(false);
        if (!res) { setPwError(t('common.serverError')); return; }
        if (res.ok) {
            setPwSuccess(isRTL ? "تم تغيير كلمة المرور بنجاح" : "Password changed successfully");
            setPwForm({ current_password: "", new_password: "", confirm_password: "" });
        } else {
            const data = await res.json();
            setPwError(data.error || data.detail || JSON.stringify(data));
        }
    };

    const handlePreferenceSave = async () => {
        setPrefSaving(true); setPrefMessage("");
        const token = getToken();
        const res = await fetch(`${API_BASE_URL}/accounts/me/`, {
            method: "PATCH",
            headers: { Authorization: `Token ${token}`, "Content-Type": "application/json" },
            body: JSON.stringify({ dark_mode_enabled: darkMode }),
        }).catch(() => null);
        setPrefSaving(false);
        if (!res || !res.ok) { setPrefMessage(isRTL ? "فشل حفظ التفضيلات" : "Failed to save preferences"); return; }
        setPrefMessage(t('common.success'));
        setTimeout(() => setPrefMessage(""), 2500);
    };

    const handleLogout = () => {
        clearAuth();
        navigate("/login");
    };

    if (loading) return <div style={{ textAlign: "center", padding: "60px", fontSize: "16px" }}>{t('common.loading')}</div>;
    if (!user) return null;

    const tabStyle = (tab: Tab): React.CSSProperties => ({
        padding: "10px 20px",
        cursor: "pointer",
        border: "none",
        borderBottom: activeTab === tab ? "2px solid #1a73e8" : "2px solid transparent",
        backgroundColor: "transparent",
        color: activeTab === tab ? "#1a73e8" : "#555",
        fontWeight: activeTab === tab ? "bold" : "normal",
        fontSize: "14px",
    });

    const inputStyle: React.CSSProperties = {
        width: "100%", padding: "10px", margin: "6px 0 14px",
        borderRadius: "6px", border: "1px solid #ccc", fontSize: "14px",
        boxSizing: "border-box",
    };

    const roleLabel = user.role === "WRITER"
        ? (isRTL ? "كاتب (مؤلف)" : "Writer")
        : user.role === "READER"
        ? (isRTL ? "قارئ" : "Reader")
        : user.role;
    const genderLabel = user.gender === "male"
        ? (isRTL ? "ذكر" : "Male")
        : user.gender === "female"
        ? (isRTL ? "أنثى" : "Female")
        : user.gender || "—";
    const joinDate = user.date_joined
        ? new Date(user.date_joined).toLocaleDateString(isRTL ? "ar-SA" : "en-US")
        : "—";

    return (
        <div style={{ maxWidth: "600px", margin: "30px auto", padding: "0 20px", direction: isRTL ? "rtl" : "ltr", fontFamily: "sans-serif" }}>
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "20px" }}>
                <h2 style={{ margin: 0 }}>{t('settings.title')}</h2>
                <Link to="/profile/me" style={{ fontSize: "13px", color: "#1a73e8", textDecoration: "none" }}>
                    {isRTL ? '← ' : '→ '}{t('profile.myProfile')}
                </Link>
            </div>

            <div style={{ display: "flex", borderBottom: "1px solid #eee", marginBottom: "24px" }}>
                <button style={tabStyle("info")} onClick={() => setActiveTab("info")}>
                    {isRTL ? "معلومات الحساب" : "Account Info"}
                </button>
                <button style={tabStyle("password")} onClick={() => setActiveTab("password")}>
                    {t('settings.changePassword')}
                </button>
                <button style={tabStyle("preferences")} onClick={() => setActiveTab("preferences")}>
                    {isRTL ? "التفضيلات" : "Preferences"}
                </button>
            </div>

            {activeTab === "info" && (
                <div>
                    <div style={{ backgroundColor: "#f9f9f9", borderRadius: "8px", padding: "20px", marginBottom: "20px" }}>
                        <Row label={isRTL ? "اسم المستخدم" : "Username"} value={user.username} />
                        <Row label={isRTL ? "الاسم الكامل" : "Full Name"} value={`${user.first_name} ${user.last_name}`.trim() || "—"} />
                        <Row label={isRTL ? "البريد الإلكتروني" : "Email"} value={user.email} />
                        <Row label={isRTL ? "نوع الحساب" : "Account Type"} value={roleLabel} />
                        <Row label={isRTL ? "البلد" : "Country"} value={user.country || "—"} />
                        <Row label={isRTL ? "رقم الهاتف" : "Phone"} value={user.phone || "—"} />
                        <Row label={isRTL ? "الجنس" : "Gender"} value={genderLabel} />
                        <Row label={isRTL ? "تاريخ الميلاد" : "Date of Birth"} value={user.date_of_birth || "—"} />
                        <Row label={isRTL ? "تاريخ الانضمام" : "Joined"} value={joinDate} last />
                    </div>
                    <Link to="/profile/edit"
                        style={{ display: "inline-block", padding: "10px 20px", backgroundColor: "#1a73e8", color: "#fff", borderRadius: "6px", textDecoration: "none", fontSize: "14px" }}>
                        {t('profile.editProfile')}
                    </Link>
                </div>
            )}

            {activeTab === "password" && (
                <div>
                    {pwSuccess && <div style={{ padding: "10px", backgroundColor: "#e6f4ea", color: "#34a853", borderRadius: "6px", marginBottom: "16px" }}>{pwSuccess}</div>}
                    {pwError && <div style={{ padding: "10px", backgroundColor: "#fce8e6", color: "#ea4335", borderRadius: "6px", marginBottom: "16px" }}>{pwError}</div>}
                    <form onSubmit={handlePasswordSubmit}>
                        <label style={{ fontSize: "14px" }}>{isRTL ? "كلمة المرور الحالية" : "Current Password"}</label>
                        <input type="password" name="current_password" value={pwForm.current_password}
                            onChange={handlePasswordChange} required style={inputStyle} />
                        <label style={{ fontSize: "14px" }}>{isRTL ? "كلمة المرور الجديدة" : "New Password"}</label>
                        <input type="password" name="new_password" value={pwForm.new_password}
                            onChange={handlePasswordChange} required style={inputStyle} />
                        <label style={{ fontSize: "14px" }}>{isRTL ? "تأكيد كلمة المرور الجديدة" : "Confirm New Password"}</label>
                        <input type="password" name="confirm_password" value={pwForm.confirm_password}
                            onChange={handlePasswordChange} required style={inputStyle} />
                        <button type="submit" disabled={pwLoading}
                            style={{ width: "100%", padding: "11px", backgroundColor: "#1a73e8", color: "#fff", border: "none", borderRadius: "6px", cursor: "pointer", fontSize: "15px", fontWeight: "bold" }}>
                            {pwLoading ? t('common.loading') : t('settings.changePassword')}
                        </button>
                    </form>
                    <div style={{ marginTop: "16px", textAlign: "center" }}>
                        <Link to="/forgot-password" style={{ fontSize: "13px", color: "#1a73e8" }}>{t('login.forgotPassword')}</Link>
                    </div>
                </div>
            )}

            {activeTab === "preferences" && (
                <div>
                    {/* Language Selector */}
                    <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", padding: "14px 0", borderBottom: "1px solid #eee" }}>
                        <div>
                            <div style={{ fontWeight: "bold", fontSize: "14px" }}>{t('settings.language')}</div>
                            <div style={{ fontSize: "12px", color: "#888", marginTop: "2px" }}>
                                {isRTL ? "اختر لغة الواجهة" : "Choose interface language"}
                            </div>
                        </div>
                        <div style={{ display: "flex", gap: "8px" }}>
                            <button
                                onClick={() => i18n.changeLanguage('ar')}
                                style={{
                                    padding: "6px 14px", borderRadius: "6px", cursor: "pointer", fontSize: "13px",
                                    border: isRTL ? "2px solid #1a73e8" : "1px solid #ccc",
                                    backgroundColor: isRTL ? "#e8f0fe" : "#fff",
                                    color: isRTL ? "#1a73e8" : "#333",
                                    fontWeight: isRTL ? "bold" : "normal",
                                }}>
                                {t('settings.arabic')}
                            </button>
                            <button
                                onClick={() => i18n.changeLanguage('en')}
                                style={{
                                    padding: "6px 14px", borderRadius: "6px", cursor: "pointer", fontSize: "13px",
                                    border: !isRTL ? "2px solid #1a73e8" : "1px solid #ccc",
                                    backgroundColor: !isRTL ? "#e8f0fe" : "#fff",
                                    color: !isRTL ? "#1a73e8" : "#333",
                                    fontWeight: !isRTL ? "bold" : "normal",
                                }}>
                                {t('settings.english')}
                            </button>
                        </div>
                    </div>

                    {/* Dark Mode */}
                    <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", padding: "14px 0", borderBottom: "1px solid #eee" }}>
                        <div>
                            <div style={{ fontWeight: "bold", fontSize: "14px" }}>{isRTL ? "الوضع الداكن" : "Dark Mode"}</div>
                            <div style={{ fontSize: "12px", color: "#888", marginTop: "2px" }}>
                                {isRTL ? "تفعيل المظهر الداكن للموقع" : "Enable dark theme"}
                            </div>
                        </div>
                        <label style={{ display: "flex", alignItems: "center", cursor: "pointer", gap: "8px" }}>
                            <input type="checkbox" checked={darkMode} onChange={e => setDarkMode(e.target.checked)}
                                style={{ width: "18px", height: "18px", cursor: "pointer" }} />
                            <span style={{ fontSize: "13px" }}>
                                {darkMode ? (isRTL ? "مفعّل" : "On") : (isRTL ? "معطّل" : "Off")}
                            </span>
                        </label>
                    </div>

                    {prefMessage && <div style={{ marginTop: "12px", padding: "10px", backgroundColor: "#e6f4ea", color: "#34a853", borderRadius: "6px" }}>{prefMessage}</div>}
                    <button onClick={handlePreferenceSave} disabled={prefSaving}
                        style={{ marginTop: "20px", padding: "10px 24px", backgroundColor: "#1a73e8", color: "#fff", border: "none", borderRadius: "6px", cursor: "pointer", fontSize: "14px" }}>
                        {prefSaving ? t('common.loading') : t('common.save')}
                    </button>
                </div>
            )}

            <div style={{ marginTop: "40px", paddingTop: "20px", borderTop: "1px solid #eee", textAlign: "center" }}>
                <button onClick={handleLogout}
                    style={{ padding: "10px 24px", backgroundColor: "transparent", color: "#e74c3c", border: "1px solid #e74c3c", borderRadius: "6px", cursor: "pointer", fontSize: "14px" }}>
                    {t('header.logout')}
                </button>
            </div>
        </div>
    );
};

const Row: FC<{ label: string; value: string; last?: boolean }> = ({ label, value, last }) => (
    <div style={{ display: "flex", justifyContent: "space-between", padding: "10px 0", borderBottom: last ? "none" : "1px solid #eee" }}>
        <span style={{ color: "#666", fontSize: "14px" }}>{label}</span>
        <span style={{ fontWeight: "500", fontSize: "14px" }}>{value}</span>
    </div>
);

export default Accounts;
