import { Link } from "react-router-dom";
import HeaderComp from "../components/HeaderComp.js";

function HomePage() {
    return (
        <div>
            <HeaderComp></HeaderComp>
            <h2>Главная страница</h2>
            <p>Данное веб-приложение использует React для создания пользовательского интерфейса.</p>
            <p>Приложение взаимодействует с базой данных.</p>
            <Link to="/Street"><button>Список объектов БД</button></Link>
        </div>
    );
}

export default HomePage;