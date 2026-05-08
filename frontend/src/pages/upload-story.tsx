import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { API_BASE_URL, getToken } from '../config/api';
import './upload-story.css';

const UploadStory = () => {
  const { t } = useTranslation();
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
      const token = getToken();
      const response = await fetch(`${API_BASE_URL}/stories/stories/`, {
        method: 'POST',
        headers: {
          'Authorization': `Token ${token}`,
        },
        body: formDataToSend,
      });

      if (response.ok) {
        setSuccess(t('uploadStory.successMessage'));
        setTimeout(() => {
          navigate('/profel/MyProfile');
        }, 2000);
      } else {
        const errorData = await response.json();
        setError(errorData.detail || t('uploadStory.failMessage'));
      }
    } catch (err: unknown) {
      console.error('Upload error:', err);
      setError(t('uploadStory.connectionError'));
    } finally {
      setUploading(false);
    }
  };

  return (
    <div className="upload-story-container">
      <div className="upload-story-header">
        <h1>{t('uploadStory.pageTitle')}</h1>
        <p>{t('uploadStory.pageSubtitle')}</p>
      </div>

      {error && <div className="error-message">{error}</div>}
      {success && <div className="success-message">{success}</div>}

      <form onSubmit={handleSubmit} className="upload-story-form">
        <div className="form-group">
          <label htmlFor="title" className="title-label">{t('uploadStory.storyTitle')} *</label>
          <input
            type="text"
            id="title"
            name="title"
            value={formData.title}
            onChange={handleChange}
            required
            placeholder={t('uploadStory.titlePlaceholder')}
            className="title-input"
          />
        </div>

        <div className="form-group">
          <label htmlFor="file_path" className="file-label">{t('uploadStory.storyFile')} *</label>
          <input
            type="file"
            id="file_path"
            name="file_path"
            onChange={handleFileChange}
            required
            accept=".pdf,.doc,.docx,.txt"
            className="file-input"
          />
          <small className="file-hint">{t('uploadStory.allowedFormats')}</small>
        </div>

        <div className="form-group">
          <label className="genre-label">{t('uploadStory.genre')} *</label>
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
          <label htmlFor="status" className="status-label">{t('uploadStory.status')}</label>
          <select
            id="status"
            name="status"
            value={formData.status}
            onChange={handleChange}
            className="status-select"
          >
            <option value="draft">{t('uploadStory.draft')}</option>
            <option value="published">{t('uploadStory.published')}</option>
          </select>
        </div>

        <div className="form-group">
          <label htmlFor="description" className="description-label">{t('uploadStory.intro')}</label>
          <textarea
            id="description"
            name="description"
            value={formData.description}
            onChange={handleChange}
            placeholder={t('uploadStory.introPlaceholder')}
            rows={3}
            maxLength={300}
            className="description-textarea"
          />
          <small className="description-counter">{t('uploadStory.charCount', { count: formData.description.length })}</small>
        </div>

        <div className="form-actions">
          <button
            type="button"
            className="cancel-btn"
            onClick={() => navigate('/profel/MyProfile')}
          >
            {t('common.cancel')}
          </button>
          <button
            type="submit"
            className="submit-btn"
            disabled={uploading}
          >
            {uploading ? t('uploadStory.uploading') : t('uploadStory.submit')}
          </button>
        </div>
      </form>
    </div>
  );
};

export default UploadStory;