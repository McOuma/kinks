import "./footer.css"

function Footer (){
    return(
        <div>
            <footer className="bg bg-light">
                <section className="one">
                <div className="container">
                    <div className="row">
                        <div className="col-sm-2">
                            < a className="text-decoration-none" href="">
                            <p className="fw-medium pt-3 text-danger">About Us</p>
                            </a>
                        </div>
                        <div className="col-sm-2">
                            < a className="text-decoration-none" href="">
                            <p className="fw-medium text-danger pt-3">Collections</p>
                            </a>
                            <div className="d-flex flex-column">
                                <a className="text-decoration-none text-dark" href="">
                                    <p>Afro Styles</p>
                                </a>
                                <a className="text-decoration-none text-dark"  href="">
                                    <p>Kids</p>
                                </a>

                                <a className="text-decoration-none text-dark"  href="">
                                    <p>Crochet</p>
                                </a>

                            </div>
                        </div>
                        <div className="col-sm-2">
                            <a className="text-decoration-none" href="">
                            <p className="fw-medium pt-3 text-danger">Find a Salon</p>
                            </a>
                        </div>
                        <div className="col-sm-2">
                            <a className="text-decoration-none" href="">
                            <p className=" fw-medium pt-3 text-danger">Contact Us</p>
                            </a>
                        </div>
                        <div className="col-sm-4">
                            <p className="fw-medium pt-3 text-danger text-center">Subscribe </p>
                            <div className='d-flex flex-column justify-content-center'>
                                <p className="text-center">Stay connected to receive updates on tips and products </p>
                                <form className='d-flex flex-row '>
                                    <input className="form-control custom-input" type="search" placeholder="Email Address"
                                           aria-label="Search"/>
                                    <button className="btn btn-outline-danger" type="submit">Subscribe</button>
                                </form>
                                <ul className="d-flex flex-row list-unstyled pt-3 px-5">
                                    <li className="pe-3">
                                        <a href="">
                                            <i className="bi bi-twitter text-danger"></i>
                                        </a>
                                    </li>
                                    <li className="px-3">
                                        <a href="">
                                            <i className="bi bi-facebook text-danger"></i>
                                        </a>
                                    </li>
                                    <li className="px-3">
                                        <a href="">
                                            <i className="bi bi-instagram text-danger"></i>
                                        </a>
                                    </li>
                                    <li className="px-3">
                                        <a href="">
                                            <i className="bi bi-threads text-danger"></i>
                                        </a>
                                    </li>
                                    <li className="px-3">
                                        <a href="">
                                            <i className="bi bi-whatsapp text-danger"></i>
                                        </a>
                                    </li>

                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
                </section>
                <hr/>
                <section className="two">
                    <div className="d-flex justify-content-center flex-row">
                        <a className="text-decoration-none text-danger" href="">
                        <p className="fs-6 fw-bold text-center px-5">Terms and Condition</p>
                        </a>
                        <a className="text-decoration-none text-danger" href="">
                        <p className="fs-6 fw-bold text-center px-5">Privacy Policy</p>
                        </a>
                        <p className="fs-6 fw-bold text-center px-5 text-danger">Copyright</p>
                    </div>
                </section>
            </footer>
        </div>
    )
}

export default Footer;