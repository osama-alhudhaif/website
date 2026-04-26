import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { API_BASE_URL } from '../config/api';

interface Notification {
    id: number;
    notif_type: string;
    notif_type_display: string;
    title: string;
    message: string;
    is_read: boolean;
    related_story_id: number | null;
    sender_username: string | null;
    created_at: string;
}

const NOTIF_ICONS: Record<string, string> = {
    COMMENT: '💬',
    LIKE: '❤️',
    FOLLOW: '👤',
    STORY: '📖',
    SYSTEM: '🔔',
};

const Notifications: React.FC = () => {
    const [notifications, setNotifications] = useState<Notification[]>([]);
    const [loading, setLoading] = useState(true);
    const navigate = useNavigate();
    const token = localStorage.getItem('token');

    useEffect(() => {
        if (!token) { navigate('/login'); return; }
        fetch(`${API_BASE_URL}/accounts/notifications/`, {
            headers: { Authorization: `Token ${token}` },
        })
            .then(r => r.json())
            .then(data => setNotifications(Array.isArray(data) ? data : data.results || []))
            .catch(console.error)
            .finally(() => setLoading(false));
    }, [token, navigate]);

    const markAllRead = async () => {
        if (!token) return;
        await fetch(`${API_BASE_URL}/accounts/notifications/mark-all-read/`, {
            method: 'POST',
            headers: { Authorization: `Token ${token}` },
        });
        setNotifications(prev => prev.map(n => ({ ...n, is_read: true })));
    };

    const markRead = async (id: number) => {
        if (!token) return;
        await fetch(`${API_BASE_URL}/accounts/notifications/${id}/mark-read/`, {
            method: 'POST',
            headers: { Authorization: `Token ${token}` },
        });
        setNotifications(prev => prev.map(n => n.id === id ? { ...n, is_read: true } : n));
    };

    const handleClick = (notif: Notification) => {
        markRead(notif.id);
        if (notif.related_story_id) navigate(`/reading/${notif.related_story_id}`);
    };

    const unreadCount = notifications.filter(n => !n.is_read).length;

    return (
        <div style={{ maxWidth: '700px', margin: '0 auto', padding: '24px 20px', direction: 'rtl' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '24px' }}>
                <div>
                    <h1 style={{ fontSize: '24px', fontWeight: '700', color: '#111', margin: 0 }}>
                        🔔 الإشعارات
                    </h1>
                    {unreadCount > 0 && (
                        <p style={{ color: '#888', fontSize: '13px', margin: '4px 0 0' }}>
                            {unreadCount} إشعار غير مقروء
                        </p>
                    )}
                </div>
                {unreadCount > 0 && (
                    <button
                        onClick={markAllRead}
                        style={{ padding: '8px 16px', backgroundColor: '#f0f4ff', color: '#1a73e8', border: '1px solid #c7d8ff', borderRadius: '8px', cursor: 'pointer', fontSize: '13px', fontWeight: '500' }}
                    >
                        تعليم الكل كمقروء
                    </button>
                )}
            </div>

            {loading ? (
                <div style={{ textAlign: 'center', padding: '60px', color: '#888' }}>جاري التحميل...</div>
            ) : notifications.length === 0 ? (
                <div style={{ textAlign: 'center', padding: '80px 20px' }}>
                    <div style={{ fontSize: '48px', marginBottom: '16px' }}>🔔</div>
                    <p style={{ color: '#888', fontSize: '16px' }}>لا توجد إشعارات حتى الآن</p>
                </div>
            ) : (
                <div>
                    {notifications.map(notif => (
                        <div
                            key={notif.id}
                            onClick={() => handleClick(notif)}
                            style={{
                                display: 'flex', gap: '14px', padding: '16px',
                                backgroundColor: notif.is_read ? '#fff' : '#f0f4ff',
                                border: `1px solid ${notif.is_read ? '#eee' : '#c7d8ff'}`,
                                borderRadius: '10px', marginBottom: '10px',
                                cursor: notif.related_story_id ? 'pointer' : 'default',
                                transition: 'background 0.2s',
                            }}
                        >
                            <div style={{ fontSize: '24px', flexShrink: 0, lineHeight: 1.2 }}>
                                {NOTIF_ICONS[notif.notif_type] || '🔔'}
                            </div>
                            <div style={{ flex: 1 }}>
                                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                                    <p style={{ fontWeight: notif.is_read ? '400' : '600', margin: '0 0 4px', color: '#111', fontSize: '15px' }}>
                                        {notif.title}
                                    </p>
                                    {!notif.is_read && (
                                        <span style={{ width: '8px', height: '8px', borderRadius: '50%', backgroundColor: '#1a73e8', flexShrink: 0, marginTop: '4px' }} />
                                    )}
                                </div>
                                <p style={{ color: '#555', fontSize: '13px', margin: '0 0 6px', lineHeight: '1.5' }}>{notif.message}</p>
                                <div style={{ display: 'flex', gap: '12px', alignItems: 'center' }}>
                                    {notif.sender_username && (
                                        <span style={{ fontSize: '12px', color: '#1a73e8' }}>@{notif.sender_username}</span>
                                    )}
                                    <span style={{ fontSize: '11px', color: '#aaa' }}>
                                        {new Date(notif.created_at).toLocaleString('ar-SA')}
                                    </span>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
};

export default Notifications;
