import { type FC, useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useTranslation } from "react-i18next";
import { API_BASE_URL, getToken } from "../config/api";

const EditProfile: FC = () => {
    const navigate = useNavigate();
    const { t } = useTranslation();
    const [form, setForm] = useState({ first_name: "", last_name: "", email: "", country: "", phone: "", gender: "" });
    const [loading, setLoading] = useState(true);
    const [saving, setSaving] = useState(false);
    const [success, setSuccess] = useState("");
    const [error, setError] = useState("");

    useEffect(() => {
        const token = getToken();
        if (!token) { navigate("/login"); return; }
        fetch(`${API_BASE_URL}/accounts/me/`, { headers: { Authorization: `Token ${token}` } })
            .then(r => r.json())
            .then(data => setForm({ first_name: data.first_name || "", last_name: data.last_name || "", email: data.email || "", country: data.country || "", phone: data.phone || "", gender: data.gender || "" }))
            .catch(() => setError(t('profile.loadError')))
            .finally(() => setLoading(false));
    }, [navigate]);

    const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) =>
        setForm({ ...form, [e.target.name]: e.target.value });

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault(); setSaving(true); setError(""); setSuccess("");
        const token = getToken();
        const res = await fetch(`${API_BASE_URL}/accounts/me/`, {
            method: "PATCH",
            headers: { Authorization: `Token ${token}`, "Content-Type": "application/json" },
            body: JSON.stringify(form),
        });
        setSaving(false);
        if (res.ok) { setSuccess(t('profile.saved')); setTimeout(() => navigate("/profile/me"), 1500); }
        else { const data = await res.json(); setError(JSON.stringify(data)); }
    };

    const inputStyle: React.CSSProperties = { width: "100%", padding: "10px", margin: "6px 0 14px", borderRadius: "6px", border: "1px solid #ccc", fontSize: "14px" };

    if (loading) return <div style={{ textAlign: "center", padding: "50px" }}>{t('common.loading')}</div>;

    return (
        <div style={{ padding: "30px", maxWidth: "500px", margin: "0 auto", direction: "rtl" }}>
            <h2>{t('profile.editProfile')}</h2>
            {success && <div style={{ color: "green", marginBottom: "10px" }}>{success}</div>}
            {error && <div style={{ color: "red", marginBottom: "10px" }}>{error}</div>}
            <form onSubmit={handleSubmit}>
                <label>{t('profile.firstName')}</label>
                <input name="first_name" value={form.first_name} onChange={handleChange} style={inputStyle} />
                <label>{t('profile.lastName')}</label>
                <input name="last_name" value={form.last_name} onChange={handleChange} style={inputStyle} />
                <label>{t('profile.email')}</label>
                <input type="email" name="email" value={form.email} onChange={handleChange} style={inputStyle} />
                <label>{t('profile.country')}</label>
                <input name="country" value={form.country} onChange={handleChange} placeholder="e.g. Saudi Arabia" style={inputStyle} />
                <label>{t('profile.phone')}</label>
                <input name="phone" value={form.phone} onChange={handleChange} style={inputStyle} />
                <label>{t('profile.gender')}</label>
                <select name="gender" value={form.gender} onChange={handleChange} style={inputStyle}>
                    <option value="">{t('profile.genderSelect')}</option>
                    <option value="male">{t('profile.genderMale')}</option>
                    <option value="female">{t('profile.genderFemale')}</option>
                </select>
                <div style={{ display: "flex", gap: "10px", marginTop: "10px" }}>
                    <button type="button" onClick={() => navigate("/profile/me")}
                        style={{ flex: 1, padding: "10px", border: "1px solid #ccc", borderRadius: "6px", cursor: "pointer", backgroundColor: "#fff" }}>
                        {t('common.cancel')}
                    </button>
                    <button type="submit" disabled={saving}
                        style={{ flex: 1, padding: "10px", border: "none", borderRadius: "6px", cursor: "pointer", backgroundColor: "#1a73e8", color: "#fff", fontWeight: "bold" }}>
                        {saving ? t('profile.saving') : t('profile.saveChanges')}
                    </button>
                </div>
            </form>
        </div>
    );
};

export default EditProfile;
