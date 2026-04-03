import { type FC, useState } from "react";
import { Link } from "react-router-dom";

interface Story {
  id: number;
  title: string;
  evaluation: number;
  numberOfTimesRead: number;
  isHidden: boolean; // خاصية جديدة للإخفاء
}

const MyProfile: FC = () => {
  const [name] = useState<string>("osama");
  const [followers] = useState<number>(30);
  const [following] = useState<number>(15);

  const [stories, setStories] = useState<Story[]>([
    { id: 1, title: "كين وسيد التنانين", evaluation: 4.5, numberOfTimesRead: 10, isHidden: false },
    { id: 2, title: "ظلال العنقاء", evaluation: 4.0, numberOfTimesRead: 8, isHidden: false },
    { id: 3, title: "سر المدينة المفقودة", evaluation: 3.8, numberOfTimesRead: 12, isHidden: false },
    { id: 4, title: "الرحلة إلى العالم الآخر", evaluation: 4.2, numberOfTimesRead: 15, isHidden: false },
  ]);

  // دالة الحذف
  const deleteStory = (id: number) => {
    setStories(stories.filter(s => s.id !== id));
  };

  // دالة الإخفاء/الإظهار
  const toggleHideStory = (id: number) => {
    setStories(stories.map(s => s.id === id ? { ...s, isHidden: !s.isHidden } : s));
  };

  return (
    <div style={{ padding: "30px 20px", fontFamily: "sans-serif", direction: "rtl", maxWidth: "600px", margin: "0 auto" }}>
      
      {/* رأس الصفحة بدون زر متابعة */}
      <div style={{ textAlign: "center", marginBottom: "30px" }}>
        <h1>{name} (ملفي الشخصي)</h1>
        <div style={{ display: "flex", justifyContent: "center", gap: "20px" }}>
          <Link to="/followers" style={{ textDecoration: "none", color: "#333" }}>
            <strong>{followers}</strong> متابِع
          </Link>
          <Link to="/following" style={{ textDecoration: "none", color: "#333" }}>
            <strong>{following}</strong> متابَع
          </Link>
        </div>``
      </div>

      <hr />

      <h3>قصصي الذاتية</h3>
      <ul style={{ padding: 0 }}>
        {stories.map(story => (
          <li key={story.id} style={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
            padding: "15px",
            marginBottom: "10px",
            backgroundColor: story.isHidden ? "#f0f0f0" : "#fff",
            border: "1px solid #ddd",
            borderRadius: "8px",
            opacity: story.isHidden ? 0.6 : 1
          }}>
            <div>
              <strong style={{ display: "block", textDecoration: story.isHidden ? "line-through" : "none" }}>
                {story.title}
              </strong>
              <small style={{ color: "#888" }}>⭐ {story.evaluation} | 📖 {story.numberOfTimesRead}</small>
            </div>

            <div style={{ display: "flex", gap: "10px" }}>
              <button 
                onClick={() => toggleHideStory(story.id)}
                style={{ cursor: "pointer", border: "none", borderRadius: "5px", padding: "5px 10px", backgroundColor: "#ffc107" }}
              >
                {story.isHidden ? "إظهار" : "إخفاء"}
              </button>
              <button 
                onClick={() => deleteStory(story.id)}
                style={{ cursor: "pointer", border: "none", borderRadius: "5px", padding: "5px 10px", backgroundColor: "#ff4d4d", color: "white" }}
              >
                حذف
              </button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default MyProfile;