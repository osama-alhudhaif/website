import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './upload-story.css';

const UploadStory = () => {
  const [formData, setFormData] = useState({
    title: '',
    genre: [] as string[],
    description: '',
    status: 'draft'
  });
  const [file, setFile] = useState<File | null>(null);
  const [uploading, setUploading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const navigate = useNavigate();

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    
    if (name === 'genre') {
      const isChecked = (e.target as HTMLInputElement).checked;
      setFormData(prev => ({
        ...prev,
        genre: isChecked 
          ? [...prev.genre, value]
          : prev.genre.filter(g => g !== value)
      }));
    } else {
      setFormData({
        ...formData,
        [name]: value
      });
    }
  };

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      setFile(e.target.files[0]);
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    setSuccess('');
    setUploading(true);

    const formDataToSend = new FormData();
    formDataToSend.append('title', formData.title);
    formDataToSend.append('genre', formData.genre.join(', '));
    formDataToSend.append('description', formData.description);
    formDataToSend.append('status', formData.status);
    
    if (file) {
      formDataToSend.append('file_path', file);
    }

    try {
      const token = localStorage.getItem('token');
      const response = await fetch('http://127.0.0.1:8000/api/v1/stories/stories/', {
        method: 'POST',
        headers: {
          'Authorization': `Token ${token}`,
        },
        body: formDataToSend,
      });

      if (response.ok) {
        setSuccess('تم رفع القصة بنجاح!');
        setTimeout(() => {
          navigate('/profel/MyProfile');
        }, 2000);
      } else {
        const errorData = await response.json();
        setError(errorData.detail || 'فشل رفع القصة');
      }
    } catch (err: unknown) {
      console.error('Upload error:', err);
      setError('حدث خطأ في الاتصال');
    } finally {
      setUploading(false);
    }
  };

  return (
    <div className="upload-story-container">
      <div className="upload-story-header">
        <h1>رفع قصة جديدة</h1>
        <p>شارك قصتك مع القراء</p>
      </div>

      {error && <div className="error-message">{error}</div>}
      {success && <div className="success-message">{success}</div>}

      <form onSubmit={handleSubmit} className="upload-story-form">
        <div className="form-group">
          <label htmlFor="title" className="title-label">عنوان القصة *</label>
          <input
            type="text"
            id="title"
            name="title"
            value={formData.title}
            onChange={handleChange}
            required
            placeholder="أدخل عنوان القصة"
            className="title-input"
          />
        </div>

        <div className="form-group">
          <label htmlFor="file_path" className="file-label">ملف القصة *</label>
          <input
            type="file"
            id="file_path"
            name="file_path"
            onChange={handleFileChange}
            required
            accept=".pdf,.doc,.docx,.txt"
            className="file-input"
          />
          <small className="file-hint">الصيغ المسموح بها: PDF, DOC, DOCX, TXT</small>
        </div>

        <div className="form-group">
          <label className="genre-label">النوع *</label>
          <div className="checkbox-group">
            {['رومانسي', 'خيال علمي', 'غموض', 'تاريخي', 'مغامرات', 'دراما', 'كوميدي', 'رعب', 'أخرى'].map(genre => (
              <label key={genre} className="checkbox-label">
                <input
                  type="checkbox"
                  name="genre"
                  value={genre}
                  checked={formData.genre.includes(genre)}
                  onChange={handleChange}
                  className="genre-checkbox"
                />
                {genre}
              </label>
            ))}
          </div>
        </div>

        <div className="form-group">
          <label htmlFor="status" className="status-label">الحالة</label>
          <select
            id="status"
            name="status"
            value={formData.status}
            onChange={handleChange}
            className="status-select"
          >
            <option value="draft">مسودة</option>
            <option value="published">منشورة</option>
          </select>
        </div>

        <div className="form-group">
          <label htmlFor="description" className="description-label">المقدمة</label>
          <textarea
            id="description"
            name="description"
            value={formData.description}
            onChange={handleChange}
            placeholder="اكتب نبذة عن القصة (لا تتجاوز 300 حرف)"
            rows={3}
            maxLength={300}
            className="description-textarea"
          />
          <small className="description-counter">{formData.description.length}/300 حرف</small>
        </div>

        <div className="form-actions">
          <button
            type="button"
            className="cancel-btn"
            onClick={() => navigate('/profel/MyProfile')}
          >
            إلغاء
          </button>
          <button
            type="submit"
            className="submit-btn"
            disabled={uploading}
          >
            {uploading ? 'جاري الرفع...' : 'رفع القصة'}
          </button>
        </div>
      </form>
    </div>
  );
};

export default UploadStory;