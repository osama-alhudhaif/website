import { useState, useEffect } from "react"
import { Link } from "react-router-dom"
import Cardstore from "./Cardstore"

interface Story {
    id: number
    title: string
    description: string
    likes_count: number
}

const Body = () => {
    const [stories, setStories] = useState<Story[]>([])
    const [loading, setLoading] = useState(true)

useEffect(() => {
    const token = localStorage.getItem('token')
    if (!token) return
    
    fetch('http://localhost:8000/api/v1/stories/stories/', {
        headers: {
            'Authorization': `Token ${token}`
        }
    })
        .then(res => res.json())
        .then(data => {
            setStories(Array.isArray(data) ? data : data.results || [])
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
                        description={story.description} 
                        likes={story.likes_count} 
                    />
                </Link>
            ))}
        </div>
    )
}

export default Body