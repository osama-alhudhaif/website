import { FormEvent, useState } from "react";
import { sendQalamMessage, type QalamSession } from "../api/qalam";

const Qalam = () => {
  const [session, setSession] = useState<QalamSession | null>(null);
  const [message, setMessage] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    if (!message.trim()) return;

    setIsLoading(true);
    setError(null);
    try {
      const next = await sendQalamMessage({
        session_id: session?.id,
        message,
        mode: "chat",
      });
      setSession(next);
      setMessage("");
    } catch (err) {
      setError("تعذر الاتصال بخدمة قلم. تأكد من أن الخوادم تعمل.");
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: 800, margin: "20px auto", padding: 20, direction: "rtl" }}>
      <h1>قلم - مساعد الكتابة</h1>
      <p style={{ color: "#555" }}>
        اكتب فكرة، فقرة، أو سؤال أدبي، وسيقوم قلم بمساعدتك بالاعتماد على نموذج Llama 3 70B عبر خادم Ollama المحلي.
      </p>

      <div
        style={{
          border: "1px solid #ddd",
          borderRadius: 8,
          padding: 16,
          minHeight: 200,
          marginBottom: 16,
          backgroundColor: "#fafafa",
        }}
      >
        {session?.messages.length ? (
          session.messages.map((m) => (
            <div
              key={m.id}
              style={{
                marginBottom: 12,
                textAlign: m.role === "user" ? "right" : "left",
              }}
            >
              <div
                style={{
                  display: "inline-block",
                  padding: "8px 12px",
                  borderRadius: 12,
                  backgroundColor: m.role === "user" ? "#d1ecf1" : "#ffffff",
                  border: "1px solid #ddd",
                }}
              >
                <strong style={{ display: "block", marginBottom: 4 }}>
                  {m.role === "user" ? "أنت" : "قلم"}
                </strong>
                <span>{m.content}</span>
              </div>
            </div>
          ))
        ) : (
          <p style={{ color: "#888" }}>ابدأ المحادثة مع قلم بكتابة أول رسالة أدناه.</p>
        )}
      </div>

      <form onSubmit={handleSubmit}>
        <textarea
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          rows={4}
          style={{ width: "100%", padding: 10, borderRadius: 8, border: "1px solid #ccc" }}
          placeholder="اكتب هنا..."
        />
        {error && (
          <p style={{ color: "red", marginTop: 8 }}>
            {error}
          </p>
        )}
        <button
          type="submit"
          disabled={isLoading}
          style={{
            marginTop: 10,
            padding: "8px 16px",
            borderRadius: 20,
            border: "none",
            backgroundColor: "#3498db",
            color: "#fff",
            cursor: "pointer",
          }}
        >
          {isLoading ? "جارٍ الإرسال..." : "إرسال"}
        </button>
      </form>
    </div>
  );
};

export default Qalam;

