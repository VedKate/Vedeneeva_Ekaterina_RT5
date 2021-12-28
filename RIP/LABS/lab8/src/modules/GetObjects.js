const getObjects = async () =>{
    return await fetch('http://localhost:53149/Street/', {method: "GET"})
        .then((response) => {
            return response.json();
        }).catch(() => {
            return {resultCount: 0, results: []}
        })
}

export default getObjects