import React, {useState, useEffect} from 'react';
import { Link, useNavigate } from 'react-router-dom';
import Tips from '../components/Tips';
import axios from "axios";


function Main() {
    const [tips, setTips] = useState([]);
    const navigate = useNavigate();

    const getData = async () => { axios.get("http://127.0.0.1:8000/tips/all/").then((response) => setTips(response.data)); };
    
    useEffect(() => {
        getData();

        const interval = setInterval(getData, 10000);

        return () => {
            clearInterval(interval);
        };
    }, []);

    return (
        <>
            <h1>메인페이지 테스트</h1>
            <Tips tips={tips} onClickTip={ (item) =>{ navigate(`/tips/${item.animal.name}`)} } />
            <Link to="/">Main</Link>
        </>
    );
};

export default Main;