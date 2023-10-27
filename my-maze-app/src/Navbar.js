const Navbar = () => {
    return (  
        <nav className="navbar">
            <h1>Find your path</h1>
            <div className="links"></div>
            <a href="/">Home</a>
            <a href="/mazes" style={{
                color:"white",
                backgroundColor: '#f1356d',
                borderRadius: "8px",
            }}>Create a new maze</a>
        </nav>
    );
}
 
export default Navbar;