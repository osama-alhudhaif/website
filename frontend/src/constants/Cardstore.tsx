import { useState, type FC } from "react"

// أضفنا ? لكي يقبل الكود عدم إرسال قيم من الأب (بما أنك وضعت قيم افتراضية)
interface CardstoreProps {
    name?: string
    description?: string
    likes?: number
}

const Cardstore: FC<CardstoreProps> = ({
    name = "osama",
    description = "44",
    likes = 0,
}) => {
    // ملاحظة: إذا كنت لن تغير القيم، استخدم name و description مباشرة من الـ props
    const [nameState] = useState(name)
    const [descriptionState] = useState(description)
    const [likesState] = useState(likes)

    return (
        <div>
            <p>{nameState}</p>
            <p>{descriptionState}</p>
            <p>{likesState}</p>
        </div>
    )
}

export default Cardstore