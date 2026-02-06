import { useState, type FC } from "react"

interface CardstoreProps {
    name: string
    description: string
    likes: number
}

const Cardstore: FC<CardstoreProps> = ({
    name = "osama",
    description = "44",
    likes = 0,
}) => {
    const [nameState, ] = useState(name)
    const [descriptionState, ] = useState(description)
    const [likesState, ] = useState(likes)

    return (
        <div>
            <p>{nameState}</p>
            <p>{descriptionState}</p>
            <p>{likesState}</p>
        </div>
    )
}

export default Cardstore
