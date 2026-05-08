import { useState, useEffect, useCallback } from "react"
import { Link, useParams } from "react-router-dom"
import { useTranslation } from "react-i18next"
import Cardstore from "./Cardstore"
import { API_BASE_URL, getToken } from "../config/api"

interface Story {
    id: number
    title: string
    description: string
    author: number
    author_username: string
    genre: string
    views_count: number
    average_rating: number | null
    likes_count: number
    created_at: string
}

const Body = () => {
    const { categoryName } = useParams<{ categoryName?: string }>()
    const { t, i18n } = useTranslation()
    const isRTL = i18n.language === 'ar' || i18n.language.startsWith('ar')
    const [stories, setStories] = useState<Story[]>([])
    const [loading, setLoading] = useState(true)
    const [search, setSearch] = useState("")
    const [searchInput, setSearchInput] = useState("")
    const [page, setPage] = useState(1)
    const [totalPages, setTotalPages] = useState(1)
    const [totalCount, setTotalCount] = useState(0)

    const fetchStories = useCallback(() => {
        const token = getToken()
        setLoading(true)
        const params = new URLSearchParams()
        params.set("page", String(page))
        if (search) params.set("search", search)
        if (categoryName) params.set("genre", categoryName)

        const headers: Record<string, string> = {}
        if (token) headers["Authorization"] = `Token ${token}`

        fetch(`${API_BASE_URL}/stories/stories/?${params.toString()}`, { headers })
            .then((res) => res.json())
            .then((data) => {
                if (Array.isArray(data)) {
                    setStories(data); setTotalPages(1); setTotalCount(data.length)
                } else {
                    setStories(data.results || [])
                    const count = data.count || 0
                    setTotalCount(count)
                    setTotalPages(Math.ceil(count / 20))
                }
            })
            .catch((err) => console.error("Failed to fetch stories:", err))
            .finally(() => setLoading(false))
    }, [page, search, categoryName])

    useEffect(() => { fetchStories() }, [fetchStories])
    useEffect(() => { setPage(1) }, [categoryName])

    const handleSearch = (e: React.FormEvent) => {
        e.preventDefault(); setPage(1); setSearch(searchInput)
    }

    return (
        <div style={{ padding: "20px", maxWidth: "900px", margin: "0 auto", direction: isRTL ? "rtl" : "ltr" }}>
            <form onSubmit={handleSearch} style={{ display: "flex", gap: "8px", marginBottom: "24px" }}>
                <input
                    type="text" value={searchInput} onChange={(e) => setSearchInput(e.target.value)}
                    placeholder={t('body.searchPlaceholder')}
                    style={{ flex: 1, padding: "10px 14px", borderRadius: "8px", border: "1px solid #ddd", fontSize: "15px" }}
                />
                <button type="submit" style={{ padding: "10px 20px", backgroundColor: "#1a73e8", color: "#fff", border: "none", borderRadius: "8px", cursor: "pointer" }}>
                    {t('body.search')}
                </button>
                {search && (
                    <button type="button" onClick={() => { setSearch(""); setSearchInput(""); setPage(1); }}
                        style={{ padding: "10px 14px", border: "1px solid #ddd", borderRadius: "8px", cursor: "pointer", backgroundColor: "#fff" }}>
                        ✕
                    </button>
                )}
            </form>

            {categoryName && <h2 style={{ marginBottom: "16px" }}>{t('body.category')}: {categoryName}</h2>}
            {search && (
                <p style={{ color: "#666", marginBottom: "12px" }}>
                    {t('body.searchResults', { query: search, count: totalCount })}
                </p>
            )}

            {loading ? (
                <div style={{ textAlign: "center", padding: "40px", color: "#888" }}>{t('common.loading')}</div>
            ) : stories.length === 0 ? (
                <div style={{ textAlign: "center", padding: "40px", color: "#888" }}>{t('body.noStories')}</div>
            ) : (
                <>
                    {stories.map((story) => (
                        <Link key={story.id} to={`/reading/${story.id}`} style={{ textDecoration: "none", color: "inherit" }}>
                            <Cardstore
                                id={story.id}
                                name={story.title}
                                description={story.description}
                                likes={story.likes_count}
                                views={story.views_count}
                                rating={story.average_rating ?? 0}
                                genre={story.genre}
                                author={story.author_username}
                                authorId={story.author}
                                createdAt={story.created_at}
                            />
                        </Link>
                    ))}

                    {totalPages > 1 && (
                        <div style={{ display: "flex", justifyContent: "center", gap: "8px", marginTop: "30px", flexWrap: "wrap" }}>
                            <button onClick={() => setPage((p) => Math.max(1, p - 1))} disabled={page === 1}
                                style={{ padding: "8px 16px", border: "1px solid #ddd", borderRadius: "6px", cursor: "pointer", backgroundColor: page === 1 ? "#f5f5f5" : "#fff" }}>
                                {isRTL ? '← ' : '→ '}{t('body.prev')}
                            </button>
                            {Array.from({ length: Math.min(5, totalPages) }, (_, i) => {
                                const pageNum = Math.max(1, Math.min(totalPages - 4, page - 2)) + i
                                return (
                                    <button key={pageNum} onClick={() => setPage(pageNum)}
                                        style={{ padding: "8px 14px", border: "1px solid #ddd", borderRadius: "6px", cursor: "pointer", backgroundColor: pageNum === page ? "#1a73e8" : "#fff", color: pageNum === page ? "#fff" : "#333" }}>
                                        {pageNum}
                                    </button>
                                )
                            })}
                            <button onClick={() => setPage((p) => Math.min(totalPages, p + 1))} disabled={page === totalPages}
                                style={{ padding: "8px 16px", border: "1px solid #ddd", borderRadius: "6px", cursor: "pointer", backgroundColor: page === totalPages ? "#f5f5f5" : "#fff" }}>
                                {t('body.next')}{isRTL ? ' →' : ' ←'}
                            </button>
                        </div>
                    )}
                </>
            )}
        </div>
    )
}

export default Body
