import { useState, useEffect } from "react"
import { Link } from "react-router-dom"
import Cardstore from "./Cardstore"

interface Story {
    id: number
    title: string
    synopsis: string
    likes_count: number
}

const Body = () => {
    const [stories, setStories] = useState<Story[]>([])
    const [loading, setLoading] = useState(true)

    useEffect(() => {
        fetch('/api/v1/stories/stories/')
            .then(res => res.json())
            .then(data => {
                setStories(data.results || data)
                setLoading(false)
            })
            .catch(err => {
                console.error('Failed to fetch stories:', err)
                setLoading(false)
            })
    }, [])

    if (loading) return <div>جاري التحميل...</div>

    return (
        <div>
            {stories.map(story => (
                <Link key={story.id} to={`/reading/${story.id}`} style={{ textDecoration: 'none', color: 'inherit' }}>
                    <Cardstore 
                        name={story.title} 
                        description={story.synopsis} 
                        likes={story.likes_count} 
                    />
                </Link>
            ))}
        </div>
    )
}

export default Body

