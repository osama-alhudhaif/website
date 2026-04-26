import { type FC } from "react"
import "./Cardstore.css"

interface CardstoreProps {
    id?: number
    name?: string
    description?: string
    likes?: number
    views?: number
    rating?: number
    genre?: string
    author?: string
    authorId?: number
    createdAt?: string
}

const GENRE_COLORS: Record<string, string> = {
    'رومانسية': '#e91e8c',
    'romance': '#e91e8c',
    'خيال علمي': '#2196f3',
    'sci-fi': '#2196f3',
    'رعب': '#f44336',
    'horror': '#f44336',
    'مغامرات': '#ff9800',
    'adventure': '#ff9800',
    'تاريخي': '#795548',
    'history': '#795548',
    'فانتازيا': '#9c27b0',
    'fantasy': '#9c27b0',
    'جريمة': '#607d8b',
    'mystery': '#607d8b',
    'حرب': '#455a64',
    'war': '#455a64',
    'دراما': '#00bcd4',
    'drama': '#00bcd4',
}

const getGenreColor = (genre: string) =>
    GENRE_COLORS[genre?.toLowerCase()] || GENRE_COLORS[genre] || '#1a73e8'

const StarRating: FC<{ value: number }> = ({ value }) => (
    <span style={{ color: '#f59e0b', fontSize: '13px', letterSpacing: '1px' }}>
        {[1, 2, 3, 4, 5].map(s => (
            <span key={s} style={{ opacity: s <= Math.round(value) ? 1 : 0.3 }}>★</span>
        ))}
        <span style={{ color: '#888', marginRight: '4px', fontSize: '12px' }}>
            {value > 0 ? value.toFixed(1) : '—'}
        </span>
    </span>
)

const Cardstore: FC<CardstoreProps> = ({
    name = "قصة بدون عنوان",
    description = "",
    likes = 0,
    views = 0,
    rating = 0,
    genre = "",
    author = "",
    createdAt,
}) => {
    const genreColor = getGenreColor(genre)
    const dateStr = createdAt
        ? new Date(createdAt).toLocaleDateString('ar-SA', { year: 'numeric', month: 'short', day: 'numeric' })
        : ''

    return (
        <div className="story-card">
            <div className="story-card__header">
                <div className="story-card__title-row">
                    <h3 className="story-card__title">{name}</h3>
                    {genre && (
                        <span
                            className="story-card__genre"
                            style={{ backgroundColor: genreColor + '18', color: genreColor, borderColor: genreColor + '44' }}
                        >
                            {genre}
                        </span>
                    )}
                </div>
                {author && (
                    <p className="story-card__author">بقلم: {author}</p>
                )}
            </div>

            {description && (
                <p className="story-card__description">{description}</p>
            )}

            <div className="story-card__footer">
                <div className="story-card__stats">
                    <span className="story-card__stat">
                        <span>❤️</span> {likes.toLocaleString('ar-EG')}
                    </span>
                    <span className="story-card__stat">
                        <span>👁</span> {views.toLocaleString('ar-EG')}
                    </span>
                    {rating > 0 && <StarRating value={rating} />}
                </div>
                {dateStr && <span className="story-card__date">{dateStr}</span>}
            </div>
        </div>
    )
}

export default Cardstore
