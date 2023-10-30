import React, { useState, useEffect, useRef } from 'react';


const Canvas = ({mazes, path}) => {
    const canvasRef = useRef(null);
    path.push(0);
    const [mazeDrawn, setMazeDrawn] = useState(false);
    useEffect(() => {
        const canvas = canvasRef.current;
        if (!canvas) {
            console.error("Canvas element is not available.");
            return;
        }
        const values = Object.values(mazes);
        const row_len = parseInt(Math.sqrt(values.length))
        const sorted = path.slice().sort((a, b) => {
            const columnA = a % row_len;
            const columnB = b % row_len;

            if (columnA !== columnB) {
                return columnA - columnB;
            }

            return a - b;
        })

        const ctx = canvas.getContext("2d");
        const delay = 50;

        const cellSize = 45;
        const middle = cellSize / 2;

        const drawMaze = (values, index = 0) => {
            if (index >= values.length) {
                setMazeDrawn(true);
                drawPath(values, sorted);
                return;
            }
                const value = values[index];
                const x = value.x;
                const y = value.y;
                let walls = value.walls;
                const left = y * cellSize;
                const top = x * cellSize;

                ctx.fillStyle = "black";

                if (walls[0] === 0) {
                    ctx.fillRect(left, top, cellSize, 1);
                }

                if ((value.id != 0) && walls[1] === 0) {
                    ctx.fillRect(left, top, 1, cellSize);
                }

                if (walls[2] === 0) {
                    ctx.fillRect(left, top + cellSize - 1, cellSize, 1);
                }

                if ((value.id != Object.keys(mazes).length - 1) && walls[3] === 0) {
                    ctx.fillRect(left + cellSize - 1, top, 1, cellSize);
                }

                setTimeout(() => {
                    drawMaze(values, index + 1);
                }, 10);
        };

        const drawPath = (values, sortedPath) => {
            if (!mazeDrawn) {
                setTimeout(() => {
                    drawPath(values, sortedPath);
                }, delay);
                return;
            }
            let currentIndex = 0;
            
            const drawNextCell = () => {
                if (currentIndex >= sortedPath.length) return;
                const cellIndex = sortedPath[currentIndex];
                const value = values[cellIndex];
                ctx.fillStyle = "blue";
                const x = value.x;
                const y = value.y;
                const left = y * cellSize;
                const top = x * cellSize;
                const midtop = top + middle;
                const midleft = left + middle;
                ctx.fillRect(midleft, midtop, 3, 3);

                currentIndex++;

                setTimeout(drawNextCell, delay);

        }

        drawNextCell();
        };

        if (mazes) {
            drawMaze(values);
            drawPath(values, sorted);
        }


    }, [mazes, mazeDrawn]);


    return <canvas ref={canvasRef} width={2000} height={2000}></canvas>
    
}

export default Canvas;