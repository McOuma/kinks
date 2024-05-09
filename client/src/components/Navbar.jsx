import React from "react";

function Navbar() {
    return (
        <div>
            <section className="socials ">
                <div className="container">
                    <ul className="d-flex flex-row list-unstyled justify-content-center pt-3">
                        <li className="px-4">
                            <a href=""><i className="bi bi-twitter text-danger"></i></a>
                        </li>
                        <li className="px-4">
                            <a href=""><i className="bi bi-facebook text-danger"></i></a>
                        </li>
                        <li className="px-4">
                            <a href=""><i className="bi bi-instagram text-danger"></i></a>
                        </li>
                        <li className="px-4">
                            <a href=""><i className="bi bi-threads text-danger"></i></a>
                        </li>
                        <li className="px-4">
                            <a href=""><i className="bi bi-envelope-at text-danger"></i></a>
                        </li>

                    </ul>
                </div>

            </section>
            <header>
                <nav className="navbar navbar-expand-lg navbar-light ">

  <div className="container">
    <a className="navbar-brand fs-2 fw-light text-danger" href="#">Kinks&Queens</a>
    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span className="navbar-toggler-icon"></span>
    </button>
    <div className="collapse navbar-collapse justify-content-end" id="navbarNav">
      <ul className="navbar-nav">
        <li className="nav-item ">
          <a className="nav-link active text-danger" aria-current="page" href="#">About Us</a>
        </li>
        <li className="nav-item ">
          <a className="nav-link active text-danger" href="#">Afro Styles</a>
        </li>
        <li className="nav-item ">
          <a className="nav-link active text-danger" href="#">Blogs</a>
        </li>
          <li className="nav-item ">
              <a className="nav-link active text-danger" href="#">Afro Products</a>
          </li>
          <li className="nav-item ">
              <a className="nav-link active text-danger" href="#">Find a Salon</a>
          </li>
          <li className="nav-item ">
              <a className="nav-link active text-danger" href="#">Contact Us</a>
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
