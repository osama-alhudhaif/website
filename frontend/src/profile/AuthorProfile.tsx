import { type FC, useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { API_BASE_URL } from "../config/api";

interface AuthorStory { id: number; title: string; genre: string; created_at: string; }
interface AuthorData {
    id: number; username: string; first_name: string; last_name: string;
    country: string | null; stories_count: number; followers_count: number; stories: AuthorStory[];
}

const AuthorProfile: FC = () => {
    const { authorId } = useParams<{ authorId: string }>();
    const navigate = useNavigate();
    const [author, setAuthor] = useState<AuthorData | null>(null);
    const [isFollowing, setIsFollowing] = useState(false);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");
    const [followersCount, setFollowersCount] = useState(0);

    useEffect(() => {
        const token = localStorage.getItem("token");
        if (!token) { navigate("/login"); return; }
        fetch(`${API_BASE_URL}/accounts/authors/${authorId}/`, { headers: { Authorization: `Token ${token}` } })
            .then(res => {
                if (res.status === 403) throw new Error("subscription_required");
                if (!res.ok) throw new Error("not_found");
                return res.json();
            })
            .then(data => { setAuthor(data); setFollowersCount(data.followers_count); })
            .catch(err => setError(err.message === "subscription_required" ? "يجب الاشتراك لرؤية ملف الكاتب" : "الكاتب غير موجود"))
            .finally(() => setLoading(false));
    }, [authorId, navigate]);

    const handleFollowToggle = async () => {
        const token = localStorage.getItem("token");
        if (!token || !author) return;
        if (isFollowing) {
            const res = await fetch(`${API_BASE_URL}/accounts/unfollow/${author.id}/`, { method: "POST", headers: { Authorization: `Token ${token}` } });
            if (res.ok) { setIsFollowing(false); setFollowersCount(p => p - 1); }
        } else {
            const res = await fetch(`${API_BASE_URL}/accounts/follows/`, {
                method: "POST",
                headers: { Authorization: `Token ${token}`, "Content-Type": "application/json" },
                body: JSON.stringify({ following: author.id }),
            });
            if (res.ok) { setIsFollowing(true); setFollowersCount(p => p + 1); }
        }
    };

    if (loading) return <div style={{ textAlign: "center", padding: "50px" }}>جاري التحميل...</div>;
    if (error) return <div style={{ textAlign: "center", padding: "50px", color: "red" }}>{error}</div>;
    if (!author) return null;

    const displayName = author.first_name ? `${author.first_name} ${author.last_name}`.trim() : author.username;

    return (
        <div style={{ padding: "20px", fontFamily: "'Segoe UI', Tahoma, sans-serif", direction: "rtl", maxWidth: "650px", margin: "40px auto", backgroundColor: "#fff", boxShadow: "0 4px 15px rgba(0,0,0,0.1)", borderRadius: "15px" }}>
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", marginBottom: "15px" }}>
                <div>
                    <h1 style={{ margin: 0, fontSize: "1.8em", color: "#222" }}>{displayName}</h1>
                    {author.country && <p style={{ color: "#888", margin: "5px 0" }}>📍 {author.country}</p>}
                    <div style={{ display: "flex", gap: "20px", marginTop: "10px" }}>
                        <span><strong>{followersCount}</strong> متابِع</span>
                        <span><strong>{author.stories_count}</strong> قصة</span>
                    </div>
                </div>
                <button onClick={handleFollowToggle}
                    style={{ padding: "8px 20px", borderRadius: "20px", border: isFollowing ? "1px solid #ccc" : "none", fontWeight: "bold", cursor: "pointer", backgroundColor: isFollowing ? "#fff" : "#1a73e8", color: isFollowing ? "#333" : "#fff" }}>
                    {isFollowing ? "إلغاء المتابعة" : "متابعة"}
                </button>
            </div>

            <hr style={{ border: "0", borderTop: "1px solid #eee", margin: "20px 0" }} />
            <h3>القصص المنشورة</h3>

            {author.stories.length === 0 ? <p style={{ color: "#888" }}>لا توجد قصص منشورة.</p> : (
                <ul style={{ listStyleType: "none", padding: 0 }}>
                    {author.stories.map(story => (
                        <li key={story.id} style={{ marginBottom: "12px", padding: "12px", borderBottom: "1px solid #eee" }}>
                            <a href={`/reading/${story.id}`} style={{ textDecoration: "none", color: "#1a73e8", fontWeight: "bold" }}>{story.title}</a>
                            <div style={{ fontSize: "0.85em", color: "#888", marginTop: "4px" }}>
                                {story.genre} | {new Date(story.created_at).toLocaleDateString('ar-SA')}
                            </div>
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
};

export default AuthorProfile;
