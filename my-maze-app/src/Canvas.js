import React, { useEffect, useRef } from 'react';


const Canvas = ({mazes}) => {
    const canvasRef = useRef();

    useEffect(() => {
        const canvas = canvasRef.current;
        if (!canvas) {
            console.error("Canvas element is not available.");
            return;
        }

        const ctx = canvas.getContext("2d");
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        const cellSize = 50;

        if (mazes) {
            console.log(typeof(mazes));
            const values = Object.values(mazes);
            for (const value of values) {
                ctx.fillStyle = "black";
                const x = value.x;
                const y = value.y;
                let walls = [];
                walls = value.walls;
                const left = y * cellSize;
                const top = x * cellSize;

                if (walls[0] === 0) {
                    ctx.fillRect(left, top, cellSize, 2);
                }

                if ((value.id != 0) && walls[1] === 0) {
                    ctx.fillRect(left, top, 2, cellSize);
                }

                if (walls[2] === 0) {
                    ctx.fillRect(left, top + cellSize - 2, cellSize, 2);
                }

                if ((value.id != Object.keys(mazes).length - 1) && walls[3] === 0) {
                    ctx.fillRect(left + cellSize - 2, top, 2, cellSize);
                }
            }

        }
    }, [mazes]);

    return <canvas ref={canvasRef} width={2000} height={2000}></canvas>
    
}

export default Canvas;