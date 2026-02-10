import { useState } from "react"
import Cardstore from "./Cardstore"

const Body = () => {
    const [nameState] = useState("osama")
    const [descriptionState] = useState("44")
    const [likesState] = useState(0)

    const [nameStatesence] = useState("ali")
    const [descriptionStatesence] = useState("55")
    const [likesStatesence] = useState(100)

    return (
        <div>
            <Cardstore name={nameState} description={descriptionState} likes={likesState} />
            <Cardstore name={nameStatesence} description={descriptionStatesence} likes={likesStatesence} />
        </div>
    )
}

export default Body

