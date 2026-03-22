import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

interface Story {
    id: number;
    title: string;
    author: string;
    content: string;
}

const Reading: React.FC = () => {
    const { id } = useParams<{ id: string }>();
    const [story, setStory] = useState<Story | null>(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        if (id) {
            fetch(`/api/v1/stories/stories/${id}/`)
                .then(res => res.json())
                .then(data => {
                    setStory(data);
                    setLoading(false);
                })
                .catch(err => {
                    console.error('Failed to fetch story:', err);
                    setLoading(false);
                });
        }
    }, [id]);

    if (loading) return <div>جاري التحميل...</div>;
    if (!story) return <div>القصة غير موجودة</div>;

    return (
        <div className="reading-page-wrapper" dir="rtl">
            <header className="data-header">
                <h1 className="main-title">{story.title}</h1>
                <h3 className="author-info">
                    <span>المؤلف:</span> {story.author}
                </h3>
            </header>

            <hr className="separator" />

            <article className="storetext">
                <p style={{ whiteSpace: 'pre-line' }}>
                    {story.content}
                </p>
            </article>
        </div>
    );
};

export default Reading;