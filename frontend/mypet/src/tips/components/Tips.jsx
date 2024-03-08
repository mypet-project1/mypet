import Tip from "./Tip";

function Tips(props) {
    const { tips, onClickTip } = props;

    return (
        <div>
            {tips.map((tip, index) => (
                <Tip key={tip.id} tip={tip} onClick={() => { onClickTip(tip); }} />
            ))}
        </div>
    );
};

export default Tips;