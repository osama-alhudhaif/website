import React, { useState, type ChangeEvent, type FormEvent } from 'react';
import { Mail, Twitter, Send } from 'lucide-react';
import './Contact.css';

// تعريف أنواع البيانات للمدخلات
interface ContactFormData {
  name: string;
  email: string;
  message: string;
}

const Contact: React.FC = () => {
  const [formData, setFormData] = useState<ContactFormData>({
    name: '',
    email: '',
    message: '',
  });

  const [status, setStatus] = useState<string>('');

  const handleChange = (e: ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();
    // هنا يمكنك ربط النموذج بـ API أو EmailJS
    console.log('بيانات النموذج:', formData);
    setStatus('تم إرسال رسالتك بنجاح!');
    setFormData({ name: '', email: '', message: '' });
  };

  return (
    <section className="contact-section">
      <div className="contact-container">
        <header className="contact-header">
          <h2>تواصل معي</h2>
          <p>يسعدني دائماً استقبال رسائلكم واستفساراتكم.</p>
        </header>

        <div className="contact-grid">
          {/* معلومات التواصل */}
          <aside className="contact-sidebar">
            <div className="info-card">
              <Mail className="icon" />
              <div>
                <h4>البريد الإلكتروني</h4>
                <p>osama@oda.com</p>
              </div>
            </div>
            <div className="info-card">
            </div>
            <div className="info-card">
              <Twitter className="icon" />
              <div>
                <h4>تويتر</h4>
                <p>@oda</p>
              </div>
            </div>
          </aside>

          {/* نموذج التواصل */}
          <main className="contact-main">
            <form onSubmit={handleSubmit} className="contact-form">
              <div className="input-group">
                <input
                  type="text"
                  name="name"
                  placeholder="الاسم الكامل"
                  value={formData.name}
                  onChange={handleChange}
                  required
                />
              </div>
              <div className="input-group">
                <input
                  type="email"
                  name="email"
                  placeholder="البريد الإلكتروني"
                  value={formData.email}
                  onChange={handleChange}
                  required
                />
              </div>
              <div className="input-group">
                <textarea
                  name="message"
                  placeholder="كيف يمكنني مساعدتك؟"
                  rows={5}
                  value={formData.message}
                  onChange={handleChange}
                  required
                ></textarea>
              </div>
              <button type="submit" className="submit-btn">
                <span>إرسال</span>
                <Send size={18} />
              </button>
              {status && <p className="status-msg">{status}</p>}
            </form>
          </main>
        </div>
      </div>
    </section>
  );
};

export default Contact;