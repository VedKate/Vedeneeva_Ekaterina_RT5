import { Link } from "react-router-dom";
import HeaderComp from "../components/HeaderComp.js";



function ObjectPage(params) {
    const StreetList = params.location.data
    return (
        <div>
            <HeaderComp></HeaderComp>
            <h2>{StreetListList.StreetName}</h2>
            <Link to="/Street"><button>Назад</button></Link>
        </div>
    );
}

export default ObjectPage;