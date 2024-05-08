import React from "react";

function Navbar() {
    return (
        <div>
            <header>
                <nav className="navbar navbar-expand-lg bg-body-tertiary">
  <div className="container">
    <a className="navbar-brand fs-2 fw-light text-danger" href="#">Kinks&Queens</a>
    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span className="navbar-toggler-icon"></span>
    </button>
    <div className="collapse navbar-collapse justify-content-end" id="navbarNav">
      <ul className="navbar-nav">
        <li className="nav-item ">
          <a className="nav-link active text-danger" aria-current="page" href="#">Home</a>
        </li>
        <li className="nav-item ">
          <a className="nav-link active text-danger" href="#">Content</a>
        </li>
        <li className="nav-item ">
          <a className="nav-link active text-danger" href="#">Products</a>
        </li>
          <li className="nav-item ">
              <a className="nav-link active text-danger" href="#">Sign Up</a>
          </li>
      </ul>
    </div>
  </div>
</nav>
</header>

        </div>
    );
}

export default Navbar;
