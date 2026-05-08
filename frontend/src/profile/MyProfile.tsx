import { type FC, useState, useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useTranslation } from "react-i18next";
import { API_BASE_URL, getToken } from "../config/api";

interface Story {
    id: number; title: string; average_rating: number | null;
    views_count: number; status: string; genre: string; created_at: string;
}
interface UserProfile {
    id: number; username: string; first_name: string; last_name: string;
    email: string; country: string | null; role: string;
    followers_count: number; following_count: number; has_active_subscription: boolean;
}

const MyProfile: FC = () => {
    const navigate = useNavigate();
    const { t } = useTranslation();
    const [profile, setProfile] = useState<UserProfile | null>(null);
    const [stories, setStories] = useState<Story[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    useEffect(() => {
        const token = getToken();
        if (!token) { navigate("/login"); return; }
        const headers = { Authorization: `Token ${token}` };
        Promise.all([
            fetch(`${API_BASE_URL}/accounts/me/`, { headers }).then(r => r.json()),
            fetch(`${API_BASE_URL}/stories/stories/?my_stories=1`, { headers }).then(r => r.json()),
        ]).then(([profileData, storiesData]) => {
            if (profileData.detail) { localStorage.removeItem("token"); navigate("/login"); return; }
            setProfile(profileData);
            setStories(Array.isArray(storiesData) ? storiesData : storiesData.results || []);
        }).catch(() => setError(t('profile.loadDataError')))
        .finally(() => setLoading(false));
    }, [navigate]);

    const deleteStory = async (id: number) => {
        if (!confirm(t('profile.deleteConfirm'))) return;
        const token = getToken();
        const res = await fetch(`${API_BASE_URL}/stories/stories/${id}/`, {
            method: "DELETE", headers: { Authorization: `Token ${token}` },
        });
        if (res.ok) setStories(stories.filter(s => s.id !== id));
    };

    const toggleStatus = async (story: Story) => {
        const token = getToken();
        const newStatus = story.status === "published" ? "draft" : "published";
        const res = await fetch(`${API_BASE_URL}/stories/stories/${story.id}/`, {
            method: "PATCH",
            headers: { Authorization: `Token ${token}`, "Content-Type": "application/json" },
            body: JSON.stringify({ status: newStatus }),
        });
        if (res.ok) setStories(stories.map(s => s.id === story.id ? { ...s, status: newStatus } : s));
    };

    if (loading) return <div style={{ textAlign: "center", padding: "50px" }}>{t('common.loading')}</div>;
    if (error) return <div style={{ textAlign: "center", padding: "50px", color: "red" }}>{error}</div>;
    if (!profile) return null;

    const displayName = profile.first_name ? `${profile.first_name} ${profile.last_name}`.trim() : profile.username;

    return (
        <div style={{ padding: "30px 20px", fontFamily: "sans-serif", direction: "rtl", maxWidth: "700px", margin: "0 auto" }}>
            <div style={{ textAlign: "center", marginBottom: "30px" }}>
                <h1>{displayName} ({t('profile.myProfile')})</h1>
                <p style={{ color: "#666" }}>{profile.email}</p>
                {profile.country && <p style={{ color: "#888" }}>📍 {profile.country}</p>}
                <div style={{ display: "flex", justifyContent: "center", gap: "20px", marginTop: "10px" }}>
                    <span><strong>{profile.followers_count}</strong> {t('profile.follower')}</span>
                    <span><strong>{profile.following_count}</strong> {t('profile.following')}</span>
                </div>
                <div style={{ marginTop: "12px", display: "flex", justifyContent: "center", gap: "10px" }}>
                    <Link to="/profile/edit" style={{ padding: "8px 16px", backgroundColor: "#1a73e8", color: "#fff", borderRadius: "5px", textDecoration: "none" }}>
                        {t('profile.editAccount')}
                    </Link>
                    <Link to="/upload-story" style={{ padding: "8px 16px", backgroundColor: "#34a853", color: "#fff", borderRadius: "5px", textDecoration: "none" }}>
                        {t('profile.uploadStoryBtn')}
                    </Link>
                </div>
            </div>

            <hr />
            <h3>{t('profile.myStories', { count: stories.length })}</h3>

            {stories.length === 0 ? (
                <p style={{ color: "#888", textAlign: "center" }}>{t('profile.noStoriesYet')}</p>
            ) : (
                <ul style={{ padding: 0 }}>
                    {stories.map(story => (
                        <li key={story.id} style={{
                            display: "flex", justifyContent: "space-between", alignItems: "center",
                            padding: "15px", marginBottom: "10px",
                            backgroundColor: story.status === "draft" ? "#f9f9f9" : "#fff",
                            border: "1px solid #ddd", borderRadius: "8px",
                            opacity: story.status === "draft" ? 0.75 : 1,
                        }}>
                            <div>
                                <strong style={{ display: "block" }}>{story.title}</strong>
                                <small style={{ color: "#888" }}>
                                    ⭐ {story.average_rating?.toFixed(1) ?? "—"} &nbsp;|&nbsp;
                                    👁 {story.views_count} &nbsp;|&nbsp;
                                    {story.status === "published" ? `🟢 ${t('profile.statusPublished')}` : `🟡 ${t('profile.statusDraft')}`}
                                </small>
                            </div>
                            <div style={{ display: "flex", gap: "8px" }}>
                                <button onClick={() => toggleStatus(story)}
                                    style={{ cursor: "pointer", border: "none", borderRadius: "5px", padding: "5px 10px", backgroundColor: "#ffc107" }}>
                                    {story.status === "published" ? t('profile.hide') : t('profile.publish')}
                                </button>
                                <button onClick={() => deleteStory(story.id)}
                                    style={{ cursor: "pointer", border: "none", borderRadius: "5px", padding: "5px 10px", backgroundColor: "#ff4d4d", color: "white" }}>
                                    {t('common.delete')}
                                </button>
                            </div>
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
};

export default MyProfile;
