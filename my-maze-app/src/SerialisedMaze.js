const SerialisedMaze = ({mazes, handleDelete}) => {
    return ( 
        <div className="serialised-maze">
            {mazes.map((maze) => (
                <div className="node" key={maze.id}>
                    <p>{maze.x}, {maze.y}, {maze.walls}</p>
                    <button onClick={() => handleDelete(maze.id)}>delete node</button>
                </div>

            ))}
        </div>
     );
}
 
export default SerialisedMaze;