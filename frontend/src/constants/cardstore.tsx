interface CardstoreProps {
    name: string
    description: string
    likes: number
}

const Cardstore: FC<CardstoreProps> = ({
    name = "osama",
    description = "test",
    likes = 0,
}) => {
    const [nameState, setNameState] = useState(name)
    const [descriptionState, setDescriptionState] = useState(description)
    const [likesState, setLikesState] = useState(likes)

    return (
        <div>
            <p>{nameState}</p>
            <p>{descriptionState}</p>
            <p>{likesState}</p>
        </div>
    )
}

export default Cardstore

