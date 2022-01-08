import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import HeaderComp from "../components/HeaderComp.js";
import getObjects from "../modules/GetObjects.js";


function ListPage() {

    const [StreetList, setStreetList] = useState([])
    const [StreetNames, setStreetNames] = useState([])

    const handleObjectsList = async () => {

        const street_list = []
        const Streets = await getObjects()
        for (let Street of Streets) {
            street_list.push(Street['StreetName']);
        }
        setStreetList(Streets)
        setStreetNames(street_list)

    }


    useEffect(()=>{
        handleObjectsList()
    }, [])

    return (
        <div>
            <HeaderComp></HeaderComp>
            <h2>Таблица Streets </h2>
            <ul>
                {StreetNames.map((StreetName)=>{
                    return (
                        <li key={StreetName}>
                            <Link to={{pathname: "/Street/object", data: StreetList.find(obj => obj.StreetName == StreetName)}}>{StreetName}</Link>
                        </li>
                    )
                })}
            </ul>
        </div>
    );
}

export default ListPage;