import React, { useEffect, useRef } from 'react';


const Canvas = ({mazes}) => {
    const canvasRef = useRef(null);

    useEffect(() => {
        const canvas = canvasRef.current;
        if (!canvas) {
            console.error("Canvas element is not available.");
            return;
        }

        const ctx = canvas.getContext("2d");
        const delay = 200;
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        const cellSize = 45;
        const middle = cellSize / 2;

        const drawMaze = (values, index = 0) => {
            if (index > values.length - 1) return;
                const value = values[index];
                ctx.fillStyle = "black";
                const x = value.x;
                const y = value.y;
                let walls = value.walls;
                const left = y * cellSize;
                const top = x * cellSize;
                const midtop = left + middle;
                const midleft = top + middle;

                if (walls[0] === 0) {
                    ctx.fillRect(left, top, cellSize, 1);
                    ctx.fillRect(midleft - 1, midtop - 1, 3, 3);
                }

                if ((value.id != 0) && walls[1] === 0) {
                    ctx.fillRect(left, top, 1, cellSize);
                    ctx.fillRect(midleft - 1, midtop - 1, 3, 3);
                }

                if (walls[2] === 0) {
                    ctx.fillRect(left, top + cellSize - 1, cellSize, 1);
                    ctx.fillRect(midleft - 1, midtop + cellSize - 1, 3, 3);
                }

                if ((value.id != Object.keys(mazes).length - 1) && walls[3] === 0) {
                    ctx.fillRect(left + cellSize - 1, top, 1, cellSize);
                    ctx.fillRect(midleft + cellSize - 1, midtop - 1, 3, 3);
                }

                setTimeout(() => {
                    drawMaze(values, index + 1);
                }, delay);
        };

        if (mazes) {
            const values = Object.values(mazes);
            drawMaze(values);
        }

    }, [mazes]);


    return <canvas ref={canvasRef} width={2000} height={2000}></canvas>
    
}

export default Canvas;