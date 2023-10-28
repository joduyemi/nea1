import { useState, useEffect } from 'react';
import SerialisedMaze from './SerialisedMaze';

const Home = () => {
    const datax = [];
    const[mazes, setMazes] = useState(null);

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
                throw new Error("Network response was not ok,")
            })
            .then((data) => {
                const myArray = JSON.parse(JSON.parse(String(JSON.stringify(data))).maze_data);
                const myData = myArray.replace(/'/g, '"');
                const mazes = JSON.parse(myData);
                setMazes(mazes);
            
            })
            .catch((error) => console.error("Error fetching maze data: ", error))
    },[]);

    return (  
        <div className="Home">
        {mazes && <SerialisedMaze mazes={mazes}/>}
        </div>
    );
}
 
export default Home;