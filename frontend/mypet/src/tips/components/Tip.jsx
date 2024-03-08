function Tip(props) {
    const { tip, onClick } = props;


    return (
        <p onClick={onClick}>{tip.animal.name}, {tip.user}, {tip.content}</p>
    )
}

export default Tip;