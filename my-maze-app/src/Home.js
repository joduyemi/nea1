import { useState, useEffect } from 'react';
import SerialisedMaze from './SerialisedMaze';
import Canvas from './Canvas';

const Home = () => {
    const[mazes, setMazes] = useState(null);
    const[path, setPath] = useState(null);

    const handleDelete = (id) => {
        const newMazes = mazes.filter((maze) => maze.id !== id);
        setMazes(newMazes);
    }

    useEffect(() => {
        fetch("/api/maze")
            .then((response) => {
                if (response.ok) {
                    return response.json();
                }
                throw new Error("Network response was not ok");
            })
            .then((data) => {
                const myArray = JSON.parse(JSON.parse(String(JSON.stringify(data))).maze_data);
                const myData = myArray.replace(/'/g, '"');
                const mazes2 = JSON.parse(myData);
                console.log(mazes2);
                setMazes(mazes2);
            })
            .catch((error) => console.error("Error fetching maze data: ", error))

        fetch("/api/data")
            .then((response) => {
                if (response.ok) {
                    return response.json();
                }
                throw new Error("Network response was not ok");
            })
            .then((result) => {
                const paths = JSON.parse(JSON.parse(result.data));
                paths.unshift(0);
                setPath(paths);
            })
            .catch((error) => console.error("Error fetching maze data: ", error))
    },[]);

    return (  
        <div className="Home">
        {/*mazes && <SerialisedMaze mazes={mazes} handleDelete={handleDelete}/>*/};
        {mazes && path && <Canvas mazes={mazes} path={path}/>}
        </div>
    );
}
 
export default Home;