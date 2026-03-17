import { type FC, useState } from "react";
import { Link } from "react-router-dom";

// 1) تعريف نوع القصة
interface Story {
  id: number;
  title: string;
  evaluation: number;
  numberOfTimesRead: number;
}

// 2) مكوّن عنصر القصة
interface StoryItemProps extends Story {
  authorName: string;
}

const StoryItem: FC<StoryItemProps> = ({
  id,
  title,
  evaluation,
  numberOfTimesRead,
  authorName,
}) => {
  return (
    <li
      style={{
        marginBottom: "15px",
        padding: "15px",
        borderBottom: "1px solid #eee",
        borderRadius: "8px",
      }}
    >
      <div style={{ fontWeight: "bold", fontSize: "1.1em" }}>
        <span style={{ color: "#888", marginLeft: "8px" }}>{id}-</span>
        <a 
          href={`/${encodeURIComponent(authorName)}/${encodeURIComponent(title)}`} 
          style={{ textDecoration: "none", color: "#1a73e8" }}
        >
          {title}
        </a>
      </div>
      <div style={{ fontSize: "0.9em", color: "#666", marginTop: "8px", display: "flex", gap: "20px" }}>
        <span>⭐ {evaluation}</span>
        <span>📖 {numberOfTimesRead} قراءة</span>
      </div>
    </li>
  );
};

// 3) المكون الرئيسي AuthorProfile
const AuthorProfile: FC = () => {
  const [name] = useState<string>("osama");
  const [followers, setFollowers] = useState<number>(30); // من يتابعونك
  const [following] = useState<number>(15);              // من تتابعهم أنت
  const [isFollowing, setIsFollowing] = useState<boolean>(false);

  const [stories] = useState<Story[]>([
    { id: 1, title: "كين وسيد التنانين", evaluation: 4.5, numberOfTimesRead: 10 },
    { id: 2, title: "ظلال العنقاء", evaluation: 4.0, numberOfTimesRead: 8 },
  ]);

  const handleFollowClick = () => {
    if (isFollowing) {
      setFollowers(prev => prev - 1);
    } else {
      setFollowers(prev => prev + 1);
    }
    setIsFollowing(!isFollowing);
  };

  // تنسيق مشترك للروابط (Followers & Following)
  const statsLinkStyle = {
    textDecoration: "none",
    color: "#555",
    fontSize: "0.95em",
    transition: "color 0.2s"
  };

  return (
    <div style={{ 
      padding: "20px", 
      fontFamily: "'Segoe UI', Tahoma, sans-serif", 
      direction: "rtl", 
      maxWidth: "600px", 
      margin: "40px auto",
      backgroundColor: "#fff",
      boxShadow: "0 4px 15px rgba(0,0,0,0.1)",
      borderRadius: "15px"
    }}>
      
      {/* قسم الهوية وزر المتابعة */}
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", marginBottom: "15px" }}>
        <div>
          <h1 style={{ margin: 0, fontSize: "1.8em", color: "#222" }}>{name}</h1>
          
          {/* قسم الروابط (المتابعين والمتابَعين) */}
          <div style={{ display: "flex", gap: "20px", marginTop: "10px" }}>
            <Link
              to={`/${name}/followers`}
              style={statsLinkStyle as React.CSSProperties}
              onMouseOver={(e) => (e.currentTarget.style.color = "#000")}
              onMouseOut={(e) => (e.currentTarget.style.color = "#555")}
            >
              <strong>{followers}</strong> متابِع
            </Link>
            
            <Link
              to={`/${name}/following`}
              style={statsLinkStyle as React.CSSProperties}
              onMouseOver={(e) => (e.currentTarget.style.color = "#000")}
              onMouseOut={(e) => (e.currentTarget.style.color = "#555")}
            >
              <strong>{following}</strong> متابَع
            </Link>
          </div>
        </div>

        <button 
          onClick={handleFollowClick}
          style={{
            padding: "8px 20px",
            borderRadius: "20px",
            border: isFollowing ? "1px solid #ccc" : "none",
            fontWeight: "bold",
            cursor: "pointer",
            backgroundColor: isFollowing ? "#fff" : "#1a73e8",
            color: isFollowing ? "#333" : "#fff",
          }}
        >
          {isFollowing ? "إلغاء المتابعة" : "متابعة"}
        </button>
      </div>

      <div style={{ marginBottom: "20px", color: "#777", fontSize: "0.9em" }}>
        <strong>📚 عدد القصص:</strong> {stories.length}
      </div>

      <hr style={{ border: "0", borderTop: "1px solid #eee", margin: "20px 0" }} />

      <h3 style={{ color: "#333" }}>القصص المنشورة</h3>
      <ul style={{ listStyleType: "none", padding: 0 }}>
        {stories.map((story) => (
          <StoryItem key={story.id} {...story} authorName={name} />
        ))}
      </ul>
    </div>
  );
};

export default AuthorProfile;