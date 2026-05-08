import React, { useEffect, useState, useRef } from 'react';
import { useParams, Link } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { API_BASE_URL, getToken, getUserId } from '../config/api';

interface Story {
    id: number; title: string; description: string;
    author: number; author_username: string;
    file_path: string; file_name: string;
    genre: string; language: string | null;
    views_count: number; average_rating: number;
    ratings_count: number; comments_count: number; created_at: string;
}
interface Comment { id: number; user: number; user_username: string; content: string; created_at: string; }

const getExt = (filename: string) => filename?.split('.').pop()?.toLowerCase() || '';

const Reading: React.FC = () => {
    const { id } = useParams<{ id: string }>();
    const { t } = useTranslation();
    const [story, setStory] = useState<Story | null>(null);
    const [fileContent, setFileContent] = useState<string | null>(null);
    const [comments, setComments] = useState<Comment[]>([]);
    const [newComment, setNewComment] = useState('');
    const [userRating, setUserRating] = useState(0);
    const [loading, setLoading] = useState(true);
    const [commentLoading, setCommentLoading] = useState(false);
    const [selectedText, setSelectedText] = useState('');
    const [translatedText, setTranslatedText] = useState('');
    const [translateLoading, setTranslateLoading] = useState(false);
    const [targetLang, setTargetLang] = useState('en');
    const [showTranslateBar, setShowTranslateBar] = useState(false);
    const [isLiked, setIsLiked] = useState(false);
    const [likesCount, setLikesCount] = useState(0);
    const [likeLoading, setLikeLoading] = useState(false);
    const [editingCommentId, setEditingCommentId] = useState<number | null>(null);
    const [editContent, setEditContent] = useState('');
    const token = getToken();
    const currentUserId = getUserId();
    const translateTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null);

    useEffect(() => {
        if (!id) return;
        const headers: Record<string, string> = token ? { Authorization: `Token ${token}` } : {};
        const likeHeaders: Record<string, string> = token ? { Authorization: `Token ${token}` } : {};
        Promise.all([
            fetch(`${API_BASE_URL}/stories/stories/${id}/`, { headers }).then(r => r.json()),
            fetch(`${API_BASE_URL}/stories/stories/${id}/comments/`, { headers }).then(r => r.json()),
            token ? fetch(`${API_BASE_URL}/stories/stories/${id}/is_liked/`, { headers: likeHeaders }).then(r => r.json()).catch(() => ({ liked: false })) : Promise.resolve({ liked: false }),
        ]).then(([storyData, commentsData, likeData]) => {
            setStory(storyData);
            setLikesCount(storyData.likes_count || 0);
            setIsLiked(likeData.liked || false);
            setComments(Array.isArray(commentsData) ? commentsData : commentsData.results || []);
            const ext = getExt(storyData.file_name || storyData.file_path);
            if (ext === 'txt' && storyData.file_path) {
                return fetch(storyData.file_path, { headers }).then(r => r.text());
            }
            return null;
        }).then(text => { if (text) setFileContent(text); })
        .catch(console.error)
        .finally(() => setLoading(false));
    }, [id, token]);

    const submitComment = async () => {
        if (!newComment.trim() || !token) return;
        setCommentLoading(true);
        const res = await fetch(`${API_BASE_URL}/stories/stories/${id}/comments/`, {
            method: 'POST',
            headers: { Authorization: `Token ${token}`, 'Content-Type': 'application/json' },
            body: JSON.stringify({ content: newComment }),
        });
        if (res.ok) { const data = await res.json(); setComments([data, ...comments]); setNewComment(''); }
        setCommentLoading(false);
    };

    const translateText = async (text: string, lang: string) => {
        if (!text || !token) return;
        setTranslateLoading(true);
        const res = await fetch(`${API_BASE_URL}/stories/translate/`, {
            method: 'POST',
            headers: { Authorization: `Token ${token}`, 'Content-Type': 'application/json' },
            body: JSON.stringify({ text, source_lang: 'ar', target_lang: lang }),
        }).catch(() => null);
        setTranslateLoading(false);
        if (!res) return;
        const data = await res.json();
        if (data.translated_text) setTranslatedText(data.translated_text);
    };

    const handleTextSelection = () => {
        const text = window.getSelection()?.toString().trim();
        if (text && text.length > 2) {
            setSelectedText(text);
            setTranslatedText('');
            setShowTranslateBar(true);
            if (translateTimerRef.current) clearTimeout(translateTimerRef.current);
            translateTimerRef.current = setTimeout(() => translateText(text, targetLang), 600);
        }
    };

    const deleteComment = async (commentId: number) => {
        if (!token || !window.confirm(t('reading.deleteCommentConfirm'))) return;
        const res = await fetch(`${API_BASE_URL}/stories/comments/${commentId}/`, {
            method: 'DELETE',
            headers: { Authorization: `Token ${token}` },
        }).catch(() => null);
        if (res && res.ok) setComments(prev => prev.filter(c => c.id !== commentId));
    };

    const startEditComment = (comment: Comment) => {
        setEditingCommentId(comment.id);
        setEditContent(comment.content);
    };

    const saveEditComment = async (commentId: number) => {
        if (!token || !editContent.trim()) return;
        const res = await fetch(`${API_BASE_URL}/stories/comments/${commentId}/`, {
            method: 'PATCH',
            headers: { Authorization: `Token ${token}`, 'Content-Type': 'application/json' },
            body: JSON.stringify({ content: editContent }),
        }).catch(() => null);
        if (res && res.ok) {
            const updated = await res.json();
            setComments(prev => prev.map(c => c.id === commentId ? { ...c, content: updated.content } : c));
            setEditingCommentId(null);
        }
    };

    const toggleLike = async () => {
        if (!token || likeLoading) return;
        setLikeLoading(true);
        const res = await fetch(`${API_BASE_URL}/stories/stories/${id}/like/`, {
            method: 'POST',
            headers: { Authorization: `Token ${token}`, 'Content-Type': 'application/json' },
        }).catch(() => null);
        setLikeLoading(false);
        if (!res) return;
        const data = await res.json();
        setIsLiked(data.liked);
        setLikesCount(data.likes_count);
    };

    const submitRating = async (value: number) => {
        if (!token) return;
        setUserRating(value);
        await fetch(`${API_BASE_URL}/stories/stories/${id}/ratings/`, {
            method: 'POST',
            headers: { Authorization: `Token ${token}`, 'Content-Type': 'application/json' },
            body: JSON.stringify({ rating: value }),
        });
    };

    if (loading) return <div style={{ textAlign: 'center', padding: '60px' }}>{t('common.loading')}</div>;
    if (!story) return <div style={{ textAlign: 'center', padding: '60px' }}>{t('reading.storyNotFound')}</div>;

    const ext = getExt(story.file_name || story.file_path);

    const renderContent = () => {
        if (ext === 'txt' && fileContent)
            return <article style={{ lineHeight: '2', fontSize: '17px', whiteSpace: 'pre-wrap', color: '#333' }}>{fileContent}</article>;
        if (ext === 'pdf' && story.file_path)
            return <embed src={story.file_path} type="application/pdf" width="100%" height="700px" style={{ border: '1px solid #ddd', borderRadius: '8px' }} />;
        if (['doc', 'docx'].includes(ext) && story.file_path)
            return (
                <div style={{ textAlign: 'center', padding: '40px', backgroundColor: '#f5f5f5', borderRadius: '8px' }}>
                    <p>{t('reading.cannotDisplay')}</p>
                    <a href={story.file_path} download style={{ padding: '10px 20px', backgroundColor: '#1a73e8', color: '#fff', borderRadius: '6px', textDecoration: 'none' }}>{t('reading.downloadFile')}</a>
                </div>
            );
        if (story.description)
            return <article style={{ lineHeight: '2', fontSize: '17px', color: '#333' }}>{story.description}</article>;
        return <p style={{ color: '#888' }}>{t('reading.noContent')}</p>;
    };

    return (
        <div style={{ maxWidth: '800px', margin: '0 auto', padding: '20px', direction: 'rtl', fontFamily: "'Segoe UI', Tahoma, sans-serif" }} onMouseUp={handleTextSelection}>
            <header style={{ marginBottom: '24px' }}>
                <h1 style={{ fontSize: '2em', color: '#111', marginBottom: '8px' }}>{story.title}</h1>
                <div style={{ color: '#666', fontSize: '14px', display: 'flex', gap: '16px', flexWrap: 'wrap' }}>
                    <span>{t('reading.by')}: <Link to={`/profile/author/${story.author}`} style={{ color: '#1a73e8', textDecoration: 'none' }}>{story.author_username}</Link></span>
                    {story.genre && <span>📚 {story.genre}</span>}
                    <span>👁 {story.views_count} {t('reading.views')}</span>
                    <span>⭐ {story.average_rating?.toFixed(1) ?? '—'} ({story.ratings_count} {t('reading.rating')})</span>
                    <span>{new Date(story.created_at).toLocaleDateString('ar-SA')}</span>
                </div>
            </header>

            {/* زر اللايك */}
            {token && (
                <div style={{ display: 'flex', gap: '10px', marginBottom: '16px' }}>
                    <button
                        onClick={toggleLike}
                        disabled={likeLoading}
                        style={{
                            display: 'flex', alignItems: 'center', gap: '6px',
                            padding: '8px 18px', borderRadius: '24px', cursor: 'pointer',
                            backgroundColor: isLiked ? '#fee2e2' : '#f5f5f5',
                            border: `1.5px solid ${isLiked ? '#f87171' : '#ddd'}`,
                            color: isLiked ? '#e53e3e' : '#555',
                            fontWeight: isLiked ? '600' : '400',
                            transition: 'all 0.2s', fontSize: '14px',
                        }}
                    >
                        {isLiked ? '❤️' : '🤍'} {t('reading.likesCount', { count: likesCount })}
                    </button>
                </div>
            )}

            {story.description && (
                <div style={{ backgroundColor: '#f8f8f8', padding: '12px 16px', borderRight: '4px solid #1a73e8', marginBottom: '24px', borderRadius: '4px', color: '#555' }}>
                    {story.description}
                </div>
            )}

            <hr style={{ margin: '16px 0', border: '0', borderTop: '1px solid #eee' }} />
            <div style={{ marginBottom: '40px' }}>{renderContent()}</div>

            {/* شريط الترجمة */}
            {token && showTranslateBar && (
                <div style={{ position: 'sticky', bottom: '16px', backgroundColor: '#fff', border: '1px solid #ddd', borderRadius: '12px', padding: '16px', boxShadow: '0 4px 20px rgba(0,0,0,0.15)', marginBottom: '20px', zIndex: 100 }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '10px' }}>
                        <strong style={{ fontSize: '14px' }}>🌐 {t('reading.translateBarTitle')}</strong>
                        <button onClick={() => setShowTranslateBar(false)} style={{ border: 'none', background: 'none', cursor: 'pointer', fontSize: '18px', color: '#999' }}>✕</button>
                    </div>
                    <div style={{ backgroundColor: '#f5f5f5', padding: '8px 12px', borderRadius: '6px', marginBottom: '10px', fontSize: '14px', color: '#555', maxHeight: '80px', overflow: 'auto' }}>
                        {selectedText}
                    </div>
                    <div style={{ display: 'flex', gap: '8px', marginBottom: '10px' }}>
                        <select value={targetLang} onChange={(e) => { setTargetLang(e.target.value); if (selectedText) translateText(selectedText, e.target.value); }}
                            style={{ padding: '6px 10px', borderRadius: '6px', border: '1px solid #ddd', fontSize: '13px' }}>
                            <option value="en">{t('reading.langEn')}</option>
                            <option value="ar">{t('reading.langAr')}</option>
                            <option value="fr">{t('reading.langFr')}</option>
                            <option value="de">{t('reading.langDe')}</option>
                            <option value="es">{t('reading.langEs')}</option>
                            <option value="tr">{t('reading.langTr')}</option>
                            <option value="zh">{t('reading.langZh')}</option>
                            <option value="ru">{t('reading.langRu')}</option>
                            <option value="ja">{t('reading.langJa')}</option>
                        </select>
                        <button onClick={() => translateText(selectedText, targetLang)} disabled={translateLoading}
                            style={{ padding: '6px 16px', backgroundColor: '#1a73e8', color: '#fff', border: 'none', borderRadius: '6px', cursor: 'pointer', fontSize: '13px' }}>
                            {translateLoading ? '...' : t('reading.retranslate')}
                        </button>
                    </div>
                    {translatedText && (
                        <div style={{ backgroundColor: '#e8f0fe', padding: '10px 12px', borderRadius: '6px', fontSize: '14px', color: '#1a73e8' }}>
                            {translatedText}
                        </div>
                    )}
                </div>
            )}

            {/* التقييم */}
            {token && (
                <div style={{ marginBottom: '30px', padding: '16px', backgroundColor: '#fafafa', borderRadius: '8px', border: '1px solid #eee' }}>
                    <p style={{ marginBottom: '8px', fontWeight: 'bold' }}>{t('reading.rateStory')}</p>
                    <div style={{ display: 'flex', gap: '6px' }}>
                        {[1, 2, 3, 4, 5].map(star => (
                            <button key={star} onClick={() => submitRating(star)}
                                style={{ fontSize: '24px', background: 'none', border: 'none', cursor: 'pointer', color: star <= userRating ? '#f59e0b' : '#ccc' }}>★</button>
                        ))}
                    </div>
                </div>
            )}

            {/* التعليقات */}
            <div>
                <h3 style={{ marginBottom: '16px' }}>{t('reading.comments', { count: comments.length })}</h3>
                {token ? (
                    <div style={{ marginBottom: '20px' }}>
                        <textarea value={newComment} onChange={(e) => setNewComment(e.target.value)}
                            placeholder={t('reading.addComment')} rows={3}
                            style={{ width: '100%', padding: '10px', borderRadius: '6px', border: '1px solid #ddd', resize: 'vertical', fontSize: '14px' }} />
                        <button onClick={submitComment} disabled={commentLoading || !newComment.trim()}
                            style={{ marginTop: '8px', padding: '8px 20px', backgroundColor: '#1a73e8', color: '#fff', border: 'none', borderRadius: '6px', cursor: 'pointer' }}>
                            {commentLoading ? t('reading.sending') : t('reading.sendComment')}
                        </button>
                    </div>
                ) : (
                    <p style={{ color: '#888', marginBottom: '16px' }}>
                        <Link to="/login" style={{ color: '#1a73e8' }}>{t('header.login')}</Link> {t('reading.loginToComment')}
                    </p>
                )}
                {comments.length === 0 ? <p style={{ color: '#aaa' }}>{t('reading.noComments')}</p> : (
                    comments.map(c => (
                        <div key={c.id} style={{ padding: '12px', marginBottom: '10px', backgroundColor: '#f9f9f9', borderRadius: '8px', border: '1px solid #eee' }}>
                            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '6px' }}>
                                <span style={{ fontWeight: 'bold' }}>{c.user_username}</span>
                                {currentUserId === c.user && editingCommentId !== c.id && (
                                    <div style={{ display: 'flex', gap: '6px' }}>
                                        <button onClick={() => startEditComment(c)}
                                            style={{ padding: '3px 10px', fontSize: '12px', border: '1px solid #1a73e8', borderRadius: '4px', background: 'none', color: '#1a73e8', cursor: 'pointer' }}>
                                            {t('common.edit')}
                                        </button>
                                        <button onClick={() => deleteComment(c.id)}
                                            style={{ padding: '3px 10px', fontSize: '12px', border: '1px solid #e74c3c', borderRadius: '4px', background: 'none', color: '#e74c3c', cursor: 'pointer' }}>
                                            {t('common.delete')}
                                        </button>
                                    </div>
                                )}
                            </div>
                            {editingCommentId === c.id ? (
                                <div>
                                    <textarea value={editContent} onChange={(e) => setEditContent(e.target.value)} rows={3}
                                        style={{ width: '100%', padding: '8px', borderRadius: '6px', border: '1px solid #ddd', fontSize: '14px', resize: 'vertical' }} />
                                    <div style={{ display: 'flex', gap: '8px', marginTop: '6px' }}>
                                        <button onClick={() => saveEditComment(c.id)}
                                            style={{ padding: '5px 14px', backgroundColor: '#1a73e8', color: '#fff', border: 'none', borderRadius: '4px', cursor: 'pointer', fontSize: '13px' }}>
                                            {t('common.save')}
                                        </button>
                                        <button onClick={() => setEditingCommentId(null)}
                                            style={{ padding: '5px 14px', border: '1px solid #ccc', borderRadius: '4px', cursor: 'pointer', fontSize: '13px', background: '#fff' }}>
                                            {t('common.cancel')}
                                        </button>
                                    </div>
                                </div>
                            ) : (
                                <p style={{ margin: 0, color: '#555', lineHeight: '1.6' }}>{c.content}</p>
                            )}
                            <small style={{ color: '#aaa' }}>{new Date(c.created_at).toLocaleDateString('ar-SA')}</small>
                        </div>
                    ))
                )}
            </div>
        </div>
    );
};

export default Reading;
