import React from 'react';

// تحديد أنواع البيانات للمكون (TypeScript Interface)
interface ReadingProps {
    title?: string;
    author?: string;
    content?: string;
}

const Reading: React.FC<ReadingProps> = ({ 
    title = "عنوان القصة الافتراضي", 
    author = "اسم المؤلف", 
    content = "نص القصة سيظهر هنا..." 
}) => {
    return (
        <div className="reading-page-wrapper" dir="rtl">
            <header className="data-header">
                <h1 className="main-title">{title}</h1>
                <h3 className="author-info">
                    <span>المؤلف:</span> {author}
                </h3>
            </header>

            <hr className="separator" />

            <article className="storetext">
                {/* استخدام whiteSpace: 'pre-line' للحفاظ على فواصل الأسطر في النص */}
                <p style={{ whiteSpace: 'pre-line' }}>
                    {content}
                </p>
            </article>
        </div>
    );
};

export default Reading;